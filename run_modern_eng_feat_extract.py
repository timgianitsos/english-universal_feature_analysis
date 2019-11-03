# pylint: disable = C0330
'''
Modern English feature extraction
'''

import sys
import os
from io import StringIO

import qcrit.extract_features

from modern_english_features import * #pylint: disable = wildcard-import, unused-wildcard-import
from download_corpus import download_corpus

MODERN_ENGLISH_CORPUS_PATH = ('english-diachronic-corpus', 'Modern_English')

def parse_txt(file_name):
	'''Parse text files'''
	file_text = StringIO()
	with open(file_name, mode='r', encoding='utf-8') as file:
		for line in file:
			file_text.write(line.strip())
			file_text.write(' ')
	return file_text.getvalue()

def feature_extraction(output):
	'''Perform a feature extraction'''
	download_corpus(MODERN_ENGLISH_CORPUS_PATH)
	qcrit.extract_features.main(
		corpus_dir=os.path.join(*MODERN_ENGLISH_CORPUS_PATH),
		file_extension_to_parse_function={
			'txt': parse_txt,
		},
		output_file=output
	)

if __name__ == '__main__':
	feature_extraction(None if len(sys.argv) <= 1 else sys.argv[1])