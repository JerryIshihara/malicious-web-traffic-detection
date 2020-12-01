# Malicious Web Traffic Detection Model

## Description

This repository is for the Sphinx machine learning model development, as well as the `Flask` backend server deployment.

## Dataset:

CIRA-CIC-DoHBrw-2020 Dataset ([link](https://www.unb.ca/cic/datasets/dohbrw-2020.html))

CREDIT:
> Mohammadreza MontazeriShatoori, Logan Davidson, Gurdip Kaur, and Arash Habibi Lashkari, “Detection of DoH Tunnels using Time-series Classification of Encrypted Traffic”, The 5th IEEE Cyber Science and Technology Congress, Calgary, Canada, August 2020

## Models:

- Baseline: Catboost model, achieve F-score 0.99789
- PCA: A PCA process that projects the data into 3D

## Included:

- [x] Flask routes for prediction and clustering
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

The server will start locally on `PORT:5000`. You may change the default port in `.env` file.

```
$ python3 app.py
```

## Testing & Debug

Run the `Flask` test with the command:

```
$ python3 -m pytest -v
```

Change the `DEBUG` variable in `.env` file to run in debug mode
