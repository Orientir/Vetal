from core import *

PAGE_URL = "https://en.wikipedia.org/wiki/Neil_Armstrong"

if __name__ == '__main__':
    # **************  FREQUENCY PHRASES  ***************
    text = get_text_from_url(PAGE_URL)
    all_words = get_tokenized_words(text)
    nouns_words = get_list_filter_words(all_words)
    frequency_phrases = get_frequency_phrases(nouns_words)
    sort_frequency_phrases = sorted(frequency_phrases.items(), key=lambda x: x[1], reverse=True)

    # ******************  BIGRAM  **********************
    list_words = get_list_filter_words(all_words, only_nouns=False)
    bigram = get_bigramm(list_words, frequency_phrases)
    sort_bigram = sorted(bigram, key=lambda x: x[0])
    write_bigram_to_txt(sort_bigram)