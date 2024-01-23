reset_schema:
	poetry run python scripts/reset_schema.py
	poetry run alembic upgrade head

lines:
	poetry run python scripts/lines.py

dev:
	cd ..
	docker compose up api-dev

build:
	docker build -t antoniofernandodj/chickie:${v} -f ./dockerfiles/Dockerfile.prod .
	docker push antoniofernandodj/chickie:${v}