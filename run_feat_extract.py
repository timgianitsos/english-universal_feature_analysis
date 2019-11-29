'''
Modern English feature extraction
'''

import sys
import os
import re
from io import StringIO
import getopt

import qcrit.extract_features

from modern_english_features import * #pylint: disable = wildcard-import, unused-wildcard-import
from download_corpus import download_corpus

def parse_txt(file_name):
	'''Parse text files'''
	file_text = StringIO()
	with open(file_name, mode='r', encoding='utf-8') as file:
		text_name = os.path.splitext(os.path.basename(file_name))[0].upper()
		for line in file:

			# Some lines are tagged with author name and line number. This removes these tags.
			# e.g. "These vessels are of five kinds.  ADAMS-1787-2,653.17"
			# becomes "These vessels are of five kinds.  "
			line = re.sub(text_name + '.*', '', line)

			file_text.write(line.strip())
			file_text.write(' ')
	return file_text.getvalue()

def feature_extraction(corpus_path, output, features):
	'''Perform a feature extraction'''
	download_corpus(corpus_path)
	qcrit.extract_features.main(
		corpus_dir=os.path.join(*corpus_path),
		file_extension_to_parse_function={
			'txt': parse_txt,
		},
		output_file=output,
		features=features,
	)

def main():
	'''Main'''
	cp_specifier = 'corpus-path'
	corpus_path = None
	f_specifier = 'features'
	features = []
	dump_specifier = 'dump'
	dump = False

	opts, _ = getopt.getopt(sys.argv[1:], shortopts='', longopts=(
		f'{cp_specifier}=',
		f'{f_specifier}=',
		f'{dump_specifier}',
	))
	for opt, val in opts:
		if opt == f'--{cp_specifier}':
			corpus_path = val
		if opt == f'--{f_specifier}':
			features.append(val)
		if opt == f'--{dump_specifier}':
			dump = True
	if not corpus_path:
		msg = f'Arguments are missing a required option: "--{cp_specifier}=<some path>"'
		raise getopt.GetoptError(msg)

	corpus_path = corpus_path.split(os.sep)
	feature_extraction(
		corpus_path,
		f'{corpus_path[-1].lower()}.pickle' if dump else None,
		features if features else None,
	)

if __name__ == '__main__':
	main()