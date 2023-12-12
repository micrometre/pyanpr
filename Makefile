.PHONY: run
claean: 
	sudo rm -rf static/images/*.jpg
start_flak:
	flask run --host=0.0.0.0 --debug	
alprd_start:
	docker-compose -f openalpr-docker/docker-compose.yml up -d
alprd_stop:
	docker-compose -f openalpr-docker/docker-compose.yml down
update:
	docker-compose -f openalpr-docker/docker-compose.yml down
	docker-compose -f openalpr-docker/docker-compose.yml pull
	docker-compose -f openalpr-docker/docker-compose.yml -d --build
restart:	
	docker-compose -f openalpr-docker/docker-compose.yml restart
remove:	
	docker-compose -f openalpr-docker/docker-compose.yml down -v
	docker-compose -f openalpr-docker/docker-compose.yml down rm -rf