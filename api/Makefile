COMPOSE_RUN= docker compose -f local.yml

build:
	$(COMPOSE_RUN) up --build -d --remove-orphans

up:
	$(COMPOSE_RUN) up -d

down:
	$(COMPOSE_RUN) down

show_logs:
	$(COMPOSE_RUN) logs

migrate:
	$(COMPOSE_RUN) run --rm api python3 manage.py migrate

makemigrations:
	$(COMPOSE_RUN) run --rm api python3 manage.py makemigrations

collectstatic:
	$(COMPOSE_RUN) run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	$(COMPOSE_RUN) run --rm api python3 manage.py createsuperuser

down-v:
	$(COMPOSE_RUN) down -v

volume:
	docker volume inspect api_local_postgres_data

authors-db:
	$(COMPOSE_RUN) exec postgres psql --username=salman --dbname=authors-live

test:
	$(COMPOSE_RUN) run --rm api pytest --disable-warnings

sh:
	$(COMPOSE_RUN) run --rm api sh

shell:
	$(COMPOSE_RUN) run --rm api python3 manage.py shell_plus --ipython --quiet-load

flake8:
	$(COMPOSE_RUN) exec api flake8 .

black-check:
	$(COMPOSE_RUN) exec api black --check --exclude=migrations .

black-diff:
	$(COMPOSE_RUN) exec api black --diff --exclude=migrations .

black:
	$(COMPOSE_RUN) exec api black --exclude=migrations .

isort-check:
	$(COMPOSE_RUN) exec api isort . --check-only --skip env --skip migrations

isort-diff:
	$(COMPOSE_RUN) exec api isort . --diff --skip env --skip migrations

isort:
	$(COMPOSE_RUN) exec api isort . --skip env --skip migrations	

