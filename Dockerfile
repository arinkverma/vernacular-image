FROM python:3.10.0a5-alpine3.13

RUN pip install rq==1.7.0
RUN pip install flask==1.1.2
RUN pip install rq_dashboard==0.6.1
RUN pip install Flask-RQ2==18.3

ADD vernacular_image vernacular_image
#WORKDIR /vernacular_image
ENV PYTHONPATH "${PYTHONPATH}:/vernacular_image"
RUN chmod +x /vernacular_image/start.sh

EXPOSE 8080:8080
EXPOSE 5000:5000

CMD ["python", "app.py"]