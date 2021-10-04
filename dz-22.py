import re
from uuid import uuid4
from urllib.parse import unquote
from requests_html import HTMLSession


def get_images_from_google(keyword):
    url = f'https://www.google.com/search?q={keyword}&tbm=isch'

    with HTMLSession() as session:
        response = session.get(url)

    # expr = re.compile(r',\[\"(.*)\",')
    expr = re.compile(',\[\"(.*)\",')
    matches = re.findall(expr, response.text)
    print(len(matches))
    img_types = {'.jpg', '.png', '.webp', '.gif'}
    images = []
    for match in matches:
        # print(match)
        if not any(tp in match for tp in img_types):
            # print('------------------')
            continue
        img = match.split('?')[0]
        # print(img)
        # print('*****************')
        images.append(unquote(img))
    return images

images = get_images_from_google('cats')
print(images)