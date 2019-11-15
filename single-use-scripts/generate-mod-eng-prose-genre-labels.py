'''
Generate the csv of genre labels for files
'''
import os
from os.path import join, dirname
import csv

def main():
	verse_dir = ('english-diachronic-corpus', 'Modern_English', 'Verse_Corpus')
	prose_dir = ('english-diachronic-corpus', 'Modern_English', 'Plaintext_prose_corpus')
	prose_genre_label_file = (
		'english-diachronic-corpus', 'Modern_English', 'MdE_prose_metadata.csv',
	)

	'''
	There are many categories with only a few texts within each. We will merge categories that are similar.
	Original category counts:
	Counter({
		'EDUC_TREATISE': 24,'LETTERS_PRIV': 22,'HISTORY': 21,'TRAVELOGUE': 21,'FICTION': 21,
		'DRAMA_COMEDY': 21,'DIARY_PRIV': 21,'HANDBOOK_OTHER': 21,'SERMON': 19,'SCIENCE_OTHER': 15,
		'PROCEEDINGS_TRIAL': 10,'BIOGRAPHY_AUTO': 10,'BIBLE': 10,'LETTERS_NON-PRIV': 10,
		'BIOGRAPHY_OTHER': 9,'SCIENCE_MEDICINE': 9,'LAW': 7,'PHILOSOPHY': 4,
	})
	MERGE: BIBLE, SERMON -> religious
	MERGE: SCIENCE_OTHER, SCIENCE_MEDICINE -> science
	MERGE: PROCEEDINGS_TRIAL, LAW -> law
	MERGE: BIOGRAPHY_AUTO, BIOGRAPHY_OTHER -> biography
	MERGE: LETTERS_PRIV, LETTERS_NON-PRIV -> letters
	MERGE: HANDBOOK_OTHER, EDUC_TREATISE -> educ_treatise
	MERGE: PHILOSOPHY, RELIGIOUS -> religious
	Merged category counts:
	Counter({
		'educ_treatise': 45,'history': 21,'travelogue': 21,'fiction': 21,'drama_comedy': 21,
		'diary_priv': 21,'science': 24,'biography': 19,'religious': 33,'letters': 32,'law': 17,
	})
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
	merge_label_to_value = {
		'educ_treatise': 1, 'history': 2, 'travelogue': 3, 'fiction': 4, 'drama_comedy': 5,
		'diary_priv': 6, 'science': 7, 'biography': 8, 'religious': 9, 'letters': 10, 'law':11,
	}
	with open(join(dirname(__file__), '..', 'labels', 'modern_english_prose_genre.csv'), mode='w') as label_f:
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
				f'{"/".join(prose_dir)}/{row[0]}.txt,'
				f'{merge_label_to_value[found_label_to_merge_label[row[2]]]}\n'
			)
	print('Success!')

if __name__ == '__main__':
	main()
