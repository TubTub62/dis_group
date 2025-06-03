#!/bin/bash

clear

echo RESETING DB
bash create_db.sh
clear

echo POPULATING DB
bash populate_db.sh
clear

echo STARTING WEBSITE
flask --app ../steamStats run --host=0.0.0.0 --debug
