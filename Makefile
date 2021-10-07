BASE := $(shell /bin/pwd)

test: 
	python -m pytest tests

build: 
	docker build -f Dockerfile -t hello-api:latest .