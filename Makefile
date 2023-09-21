install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check .

refactor: format lint

		
all: install lint test format
