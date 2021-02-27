
all: build run
	

build:
	docker build . -t vernacular-image:latest 

run:
	docker-compose up

