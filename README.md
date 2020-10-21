# sphinx-model
## Description
This repository is for the Sphinx machine learning model development, as well as the `Flask` backend server deployment.

## Included:
- [ ] `service.yml` file that includes the tools, services, commands, etc
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
$ python app.py
```

## Testing
Run the `Flask` test with the command:
```
$ pytest -v
```
