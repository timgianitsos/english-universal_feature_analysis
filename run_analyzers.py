'''
Run model analyzer
'''
import sys

import qcrit.analyze_models
from qcrit.model_analyzer import DECORATED_ANALYZERS

def main():
	'''Main'''
	if len(sys.argv) <= 1 or sys.argv[1] not in ('-s', '-d'):
		print(
			'Please specify either (-s)ynchronic_analyzers or (-d)iachronic_analyzers on the command line',
			file=sys.stderr
		)
		return
	if sys.argv[1] == '-s':
		import synchronic_analyzers # pylint: disable = unused-import, import-outside-toplevel
	if sys.argv[1] == '-d':
		import diachronic_analyzers # pylint: disable = unused-import, import-outside-toplevel
	qcrit.analyze_models.main(
		sys.argv[2] if len(sys.argv) > 2 else input('Enter filename to extract feature data: '),
		sys.argv[3] if len(sys.argv) > 3 else input('Enter filename to extract classification data: '),
		None if len(sys.argv) > 4 and sys.argv[4] == 'all' else
		sys.argv[4:] if len(sys.argv) > 4 else input(
			'What would you like to do?\n' +
			'\n'.join('\t' + name for name in DECORATED_ANALYZERS) + '\n'
		).split()
	)

if __name__ == '__main__':
	main()
