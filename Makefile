.PHONY: run
claen: 
	sudo rm -rf static/images/*.jpg
flask_start:
	flask run --host=0.0.0.0 --debug	
alprd_start:
	docker-compose -f openalpr-docker/docker-compose.yml up -d
alprd_stop:
	docker-compose -f openalpr-docker/docker-compose.yml down
alprd_update:
	docker-compose -f openalpr-docker/docker-compose.yml down
	docker-compose -f openalpr-docker/docker-compose.yml pull
	docker-compose -f openalpr-docker/docker-compose.yml up -d --build
alprd_restart:	
	docker-compose -f openalpr-docker/docker-compose.yml restart
alprd_remove:	
	docker-compose -f openalpr-docker/docker-compose.yml down -v
	docker-compose -f openalpr-docker/docker-compose.yml down rm -rf
start:
	docker-compose up -d 

stop:
	docker-compose down 

update:
	docker-compose down 
	docker-compose pull
	docker-compose up -d --build

restart:
	docker-compose restart

remove:
	docker-compose down -v
	docker-compose rm -f
