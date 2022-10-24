# ft_blockchain

## Description

This project is a blockchain implementation in python3 It is a simple implementation of a blockchain, with a proof of work algorithm, and a simple consensus algorithm (the longest chain wins)
rest api is implemented using flask

## Installation

```bash
git clone git@github.com:dugonzal/ft_blockchain.git

cd ft_blockchain

virtualenv -p python3 venv

. venv/bin/activate  or source venv/bin/activate

pip3 install -r requirements.txt
```

## Usage

```bash
python3 ft_blockchain.py
```
## routes

```

GET /chain

--- Returns the full blockchain

GET /mine

--- Mine a new block

POST /transactions/new
-- Add a new transaction to the list of transactions
```

## Author

* **Duvan González** - *Initial work* - [dugonzal]

