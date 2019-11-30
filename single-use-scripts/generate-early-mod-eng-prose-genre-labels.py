'''
Generate the csv of genre labels for files
'''
import os
from os.path import join, dirname
import csv

def main():
	'''main'''
	verse_dir = ('english-diachronic-corpus', 'Early-Modern-English', 'Verse-corpus')
	prose_dir = ('english-diachronic-corpus', 'Early-Modern-English', 'Plaintext-prose-corpus')
	prose_genre_label_file = (
		'english-diachronic-corpus', 'Early-Modern-English', 'EME_metadata.csv',
	)

	'''
	There are many categories with only a few texts within each. We will merge categories that are similar.
	Original category counts:
	>>> import csv; from collections import Counter
	>>> gen = (row[1] for row in csv.reader(
	...     open('english-diachronic-corpus/Early-Modern-English/EME_metadata.csv', mode='r')
	... ))
	>>> next(gen) #remove first line
	>>> Counter(gen)
	Counter({
		'LETTERS_PRIV': 129, 'LETTERS_NON-PRIV': 71, 'SERMON': 22, 'DIARY_PRIV': 21,
		'EDUC_TREATISE': 20, 'LAW': 20, 'TRAVELOGUE': 19, 'HANDBOOK_OTHER': 19,
		'FICTION': 18, 'HISTORY': 18, 'DRAMA_COMEDY': 18, 'PROCEEDINGS_TRIAL': 16,
		'SCIENCE_OTHER': 13, 'BIBLE': 12, 'PHILOSOPHY': 9, 'BIOGRAPHY_OTHER': 9,
		'SCIENCE_MEDICINE': 7, 'BIOGRAPHY_AUTO': 7,
	})

	MERGE: BIBLE, SERMON -> religious
	MERGE: SCIENCE_OTHER, SCIENCE_MEDICINE -> science
	MERGE: PROCEEDINGS_TRIAL, LAW -> law
	MERGE: BIOGRAPHY_AUTO, BIOGRAPHY_OTHER -> biography
	MERGE: LETTERS_PRIV, LETTERS_NON-PRIV -> letters
	MERGE: HANDBOOK_OTHER, EDUC_TREATISE -> educ_treatise
	MERGE: PHILOSOPHY, RELIGIOUS -> religious
	'''
	found_label_to_merge_label = {
		'BIBLE': 'religious',
		'SERMON': 'religious',
		'SCIENCE_OTHER': 'science',
		'SCIENCE_MEDICINE': 'science',
		'PROCEEDINGS_TRIAL': 'law',
		'LAW': 'law',
		'BIOGRAPHY_AUTO': 'biography',
		'BIOGRAPHY_OTHER': 'biography',
		'LETTERS_PRIV': 'letters',
		'LETTERS_NON-PRIV': 'letters',
		'HANDBOOK_OTHER': 'educ_treatise',
		'EDUC_TREATISE': 'educ_treatise',
		'PHILOSOPHY': 'religious',
		'HISTORY': 'history',
		'TRAVELOGUE': 'travelogue',
		'FICTION': 'fiction',
		'DRAMA_COMEDY': 'drama_comedy',
		'DIARY_PRIV': 'diary_priv',
	}
	'''
	Merged category counts:
	>>> read = csv.reader(open('english-diachronic-corpus/Early-Modern-English/EME_metadata.csv', mode='r'))
	>>> next(read)
	>>> Counter(found_label_to_merge_label[row[1]] for row in read)
	Counter({
		'letters': 200, 'religious': 43, 'educ_treatise': 39, 'law': 36, 'diary_priv': 21,
		'science': 20, 'travelogue': 19, 'fiction': 18, 'history': 18, 'drama_comedy': 18, 'biography': 16
	})
	'''
	merge_label_to_value = {
		'educ_treatise': 1, 'history': 2, 'travelogue': 3, 'fiction': 4, 'drama_comedy': 5,
		'diary_priv': 6, 'science': 7, 'biography': 8, 'religious': 9, 'letters': 10, 'law':11,
	}
	with open(join(dirname(__file__), '..', 'labels', 'early_modern_english_prose_genre.csv'), mode='w') as label_f:
		label_f.write(
			f'verse:0,{",".join(f"{k}:{str(v)}" for k, v in merge_label_to_value.items())}\n'
		)
		label_f.write('Filename,Label\n')
		for filename in os.listdir(join(dirname(__file__), '..', *verse_dir)):
			if filename.endswith('txt'):
				label_f.write(f'{"/".join(verse_dir)}/{filename},0\n')
		csv_reader = csv.reader(open(join(dirname(__file__), '..', *prose_genre_label_file), mode='r'))
		next(csv_reader)
		for row in csv_reader:
			label_f.write(
				f'{"/".join(prose_dir)}/{row[3]}.txt,'
				f'{merge_label_to_value[found_label_to_merge_label[row[1]]]}\n'
			)
	print('Success!')

if __name__ == '__main__':
	main()
