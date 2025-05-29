#!/bin/bash

python3 -m venv venv # or just python for some
source venv/bin/activate # venv/script/activate for some (might need to be capital S in Script)

cd steam_prices
pip install -r requirements.txt

cd bash

bash setup_new_db.sh
bash db.sh

cd ..

bash run.sh