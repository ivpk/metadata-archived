env/done: env/bin/pip requirements.txt requirements-dev.txt
	env/bin/pip install -r requirements-dev.txt
	touch env/done

env/bin/pip:
	virtualenv -p python3.4 env

env/bin/pip-compile: env/bin/pip
	env/bin/pip install pip-tools

requirements.txt: env/bin/pip-compile requirements.in
	env/bin/pip-compile --no-index -o requirements.txt requirements.in

requirements-dev.txt: env/bin/pip-compile requirements.in requirements-dev.in
	env/bin/pip-compile --no-index -o requirements-dev.txt requirements.in requirements-dev.in


.PHONY: run
run:
	env/bin/python manage.py runserver

.PHONY: migrate
migrate:
	env/bin/python manage.py migrate


.PHONY: build
build: env/done
	node_modules/webpack/bin/webpack.js --config ./webpack.config.js --mode production
