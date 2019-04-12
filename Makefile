install-dev:
	pipenv install --dev

format:
	pipenv run black .

lint:
	pipenv run flake8 --ignore=F401 texlivemetadata
	pipenv run pylint texlivemetadata

release:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel --universal
	pipenv run twine check dist/*
	pipenv run twine upload dist/*
