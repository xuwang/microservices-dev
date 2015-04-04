# A Docker For Python Web Applications

## Build
	./build.sh
## Run
	docker run -d --name my_app -p 8080:80 xuwang/pyweb
## Run external app with pip install
	docker run -d --name my_app -p 8080:80 -v <my_app_dir>:/application -e PIP=true xuwang/pyweb
##Example python application folder structure:
```
docker/application
    |
    |- requirements.txt  # File containing list of dependencies
    |- /app              # Application module
    |- app.py            # WSGI file containing the "app" callable
    |- server.py         # Optional: To run the app servers (CherryPy)
    |- server.sh         # Optional: To run the app servers (Gunicorn)
```