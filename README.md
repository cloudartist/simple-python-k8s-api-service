# Python deployment template for k8s

Best way to quikcly get going is by using [Makefile](Makefile).

## Build 

```
docker build -f Dockerfile -t hello-api:latest .
```

## Tests
Runing unit tests
```
python -m pytest tests
```

## Admin

Generate requirements.txt
```
pipenv lock --keep-outdated --requirements > requirements.txt
```