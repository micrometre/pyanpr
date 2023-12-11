.PHONY: run
claean: 
	sudo rm -rf statc/images/*.jpg
start:
	flask run --host=0.0.0.0 --debug	