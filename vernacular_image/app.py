#!/usr/bin/env python

from flask import Flask, jsonify, send_from_directory
import rq_dashboard
import os
import json

from redis import Redis
from rq import Queue

from vernacular_image import settings
from vernacular_image.workers import ImageProcessor


with open('/vernacular_image/config.json') as f:
    data = json.load(f)
    image_config = dict((i["id"],i) for i in data)


jobQueueRedis = Redis(host='redis', port=6379, db=0)
dataRedis = Redis(host='redis', port=6379, db=1)
queue = Queue(connection=jobQueueRedis)
app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://redis:6379/0'
app.config.from_object(settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

@app.route('/media1/<path:path>')
def static_file(path):
    print(">>")
    print(path)
    return app.send_static_file(path)

@app.route("/banner/<int:movie>/<string:language>")
def banner(movie, language):
    key = "idx:{}:{}".format(movie, language)
    bannerFile = dataRedis.get(key)
    if bannerFile:
        return jsonify({
            "bannerFile":bannerFile.decode("utf-8")
        })

    job = queue.enqueue(
        ImageProcessor.create_banner,
        image_config[movie],
        language, result_ttl=86400)
    return jsonify({
        "jobId":job.id
    })




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
