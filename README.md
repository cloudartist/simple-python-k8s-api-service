# Python deployment template for k8s

Best way to quickly get going is by using [Makefile](Makefile).

## Build 

```
docker build -f Dockerfile -t hello-api:latest .
```

## Run
```
python app/api.py
# or
docker run -p 5000:5000 hello-api:latest 
```

## Tests
Runing unit tests
```
python -m pytest tests
```

## Management

Generate requirements.txt
```
pipenv lock --keep-outdated --requirements > requirements.txt
```