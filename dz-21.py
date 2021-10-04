from selenium import webdriver
from string import punctuation
from nltk.corpus import stopwords
from nltk.util import ngrams
import nltk
# mw-parser-output

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Neil_Armstrong")

STOP_WORDS = set(stopwords.words('english'))
STOP_WORDS_2 = '...../[]^-–, '

text = driver.find_element_by_class_name("mw-parser-output").text
driver.close()

# function to test if something is a noun
is_noun = lambda word, pos: pos[:2] == 'NN' \
                            and (word not in punctuation) \
                            and (word not in STOP_WORDS) \
                            and (word not in STOP_WORDS_2)\
                            and ('.' not in word) \
                            and ('-' not in word) \
                            and len(word)>2
# do the nlp stuff
tokenized = nltk.word_tokenize(text)
all_words = nltk.pos_tag(tokenized)
nouns = [word for (word, pos) in all_words if is_noun(word, pos)]
frequency_phrases = {}

for word in nouns:
    if word in frequency_phrases:
        frequency_phrases[word] += 1
    else:
        frequency_phrases[word] = 1

sort_frequency_phrases = sorted(frequency_phrases.items(), key=lambda x: x[1], reverse=True)
#print(sort_frequency_phrases)


#*******************************************************************
# BIGRAMM
list_words = [word for word, pos in all_words]
bigramms = ngrams(list_words, 2)

bigramms = [gr for gr in bigramms]

nouns_bigram = [(word, pos) for word, pos in bigramms if frequency_phrases.get(word)]
sort_nouns_bigram = sorted(nouns_bigram, key=lambda x: x[0])

with open('sort_nouns_bigram.txt', 'w', encoding='utf-8') as f:
    for word1, word2 in sort_nouns_bigram:
        f.write(f"{word1} - {word2}\n")
        f.flush()
f.close()