# pylint: disable = missing-docstring
'''
Modern English features
'''

from statistics import mean

from qcrit.textual_feature import textual_feature, setup_tokenizers

TERMINAL_PUNCTUATION = ('.', '?', '!')
setup_tokenizers(terminal_punctuation=TERMINAL_PUNCTUATION)

@textual_feature(tokenize_type='sentence_words')
def average_sentence_length(text):
	return mean(sum(len(word) for word in sentence) for sentence in text)

@textual_feature(tokenize_type='words')
def ratio_capital_to_lowercase(text):
	capital_cnt = sum(1 for word in text for letter in word if letter.isupper())
	lowercase_cnt = sum(1 for word in text for letter in word if letter.islower())
	return capital_cnt / lowercase_cnt
