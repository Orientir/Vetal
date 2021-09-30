from selenium import webdriver
from string import punctuation
from nltk.corpus import stopwords
import nltk
# mw-parser-output

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Neil_Armstrong")

STOP_WORDS = set(stopwords.words('english'))

text = driver.find_element_by_class_name("mw-parser-output").text
driver.close()

# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN' and (pos[:2] not in punctuation) and (pos[:2] not in STOP_WORDS)
# do the nlp stuff
tokenized = nltk.word_tokenize(text)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
print(nltk.pos_tag(tokenized))
frequency_phrases = {}

for word in nouns:
    if word in frequency_phrases:
        frequency_phrases[word] += 1
    else:
        frequency_phrases[word] = 1

sort_frequency_phrases = sorted(frequency_phrases.items(), key=lambda x: x[1], reverse=True)
#print(sort_frequency_phrases)