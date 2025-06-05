#!/bin/bash

python3 -m venv venv
source venv/bin/activate

cd steam_prices
pip install -r requirements.txt

cd bash

bash create_new_db_server.sh
bash run.sh