LOCAL_COMPOSE = docker compose -f docker-compose.local.yml
DEV_COMPOSE = docker compose -f docker-compose.dev.yml

local-up: ## Запустить local окружение
	$(LOCAL_COMPOSE) up -d

local-down: ## Остановить и удалить local окружение
	$(LOCAL_COMPOSE) down

dev-up: ## Запустить dev окружение
	$(DEV_COMPOSE) up -d

dev-down: ## Остановить и удалить dev окружение
	$(DEV_COMPOSE) down
