pip install -r requirements_dev.txt


pycodestyle *.py
pylint *.py
isort *.py
coverage run -m unittest test*.py
coverage report
