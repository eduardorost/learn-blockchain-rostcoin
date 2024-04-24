
# Run with poetry

poetry install

BLOCKCHAIN_RECEIVER=Eduardo poetry run python main.py

# Run with docker
docker-compose up


# HTTP requests

-- ADD NODES

curl --location 'http://localhost:5001/node' \
--header 'Content-Type: application/json' \
--data '{
    "nodes": [
        "http://app2:5000",
        "http://app3:5000"
    ]
}'

curl --location 'http://localhost:5002/node' \
--header 'Content-Type: application/json' \
--data '{
    "nodes": [
        "http://app1:5000",
        "http://app3:5000"
    ]
}'

curl --location 'http://localhost:5003/node' \
--header 'Content-Type: application/json' \
--data '{
    "nodes": [
        "http://app1:5000",
        "http://app2:5000"
    ]
}'


-- MINE BLOCK

curl --location 'http://localhost:5001/mine-block'

-- GET CHAIN

curl --location 'http://localhost:5001/chain'
curl --location 'http://localhost:5002/chain'
curl --location 'http://localhost:5003/chain'

-- REPLACE CHAIN

curl --location 'http://localhost:5002/chain/replace'
curl --location 'http://localhost:5003/chain/replace'

-- ADD TRANSACTION

curl --location 'http://localhost:5001/transaction' \
--header 'Content-Type: application/json' \
--data '{
    "sender": "Eduardo",
    "receiver": "Pedro",
    "amount": 1000
}'

curl --location 'http://localhost:5001/mine-block'

-- REPLACE CHAIN

curl --location 'http://localhost:5002/chain/replace'
curl --location 'http://localhost:5003/chain/replace'
