#!/bin/sh

if [ $1 == "worker" ]; then
  echo "Starting workers"
  rq worker --with-scheduler --url redis://redis:6379/0
fi

if [ $1 == "server" ]; then
  echo "Starting server"
  python /vernacular_image/app.py
fi