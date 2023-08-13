api:
	poetry run uvicorn --reload asgi:app

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
