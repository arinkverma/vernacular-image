#!/usr/bin/env python

from flask import Flask
import rq_dashboard
import os

from redis import Redis
from rq import Queue

from vernacular_image import settings
from vernacular_image.workers import ImageProcessor


queue = Queue(connection=Redis(host='redis', port=6379, db=0))
app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://redis:6379/0'
app.config.from_object(settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

@app.route("/")
def hello():
    job = queue.enqueue(ImageProcessor.create_banner, 1,2, result_ttl=86400)
    print(job)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
