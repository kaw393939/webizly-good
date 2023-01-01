#!/usr/bin/env bash
flask db upgrade
gunicorn --bind 0.0.0.0:$PORT "application:init_app()"