#!/bin/bash

clear

echo RUNNING schema.sql
psql --dbname=steam_db --username=postgres -f sql/schema.sql
clear

echo POPULATING DB
python steamStats/populate_db.py
clear

echo STARTING WEBSITE
flask --app steamStats run --host=0.0.0.0 --debug
