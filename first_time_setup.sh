#!/bin/bash

python3 -m venv venv # or just python for some
source venv/bin/activate # venv/script/activate for windows(might need to be capital S in Script)

cd steam_prices
pip install -r requirements.txt

cd bash

bash create_new_db_server.sh
bash run.sh