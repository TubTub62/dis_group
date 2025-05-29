#!/bin/bash

clear
psql --dbname=steam_db --username=postgres -f sql/schema.sql

flask --app steamStats run --host=0.0.0.0 --debug
