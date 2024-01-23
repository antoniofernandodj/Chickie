dev:
	ng serve --host 0.0.0.0 --port 4200

build:
	docker build -t antoniofernandodj/chickie-frontend:${v} -f ./dockerfiles/Dockerfile.prod .
	docker push antoniofernandodj/chickie-frontend:${v}
