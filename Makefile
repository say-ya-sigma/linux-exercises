up:
	@docker compose up -d

build:
	@docker compose build

down:
	@docker compose down

bash:
	@docker compose exec linux bash