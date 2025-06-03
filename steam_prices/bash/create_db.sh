#!/bin/bash

clear
psql --dbname=steam_db --username=postgres -f ../sql/schema.sql