# Makefile

# Variables
IMAGE_NAME=my-python-app
COMPOSE_FILE=docker-compose.yml

# Targets
build:
	docker build -t $(IMAGE_NAME) .

up: build
	docker compose -f $(COMPOSE_FILE) up -d

down:
	docker compose -f $(COMPOSE_FILE) down

logs:
	docker compose -f $(COMPOSE_FILE) logs -f

clean:
	docker-compose -f $(COMPOSE_FILE) down -v
	docker rmi $(IMAGE_NAME) || true
	docker volume rm $$(docker volume ls -qf dangling=true) || true

.PHONY: build up down logs clean