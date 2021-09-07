def some():
    print('hi')

class Website:
    def __init__(self, domen, zone, ssl=True):
        self.domen = domen
        self.zone = zone
        self.ssl = ssl
        self.url = f'https://{self.ssl}' if ssl else f'http://{self.ssl}'

    def get_url(self):
        return self.url


#Page, SearchEngine, Text, Title
class Page(Website):
    def __init__(self, domen, zone, keywords, ssl=True):
        Website.__init__(self, domen, zone, ssl)
        self.keywords = keywords

    def get_keywords(self):
        return ', '.join(self.keywords)

    def get_domen(self):
        return self.domen


class Title(Page):
    def __init__(self, domen, zone, keywords, ssl=True):
        Page.__init__(self, domen, zone, keywords, ssl)
        self.keywords = keywords

    def get_len(self):
        return 50

class SearchEngine:
    engine = 'google.com'
    def __init__(self, query):
        self.query = query

    def get_url_parse(self):
        return f'https://{self.engine}/search?q={self.query}'

class Text:
    def __init__(self, text):
        self.text = text

    def get_lines(self):
        return self.text.split(' ')

    def some(self):
        print('inside')

    def save_to_file(self):
        with open('SAVE_file_CLASS', 'w', encoding='utf-8') as f:
            lines = self.get_lines()
            f.writelines(lines)
            f.close()
            self.some()


site = Website(domen='google.com', zone='com')
page = Page(domen='google.com', zone='com', keywords=['list', 'python', 'methods'])
print(page.get_domen())
title = Title(domen='google.com', zone='com', keywords=['list', 'python', 'methods'])
print(title.get_len())
search = SearchEngine(query='python')
print(search.get_url_parse())
t = '''
111111111
222222222222
3333333333
44444444444
55555555555
'''
text = Text(t)
text.save_to_file()
text.some()
some()
