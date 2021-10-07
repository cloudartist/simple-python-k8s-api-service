BASE := $(shell /bin/pwd)

run:
	python3.8 app/api.py

test: 
	python3.8 -m pytest tests

build: 
	docker build -f Dockerfile -t hello-api:latest .
