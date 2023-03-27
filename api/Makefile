help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  build          Build docker images"
	@echo "  up             Run the docker containers"
	@echo "  down           To stop running containers"
	@echo "  show_logs      To see logs"
	@echo "  migrate        To sync your migrations to db"
	@echo "  makemigrations To make migration files"
	@echo "  collectstatic  To collectstatic files"
	@echo "  superuser      To create superuser"
	@echo "  down-v         To stop containers and remove volumes"
	@echo "  volume         To instpect volumes"
	@echo "  wookie-db      To to start psql from your terminal"
	@echo "  test           To run tests"
	@echo "  sh             To start shell from the projct container"
	@echo "  shell          To access api python console"
	@echo "  flake8         To check lintings"
	@echo "  black-check    Using black to for linting check"
	@echo "  black-diff     See linting differences before applying black"
	@echo "  black          to apply black linting"
	@echo "  isort-check    To check whether import sorts are correct"
	@echo "  isort-diff     To see sorts differences"
	@echo "  isort          To sort imports correctly"





build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show_logs:
	docker compose -f local.yml logs

migrate:
	docker compose -f local.yml run --rm api python3 manage.py migrate

makemigrations:
	docker compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python3 manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect api_local_postgres_data

wookie-db:
	docker compose -f local.yml exec postgres psql --username=salman --dbname=authors-live

test:
	docker compose -f local.yml run --rm api pytest --disable-warnings

sh:
	docker compose -f local.yml run --rm api sh

shell:
	docker compose -f local.yml run --rm api python3 manage.py shell_plus --ipython --quiet-load

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip env --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip env --skip migrations	

