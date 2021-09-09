class Title():
    def __init__(self, domen, zone, keywords, ssl=True):
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