# pylint: disable = missing-docstring
'''
Modern English features
'''

from statistics import mean

from qcrit.textual_feature import textual_feature, setup_tokenizers

from collections import defaultdict

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

@textual_feature(tokenize_type='words')
def ratio_lowercase_to_totalchars(text):
	lowercase_cnt = sum(1 for word in text for letter in word if letter.islower())
	total_cnt = sum(1 for word in text for letter in word)
	return lowercase_cnt / total_cnt

@textual_feature(tokenize_type=None)
def ratio_punctuation_to_spaces(text):
	punctuation_signs = ['.', ',', ';', '!', '?','\'', '\"', '(', ')', '-']
	punctuation_cnt = sum(text.count(punc) for punc in punctuation_signs)
	space_cnt = text.count(' ')
	return punctuation_cnt / space_cnt

@textual_feature(tokenize_type='words')
def ratio_numeric_to_alpha(text):
	numeric_cnt = sum(1 for word in text for char in word if char.isnumeric())
	total_cnt = sum(1 for word in text for letter in word)
	return numeric_cnt / total_cnt

@textual_feature(tokenize_type='words')
def mean_word_length(text):
	return mean(len(word) for word in text)

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_stop_word(text):
	stop_word_freqs = defaultdict(int)
	for sentence in text:
		stop_word_freqs[sentence[-1]] += 1
	return max(stop_word_freqs.values())

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_word(text):
	start_word_freqs = defaultdict(int)
	for sentence in text:
		start_word_freqs[sentence[0]] += 1
	return max(start_word_freqs.values())

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_letter_start_word(text):
	start_letter_start_word_freqs = defaultdict(int)
	for sentence in text:
		for letter in sentence[0]:
			start_letter_start_word_freqs[letter[0]] += 1
	return max(start_letter_start_word_freqs.values())

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_letter_stop_word(text):
	start_letter_stop_word_freqs = defaultdict(int)
	for sentence in text:
		for letter in sentence[-1]:
			start_letter_stop_word_freqs[letter[0]] += 1
	return max(start_letter_stop_word_freqs.values())

@textual_feature(tokenize_type='words')
def num_single_occurrence_words(text):
	word_freqs = defaultdict(int)
	for word in text:
		word_freqs[word] += 1
	return sum(1 for frequency in word_freqs.values() if frequency == 1)

@textual_feature(tokenize_type='words')
def num_double_occurrence_words(text):
	word_freqs = defaultdict(int)
	for word in text:
		word_freqs[word] += 1
	return sum(1 for frequency in word_freqs.values() if frequency == 2)

@textual_feature(tokenize_type='words')
def num_words_given_word_length(text):
	# Hard-coded frequency for word length 4 for now
	given_word_length = 4

	wordlength_freqs = defaultdict(int)
	for word in text:
		wordlength_freqs[len(word)] += 1
	return wordlength_freqs[given_word_length]

@textual_feature(tokenize_type='words')
def num_words_given_interval_word_length(text):
	# Hard-coded frequency for word lengths 3-5 for now
	given_word_length_interval = (3,5)

	wordlength_freqs = defaultdict(int)
	for word in text:
		wordlength_freqs[len(word)] += 1
	return sum(wordlength_freqs[length] for length in \
				 range(given_word_length_interval[0], \
					   given_word_length_interval[1]+1))

@textual_feature(tokenize_type=None)
def num_vowels(text):
	vowels = ['a','e','i','o','u']
	return sum(text.count(vowel) for vowel in vowels)
