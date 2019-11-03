# pylint: disable = C0330
'''
Utilities to download a corpus
'''

import os
import sys
import subprocess

def download_corpus(corpus_path, repo_user='timgianitsos'):
	'''
	Download a corpus from Github with a sparse checkout and shallow clone.
	https://stackoverflow.com/a/28039894/7102572

	If the directory specified by corpus_path already exists, no action will be taken.
	'''

	# Locally create a directory to hold the corpus, and prepare it for cloning the repo
	if not os.path.isdir(corpus_path[0]):
		try:
			cmd_list = [
				f'mkdir {corpus_path[0]}',
				f'git -C {corpus_path[0]} init',
				f'git -C {corpus_path[0]} remote add origin ' +
					f'https://github.com/{repo_user}/{corpus_path[0]}.git',

				# If the corpus path only has one element (the name of the repo), then the user wants
				# to clone the whole repo. If there are multiple elements, the user wants to import only
				# a subdirectory, so we prepare for a sparse checkout
				(
					f'git -C {corpus_path[0]} pull --depth=1 origin master'
					if len(corpus_path) == 1 else
					f'git -C {corpus_path[0]} config core.sparseCheckout true'
				),
			]
			cmd_str = ' && '.join(cmd_list)
			proc = subprocess.run(cmd_str, check=True, shell=True)
		except OSError as ex:
			raise ex
		except subprocess.CalledProcessError as ex:
			prgrm_names = {s.split(maxsplit=1)[0] for s in cmd_list}
			print(f'Your system could not run one of the following commands: {prgrm_names}', file=sys.stderr)
			raise ex

	# Perform a sparse checkout
	# If the corpus path has only one element, the whole directory will have already been cloned just
	# previously and this block won't execute a sparse checkout
	if not os.path.isdir(os.path.join(*corpus_path)):
		try:
			cmd_list = (
				f'echo "{os.path.join(*(corpus_path[1:]))}{os.sep}*"'
					+ f' >> {corpus_path[0]}/.git/info/sparse-checkout',
				f'git -C {corpus_path[0]} fetch --depth=1',
				f'git -C {corpus_path[0]} checkout master',
			)
			cmd_str = ' && '.join(cmd_list)
			proc = subprocess.run(cmd_str, check=True, shell=True)
		except OSError as ex:
			raise ex
		except subprocess.CalledProcessError as ex:
			prgrm_names = {s.split(maxsplit=1)[0] for s in cmd_list}
			print(f'Your system could not run one of the following commands: {prgrm_names}', file=sys.stderr)
			raise ex
