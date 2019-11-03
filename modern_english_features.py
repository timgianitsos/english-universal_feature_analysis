# pylint: disable = missing-docstring
'''
Modern English features
'''

from qcrit.textual_feature import textual_feature, setup_tokenizers

TERMINAL_PUNCTUATION = ('.', '?', '!')
setup_tokenizers(terminal_punctuation=TERMINAL_PUNCTUATION)

@textual_feature()
def foobar1(text):
	return 0

@textual_feature()
def foobar2(text):
	return 0
