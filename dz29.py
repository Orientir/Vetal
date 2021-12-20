import re
import random
from urllib.parse import unquote
from requests_html import HTMLSession

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost, EditPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media

from slugify import slugify

XML_RPC_API = 'http://wp.py4you.com/xmlrpc.php'
USER = 'admin'
PASS = 'Admin123456'

wp_client = Client(XML_RPC_API, USER, PASS)
all_posts = wp_client.call(GetPosts())

def get_images_from_google(keyword):
    url = f'https://www.google.com/search?q={keyword}&tbm=isch'

    with HTMLSession() as session:
        response = session.get(url)

    regex = r'\[\"(.*?)\",'
    matches = re.findall(regex, response.text)

    img_types = {'.jpg', '.png', '.webp', '.gif'}
    images = []
    for match in matches:
        if not any(tp in match for tp in img_types):
            continue
        img = match.split('?')[0]
        images.append(unquote(img))
    return images

def save_image(img_url):
    try:
        with HTMLSession() as session:
            response = session.get(img_url, timeout=4)
            assert response.status_code == 200
    except Exception as e:
        print(e, type(e))
        return False
    image_name = img_url.split('/')[-1]
    img_path = f'dz29/images/{image_name}'
    try:
        with open(img_path, 'wb') as f:
            f.write(response.content)

        print(f'[SAVED] {img_url}')
    except Exception as e:
        print("EXCEPTION format: ", e)
        return False
    return img_path

keyword = input('Введите ключевое слово: ')
name_surname = slugify("Виталий Козаченко")
TITLE = f"{name_surname}: KEY - {keyword}"

session = HTMLSession()
resp = session.get(f'https://www.google.com/search?q={keyword}&num=10&hl=en')

links = resp.html.xpath('//div[@class="yuRUbf"]/a[1]/@href')
random_links = random.choices(links, k=3)

bad_text = ['function()', 'script', 'position:']
text = ''
for link in random_links:
    response = session.get(link)
    div = response.html.find('div > p')
    for b in div:
        if len(b.text) > 350 and not any(tag for tag in bad_text if tag in b.text):
            text += b.text
            break

if not text:
    text = 'Paragraph not found'

images = get_images_from_google(keyword)
for image in images:
    image_path = save_image(image)
    if image_path:
        break



file = image_path
file_ext = file.split('.')[-1]

data = {
    'name': file,
    'type': f'image/{file_ext}',
}

# # read the binary file and let the XMLRPC library encode it into base64
with open(file, 'rb') as img:
    data['bits'] = xmlrpc_client.Binary(img.read())

response = wp_client.call(media.UploadFile(data))

post = WordPressPost()
post.title = TITLE
post.content = text
post.terms_names = { 'post_tag': keyword,}
post.post_status = 'publish'
post.thumbnail = response['id']
wp_client.call(NewPost(post))
print ('Post Successfully posted. Its Id is: ')