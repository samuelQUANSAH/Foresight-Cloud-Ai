install:
	pip install -r requirements.txt

demo:
	python -m src.demo

api:
	uvicorn src.api.main:app --reload

test:
	PYTHONPATH=. pytest -q
