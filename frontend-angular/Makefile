dev:
	ng serve --host 0.0.0.0 --port 4200

build:
	docker build -t antoniofernandodj/chickie-frontend:${v} -f ./dockerfiles/client.dockerfile .
	docker push antoniofernandodj/chickie-frontend:${v}
