# Final Project - CS 221 Artificial Intelligence: Principles and Techniques

## Authors
Andy Kim

David Whisler

[Tim Gianitsos](https://github.com/timgianitsos)

## Development (for Mac and Linux)

1. Ensure `Python` version 3.8 is installed.
1. Ensure `pipenv` is installed
1. (Optional) Set an environment variable <sup id="a1">[1](#f1)</sup> by executing the following lines.
	If your system uses `~/.bash_profile` (Mac for example), then run the commands with `~/.bash_profile`. If your system uses `~/.bashrc`(Linux for example), then replace `~/.bash_profile` with `~/.bashrc` in the below commands.
	```bash
	echo "#When pipenv makes a virtual environment, it will create it in the same directory as the project instead of in the home directory" >> ~/.bash_profile
	echo "PIPENV_VENV_IN_PROJECT=true" >> ~/.bash_profile
	echo "export PIPENV_VENV_IN_PROJECT" >> ~/.bash_profile
	```
	Close terminal, then repoen terminal for the environment variable to take effect.
1. While in the project directory, run
	```bash
	pipenv --python 3.8
	```
	If `PIPENV_VENV_IN_PROJECT=true`, then this will generate a virtual environment called `.venv` in the current directory that will contain the `Python` dependencies for this project. If `PIPENV_VENV_IN_PROJECT` was not set, it will be placed in the home directory.
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

## Notes

<b id="f1">1</b> The `pipenv` tool works by making project-specific directories (called virtual environments) that hold the dependencies for that project. Setting the `PIPENV_VENV_IN_PROJECT` environment variable will indicate to `pipenv` to make this virtual environment within the same directory as the project so that all the files corresponding to a project can be in the same place. This is [not default behavior](https://github.com/pypa/pipenv/issues/1382) (e.g. on Mac, the environments will be placed in `~/.local/share/virtualenv/`). [↩](#a1)


