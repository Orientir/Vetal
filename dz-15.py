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

class Title(Page):
    def __init__(self, domen, zone, keywords, ssl=True):
        Page.__init__(self, domen, zone, keywords, ssl)
        self.keywords = keywords

    def __eq__(self, other):
        return self.keywords == other.keywords

    def __ne__(self, other):
        return self.keywords != other.keywords

    def __lt__(self, other):
        return len(self.keywords) < len(other.keywords)

    def __gt__(self, other):
        return len(self.keywords) > len(other.keywords)

    def __le__(self, other):
        return len(self.keywords) <= len(other.keywords)

    def __ge__(self, other):
        return len(self.keywords) >= len(other.keywords)

    def get_len(self):
        return len(self.keywords)

    def get_keywords(self):
        return self.keywords



page1 = Title(domen='google.com', zone='com', keywords=['yandex', 'python', 'methods', 'length'])
page2 = Title(domen='yandex.com', zone='com', keywords=['yandex', 'python', 'methods', 'length'])

print(page1 < page2)


