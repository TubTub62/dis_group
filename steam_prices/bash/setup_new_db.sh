#!/bin/bash

clear
psql --dbname=steam_db --username=postgres -f ../sql/create_new_db.sql