#!/bin/bash

export PGPASSWORD='UIS'

cd bank
psql -dbank24017 --username=postgres --host=database -W -f schema.sql
psql -dbank24017 --username=postgres --host=database -W -f schema_ins.sql
psql -dbank24017 --username=postgres --host=database -W -f schema_upd.sql
cd ..

flask --app bank run --host=0.0.0.0 --debug
