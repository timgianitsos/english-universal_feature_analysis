# A Diachronic approach to English

## Authors

[Andy Kim](https://github.com/andydhkim)

[David Whisler](https://github.com/dwhisler)

[Tim Gianitsos](https://github.com/timgianitsos)

## Setup (for Mac and Linux)

1. Ensure `Python` version 3.8 is installed.
1. Ensure `pipenv` is installed
1. Ensure you have `git` at least version 1.9 installed<sup id="a1">[1](#f1)</sup>
1. While in the project directory, run
	```bash
	PIPENV_VENV_IN_PROJECT=true pipenv --python 3.8
	```
	This will generate a virtual environment called `.venv` in the current directory that will contain the `Python` dependencies for this project.<sup id="a2">[2](#f2)</sup>
1. Run 
	```bash
	pipenv shell
	```
	This will activate the virtual environment. Now, running `Python` commands will ignore the system-level `Python` version & packages, and only use the packages from the virtual environment.
1. Run
	```bash
	pipenv install --dev
	```
	This will install all the packages with versions specified by `Pipfile.lock`. Using `--dev` ensures that even development dependencies should be installed (dev dependencies may include testing and linting frameworks which are not necessary for production). After installation, you can find these dependencies in `<path to virtual environment>/lib/python3.8/site-packages/`.
1. Run
	```bash
	exit
	```
	in order to leave the virtual environment. This will restore the system-level `Python` configurations to your shell.
1. Run
	```bash
	pipenv shell
	```
	while in the project directory to activate the virtual environment again. This will make `Python` use the configurations in the project's virtual environment.

## Development

You will find the features for Modern English in `modern_english_features.py`.

You can run a feature extraction by running
```
python run_modern_eng_feat_extract.py 
```
You can output the results of the extraction for further analysis into a pickle file by running
```
python run_modern_eng_feat_extract.py modern_english.pickle
```

## Notes

<b id="f1">1)</b> The project uses the `git` protocol to download the corpus. We make use of `git`'s sparse checkout and shallow clone features to download only what we need from the repository (this is done automatically in the code). We must have [at least `git` version 1.9 to perform a sparse checkout and shallow clone](https://stackoverflow.com/a/28039894/7102572).[↩](#a1)

<b id="f2">2)</b> The `pipenv` tool works by making project-specific directories (called virtual environments) that hold the dependencies for that project. Setting the `PIPENV_VENV_IN_PROJECT` environment variable will indicate to `pipenv` to make this virtual environment within the same directory as the project so that all the files corresponding to a project can be in the same place. This is [not default behavior](https://github.com/pypa/pipenv/issues/1382) (e.g. on Mac, the environments will normally be placed in `~/.local/share/virtualenvs/` by default). [↩](#a2)
