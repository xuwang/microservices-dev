#!/usr/bin/env bash

# If $PIP is set, download and install requirements:
if [ -n "$PIP" ]; then
	pip install --upgrade -r /application/requirements.txt
fi

# Try run server
if [ -f "server.sh" ]; then
	bash server.sh
	exit
fi

# Try run server
if [ -f "server.py" ]; then
	python server.py
	exit
fi

# Try run app directly	
if [ -f "server.py" ]; then
	python app.py
	exit
fi

bash