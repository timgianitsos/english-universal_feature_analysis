'''
Run model analyzer
'''
import sys

import qcrit.analyze_models
from qcrit.model_analyzer import DECORATED_ANALYZERS

import analyzers

def main():
	'''Main'''
	qcrit.analyze_models.main(
		sys.argv[1] if len(sys.argv) > 1 else input('Enter filename to extract feature data: '),
		sys.argv[2] if len(sys.argv) > 2 else input('Enter filename to extract classification data: '),
		None if len(sys.argv) > 3 and sys.argv[3] == 'all' else
		sys.argv[3:] if len(sys.argv) > 3 else input(
			'What would you like to do?\n' +
			'\n'.join('\t' + name for name in DECORATED_ANALYZERS) + '\n'
		).split()
	)

if __name__ == '__main__':
	main()
