FROM python:3.10.0a5-alpine3.13
ENV MAGICK_HOME=/usr
RUN apk add --no-cache imagemagick && apk add --no-cache imagemagick-dev
ADD vernacular_image vernacular_image
RUN pip install -r /vernacular_image/requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/vernacular_image"
RUN chmod +x /vernacular_image/start.sh

EXPOSE 8080:8080
EXPOSE 5000:5000

CMD ["python", "app.py"]
