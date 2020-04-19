# Serveur / Client lourd
> The purpose of this project is to ...

## Install (dev)
### Create the conda environement
 * `conda create --name PApy-3.7 python=3.7`
 * `conda activate PApy-3.7`
 * `pip install pipenv`
###  Create the virtual environement using pipenv, or update dependencies 
 * `pipenv install --skip-lock --dev` run this command in the project folder
### Install a new package
 * `pipenv install <packagename> --skip-lock`
### Launch the application
 * `TODO`


## Install prod 
> TODO 

## Tests
### Tests can be launched through pytest with pytest
* `pipenv run python -m pytest test/`
### Test coverage code analysis can be launch with pytest
* `pipenv run python -m pytest --cov-report term:skip-covered --cov=main/src test/`
* `pipenv run python -m pytest --cov-report term-missing:skip-covered --cov=main/src test/`
### Dead code analysis can be launch with vulture
* `pipenv run python -m vulture main/`