# sphinx-model

![Test](https://github.com/JerryIshihara/user-behaviour-analysis-model/workflows/CI/badge.svg?branch=main)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

## Description

This repository is for the Sphinx machine learning model development, as well as the `Flask` backend server deployment.

## Included:

- [x] `service.yml` file that includes the tools, services, commands, etc
- [x] `script/bootstrap` for repo set-up
- [x] Github Actions for continuous integration
- [x] Test infrastructure

## Set-up:

- Clone the repository to your local folder.
- Navigate to the repo directory.
- Run the bootstrap file to setup everything.

```
$ script/bootstrap
```

## Start the server locally

The server will start locally on `PORT:5000`

```
$ python3 app.py
```

## Testing

Run the `Flask` test with the command:

```
$ python3 -m pytest -v
```
