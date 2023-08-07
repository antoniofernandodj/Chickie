api:
	poetry run uvicorn --reload asgi:app

ct:
	poetry run mypy --check-untyped-defs asgi.py

uic:
	poetry run pyside6-uic src/qt/views/main.ui -o src/qt/views/main.py

qt:
	poetry run python qt.py

celeryWorker:
	poetry run celery -A scheduler worker --loglevel=info

celeryBeat:
	poetry run celery -A scheduler beat --loglevel=info

celeryScheduler:
	poetry run celery -A scheduler beat --loglevel=info
