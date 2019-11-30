'''
Generate the csv of prosody labels for files
'''
import os
from os.path import join, dirname

def main():
	verse_dir = ('english-diachronic-corpus', 'Early-Modern-English', 'Verse-corpus')
	prose_dir = ('english-diachronic-corpus', 'Early-Modern-English', 'Plaintext-prose-corpus')
	with open(join(dirname(__file__), '..', 'labels', 'early_modern_english_prosody.csv'), mode='w') as f:
		f.write('verse:0,prose:1\n')
		f.write('Filename,Label\n')
		corpus = join(dirname(__file__), '..', *verse_dir)
		for filename in os.listdir(corpus):
			if filename.endswith('txt'):
				f.write(f'{"/".join(verse_dir)}/{filename},0\n')
		corpus = join(dirname(__file__), '..', *prose_dir)
		for filename in os.listdir(corpus):
			if filename.endswith('txt'):
				f.write(f'{"/".join(prose_dir)}/{filename},1\n')
	print('Success!')

if __name__ == '__main__':
	main()
