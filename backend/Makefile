api:
	poetry run uvicorn --reload asgi:app

ct:
	poetry run mypy --check-untyped-defs asgi.py

uic:
	poetry run pyside6-uic src/qt/views/main.ui -o src/qt/views/main_ui.py
	poetry run pyside6-uic src/qt/views/novaCategoria.ui -o src/qt/views/novaCategoria_ui.py
	poetry run pyside6-uic src/qt/views/novoFuncionario.ui -o src/qt/views/novoFuncionario_ui.py
	poetry run pyside6-uic src/qt/views/mainV2.ui -o src/qt/views/mainV2_ui.py
qt:
	poetry run python qt.py

celeryWorker:
	poetry run celery -A scheduler worker --loglevel=info

celeryBeat:
	poetry run celery -A scheduler beat --loglevel=info

celeryScheduler:
	poetry run celery -A scheduler beat --loglevel=info
