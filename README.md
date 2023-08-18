# Point Distance Calculator

```
Input Points:
Point 0: Latitude -19.0294, Longitude -174.4928
Point 1: Latitude -42.695, Longitude -34.2935
Point 2: Latitude -63.0232, Longitude -36.074
Point 3: Latitude -6.9889, Longitude 22.7052
Point 4: Latitude -49.0345, Longitude 88.5772

Pairwise Distances (in km):
Point 0 to Point 1: 12033.8
Point 0 to Point 2: 10200.0
Point 0 to Point 3: 16562.3
Point 0 to Point 4: 8910.0
Point 1 to Point 2: 2263.3
Point 1 to Point 3: 6819.0
Point 1 to Point 4: 8394.4
Point 2 to Point 3: 7785.0
Point 2 to Point 4: 6643.4
Point 3 to Point 4: 7675.8
```

## pre-requirements

- [poetry](https://python-poetry.org/)
- Python 3.11.4 (see [.python-version](./.python-version))

## setup

```shell
poetry install
```

## test

```shell
poetry run pytest
```

## execute

```shell
poetry run main
```

## references

- used [template](https://github.com/armand-sauzay/python-template) from Medium
  article [Python Project Setup: A Step-by-Step Guide to Industry Best Practices](https://armand-sauzay.medium.com/python-project-setup-a-step-by-step-guide-to-industry-best-practices-dbce717b2d12)
