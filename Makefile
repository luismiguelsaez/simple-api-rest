
setup:
	docker network create test

build-app:
	docker build -t api-ci:latest app

build-test:
	docker build -t api-ci-test:latest test

run-test:
	docker run --network test --rm --name api-ci-test -e ENDPOINT=http://api-ci-run api-ci-test:latest

run-app:
	docker run -d --network test --name api-ci-run -p 8080:80 api-ci:latest

clean:
	docker rm -f api-ci-run && docker network rm test

