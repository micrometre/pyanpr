.PHONY: run
claen_alprd: 
	sudo rm -rf static/images/*.jpg
claen_alpr_images: 
	rm -rf alpr-images/*.jpg
run_alpr:
	alpr -c gb  -n 1 public/images | sed 's|public|"http://localhost|g;s|plate0|{|g;s/.$/"]/;/: 1 result/d;s/^\s*./["/g; s/confidence:/","/g   '
ffmpeg_images:
	ffmpeg -i static/upload/alprVideo.mp4 -r 29/1 ffmpeg-images/out%03d.jpg	
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
