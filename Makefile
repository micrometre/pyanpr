.PHONY: run
claen_alprd: 
	sudo rm -rf flask-api/static/images/*.jpg
flask_start:
	flask run --host=0.0.0.0 --debug	
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
install_depen:
	sudo apt-get install python3-opencv  inotify-tools -y	
