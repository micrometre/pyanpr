.PHONY: run
start_dev:
	flask run --host=0.0.0.0 --debug
start_sse:
	gunicorn --bind 0.0.0.0:5000 wsgi:app	
