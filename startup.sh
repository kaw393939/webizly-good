#!/usr/bin/env bash
flask db upgrade;
if [ $DEPLOYMENT == "production" ]
then
  gunicorn --bind 0.0.0.0:$PORT "application:init_app()"
else
  flask --debug run --host=0.0.0.0 --port=$PORT
fi