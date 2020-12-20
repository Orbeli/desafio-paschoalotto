install:
	python3 -m venv .venv
	venv/bin/pip install -r requirements.txt
	export FLASK_APP="phone:create_app()"
	venv/bin/flask db upgrade

run:
	export FLASK_APP="phone:create_app()"
	venv/bin/flask run