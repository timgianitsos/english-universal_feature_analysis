# pylint: disable = missing-docstring
'''
Modern English features
'''

import re
from statistics import mean
from collections import defaultdict, Counter
from string import punctuation

from qcrit.textual_feature import textual_feature, setup_tokenizers

TERMINAL_PUNCTUATION = ('.', '?', '!')
setup_tokenizers(terminal_punctuation=TERMINAL_PUNCTUATION, language='english')

_WORD_REGEX = re.compile(r'^\w+$')
_ALL_PUNCTUATION_MARKS = f'{punctuation}‘’“”' #include slant quotes
_DEGENERATE_PLACEHOLDER = '@'
assert not _WORD_REGEX.match(_DEGENERATE_PLACEHOLDER) and len(_DEGENERATE_PLACEHOLDER) >= 1

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
	total_cnt = sum(len(word) for word in text)
	return lowercase_cnt / total_cnt

@textual_feature(tokenize_type=None)
def ratio_punctuation_to_spaces(text):
	punctuation_cnt = sum(text.count(punc) for punc in _ALL_PUNCTUATION_MARKS)
	space_cnt = text.count(' ')
	return punctuation_cnt / space_cnt

@textual_feature(tokenize_type='words')
def mean_word_length(text):
	return mean(len(word) for word in text if _WORD_REGEX.match(word))

def _counter_helper(generator, sentence_cnt):
	counts = Counter(generator)
	sent_cnt_with_only_non_words = counts[_DEGENERATE_PLACEHOLDER]
	del counts[_DEGENERATE_PLACEHOLDER] #remove placeholder for sentences with only non-words
	assert len(counts) != 0, f'Parsed invalid file with only non-word characters'
	return counts.most_common(1)[0][1] / (sentence_cnt - sent_cnt_with_only_non_words)

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_stop_word(text):
	return _counter_helper(
		(
			#Search backward for last word token in sentence
			next((word for word in reversed(sentence) if _WORD_REGEX.match(word)), _DEGENERATE_PLACEHOLDER)
			for sentence in text
		),
		len(text)
	)

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_word(text):
	return _counter_helper(
		(
			#Search forward for first word token in sentence
			next((word for word in sentence if _WORD_REGEX.match(word)), _DEGENERATE_PLACEHOLDER)
			for sentence in text
		),
		len(text)
	)

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_letter_start_word(text):
	return _counter_helper(
		(
			next((word for word in sentence if _WORD_REGEX.match(word)), _DEGENERATE_PLACEHOLDER)[0].lower()
			for sentence in text
		),
		len(text)
	)

@textual_feature(tokenize_type='sentence_words')
def freq_most_frequent_start_letter_stop_word(text):
	start_letter_stop_word_freqs = defaultdict(int)
	for sentence in text:
		start_letter_stop_word_freqs[sentence[-1][0]] += 1
	return max(start_letter_stop_word_freqs.values()) / sum(start_letter_stop_word_freqs.values())

@textual_feature(tokenize_type='words')
def num_single_occurrence_words(text):
	word_freqs = defaultdict(int)
	for word in text:
		word_freqs[word] += 1
	return sum(1 for frequency in word_freqs.values() if frequency == 1) / len(word_freqs.keys())

@textual_feature(tokenize_type='words')
def num_double_occurrence_words(text):
	word_freqs = defaultdict(int)
	for word in text:
		word_freqs[word] += 1
	return sum(1 for frequency in word_freqs.values() if frequency == 2) / len(word_freqs.keys())

@textual_feature(tokenize_type='words')
def num_words_given_word_length(text):
	# Hard-coded frequency for word length 4 for now
	given_word_length = 4

	wordlength_freqs = defaultdict(int)
	for word in text:
		wordlength_freqs[len(word)] += 1
	return wordlength_freqs[given_word_length] / sum(wordlength_freqs.values())

@textual_feature(tokenize_type='words')
def num_words_given_interval_word_length(text):
	# Hard-coded frequency for word lengths 3-5 for now
	given_word_length_interval = (3, 5)

	wordlength_freqs = defaultdict(int)
	for word in text:
		wordlength_freqs[len(word)] += 1
	return sum(wordlength_freqs[length] for length in \
				 range(given_word_length_interval[0], \
					   given_word_length_interval[1]+1)) / sum(wordlength_freqs.values())

@textual_feature(tokenize_type=None)
def num_vowels(text):
	vowels = ['a', 'e', 'i', 'o', 'u']
	return sum(text.count(vowel) for vowel in vowels) / len(text)
