reset_schema:
	poetry run python scripts/reset_schema.py

lines:
	poetry run python scripts/lines.py

dev:
	cd ..
	docker compose up api-dev

build:
	docker build -t antoniofernandodj/chickie:${v} -f ./dockerfiles/Dockerfile.prod .
	docker push antoniofernandodj/chickie:${v}

ct:
	poetry run mypy --check-untyped-defs asgi.py

uic:
	poetry run pyside6-uic src/qt/views/main.ui -o src/qt/views/main_ui.py
	poetry run pyside6-uic src/qt/views/loginForm.ui -o src/qt/views/loginForm_ui.py

qt:
	poetry run python qt.py

test:
	poetry run python -m pytest . -vv

celeryWorker:
	poetry run celery -A scheduler worker --loglevel=info

celeryBeat:
	poetry run celery -A scheduler beat --loglevel=info

celeryScheduler:
	poetry run celery -A scheduler beat --loglevel=info
