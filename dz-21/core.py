from requests_html import HTMLSession
from string import punctuation
from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk
from datetime import datetime


STOP_WORDS = set(stopwords.words('english'))
STOP_WORDS_SPECIFIED = '...../[]^-–, '

def check_punctuation_stop_words(word):
    return word not in punctuation \
        and (word not in STOP_WORDS) \
        and (word not in STOP_WORDS_SPECIFIED) \
        and ('.' not in word) \
        and ('-' not in word) \
        and len(word) > 2


def get_text_from_url(url, xpath='//div[@class="mw-parser-output"]'):
    session = HTMLSession()
    response = session.get(url)
    text = response.html.xpath(xpath)[0].text
    return text


def get_tokenized_words(text):
    # do the nlp stuff
    tokenized = nltk.word_tokenize(text)
    all_words = nltk.pos_tag(tokenized)
    return all_words


def get_list_filter_words(all_words, only_nouns=True):
    if only_nouns:
        words = [word for (word, pos) in all_words if check_punctuation_stop_words(word) and pos[:2] == 'NN']
    else:
        words = [word.lower() for (word, pos) in all_words if check_punctuation_stop_words(word)]
    return words


def get_frequency_phrases(words):
    frequency_phrases = {}
    for word in words:
        if word in frequency_phrases:
            frequency_phrases[word] += 1
        else:
            frequency_phrases[word] = 1
    return frequency_phrases


def get_bigramm(list_words, frequency_phrases):
    bigrams = ngrams(list_words, 2)
    bigrams = [gr for gr in bigrams]
    bigram = [(word, pos) for word, pos in bigrams if frequency_phrases.get(word)]
    return bigram


def write_bigram_to_txt(sort_bigram):
    now = datetime.now().strftime("%d-%m-%y_%H_%M")
    text_file = f'sort_bigram_{now}.txt'
    print(text_file)
    with open(text_file, 'w', encoding='utf-8') as f:
        for word1, word2 in sort_bigram:
            f.write(f"{word1} - {word2}\n")
            f.flush()
    f.close()
    print("Write bigram to txt")