# Wookie Store

Wookie store is a production-ready REST API self-publishing book store for Wookies, created using Python and Django .

## Environments

This project has two environments: `development` and `production`.
The development environment is where code changes and new features are tested before deployment to production. The production environment is where the finalized, tested code is deployed for use by end-users. <br>

### Development

In this environemnt you can run this project on your local computer. in order to do that, please follow below steps:

1. starting from root directory type `git checkout development` and then `cd api`<br>
2. from `api` directory, create two environment files (`.django` and `.postgres`) with this structure `.envs/.local/.django` and `.envs/.local/.postgres`.<br>
3. put below code in `.envs/.local/.django`<br>

```
CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0

DOMAIN=locahost:8080
EMAIL_PORT=1025

CELERY_FLOWER_USER=admin
CELERY_FLOWER_PASSWORD=admin123456

SIGNING_KEY=XSm8lLNS3Jl9zrOLGBN27QjnDPmaX05PRJtnEE9B7KUToG43AzE
```

4. and put below code in `.envs/.local/.postgres`

```

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=wookie
POSTGRES_USER=wookie
POSTGRES_PASSWORD=admin123456
```

5. then you can build your project by typing `make build` and then run it by typing `make up`. your project is running, but before testing it on your broswer, please type below codes.<br>

```
make shell
from core_apps.common.models import create_groups
create_groups()
exit()
```

You just started shell from the `api` container and called `create_groups` method to create some necessary groups. later we can prevent bad publishers like `Darth Vader` from publishing their work on our platform by putting them in `BannedUser` group. <br><br>

6. now you can access all API Endpoints in `localhost:8080/redoc/`.

7. To create a superuser you can type `make superuser` ... and add your info.... admin panel is acessable in this address `localhost:8080/admin`<br>
8. For SMTP, we're using `mailhog`. you can access mailhog in this address `localhost:8025/`. usually when you want to change your password or create a new user an activation email is sent to `mailhog`.

9. we're also using `celery` for handling asyn tasks like sending email and so on. and we're using `redis` that celery uses it as the `message broker` and `backend result`. we're using `flower` to monitor these tasks and processes. you can monitor these tasks in this address `localhost:5555/`. you may require to add username and password, in that case username is `admin` and password is `admin123456`

10. To run tests you can type `make test`.
11. To see all commands you can type `make help`.

### Production

In this environemnt you can deploy your project.
Please follow below steps:

1. starting from root directory `git checkout master` and then `cd api` from api directory, create two environment files (`.django` and `.postgres`) with this structure `.envs/.production/.django` and `.envs/.production/.postgres`.
   put below code in .envs/.production/.django

```
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_SECRET_KEY= ....       # random charachters

DJANGO_ADMIN_URL= admin/      # you can change your admin and make it difficult to guess for hackers

DJANGO_ALLOWED_HOSTS= ...

RABBITMQ_DEFAULT_USER= ...    # for devlopment we used redis as message broker, for production we chosed Rabbitmq
RABBITMQ_DEFAULT_PASS= ...

CELERY_BROKER= ...
CELERY_BACKEND= ...

DJANGO_SECURE_SSL_REDIRECT=False

CELERY_FLOWER_USER= ...
CELERY_FLOWER_PASSWORD= ...

SMTP_MAILGUN_PASSWORD= ...
DOMAIN= ...                 # wookie.io for example

SIGNING_KEY= ...
```

and put below code in .envs/.local/.postgres

```
POSTGRES_HOST= ...
POSTGRES_PORT= ...
POSTGRES_DB= ...
POSTGRES_USER= ...
POSTGRES_PASSWORD= ...
```

You need to add your changes based on the server you want to host, you might need to create a sperate files like `proxy` for example to store production configuratins of `nginx`.

## Notest.

here's some notes and best practices for this assignment.

- I chosed `nginx` to host static files, a better option might be using a scalable blob sotre like `AWS S3` or google cloud service to host your static files.
- You can make a backup of your DB by typing `docker compose -f local.yml exec postgres backup`. and see your backup history by typing `docker compose -f local.yml exec postgres backups`. I didn't put it in `Makeup` file, because a better approach might be using cloud services like `AWS RDS` or Digitalocean or Google cloud DB services, since they'll handle hosting and maintainance of your DB easily. If you want to host and maintain your DB by your own, you might need to have `cron job` tasks to periodically make a backup of your DB.

* We still have a custom `User` model, but I created a seperate Django app called `authors` because of the scalabily, for now only `authors` can signup and publish their works, but later you might enable users also to signup.

* It's a better idea to have another environment `staging`, for testing and making sure everything works as expected before merging into `master` branch and giving your product in the hands of end-users. I didn't add it because of the simplicity.
