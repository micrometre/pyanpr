.PHONY: run
claean: 
	sudo rm -rf public/images/*.jpg
start:
	flask run --host=0.0.0.0 --debug	