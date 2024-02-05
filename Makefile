dev:
	docker compose down && docker compose up api-dev client-angular-dev --build -d

qt:
	cd backend && poetry run python qt.py