client1:
	cd frontend-angular && ng serve

api:
	docker compose down
	docker build \
		-t antoniofernandodj/chickie:dev \
		-f ./backend/dockerfiles/api.dockerfile \
		backend
	docker compose up api-dev -d && docker logs api-dev -f

stop:
	docker compose down

build:
	cd .. && \
	docker build \
		-t antoniofernandodj/chickie:${v} \
		-f ./backend/dockerfiles/api.dockerfile backend && \
	docker push antoniofernandodj/chickie:${v}

ct:
	poetry run mypy --check-untyped-defs asgi.py

uic:
	cd backend
	poetry run pyside6-uic src/qt/views/main.ui -o src/qt/views/main_ui.py
	poetry run pyside6-uic src/qt/views/loginForm.ui -o src/qt/views/loginForm_ui.py

qt:
	cd backend
	poetry run python qt.py

test:
	cd backend
	poetry run python -m pytest . -vv

celeryWorker:
	cd backend
	poetry run celery -A scheduler worker --loglevel=info

celeryBeat:
	cd backend
	poetry run celery -A scheduler beat --loglevel=info

celeryScheduler:
	cd backend
	poetry run celery -A scheduler beat --loglevel=info
