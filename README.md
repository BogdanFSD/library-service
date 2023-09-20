# Library Service
This project provides a RESTful API for managing library system. Project focuses on developing an online management system for book borrowings


## Requirements
- Python 3 must be  installed;
- Docker and Docker Compose;
- Postgres DB.

## Installation

```shell
git clone https://github.com/BogdanFSD/library-service.git
```

```shell
cd library-service
```

```shell
python -m venv venv
```
```shell
venv\Scripts\activate (Windows)
```
```shell
source venv/bin/activate (Linux or macOS)
```

```shell
copy .env.sample -> .env and filled up with required data
```

```shell
pip install -r requirements.txt
```

```shell
python manage.py migrate
```

```shell
python manage.py runserver
```

## Run docker to start the development server:

```shell
docker-compose up --build
```

## Getting access
<hr>

- Create user via /api/user/register/
- Get access token via /api/user/token/


## API documentation

The API documentation is available at:
- api/doc/swagger/

## Features
<hr>

- JWT authenticated;
- Users authentication & registration
- Managing users borrowings of books
- Telegram notifications for borrowing events
- Stripe payments integration for book borrowings


## Users Service:
Managing authentication & user registration
API:
- POST: users/ - register a new user
- POST: users/token/ - get JWT tokens
- POST: users/token/refresh/ - refresh JWT token
- GET:  users/me/ - get my profile info
- PUT/PATCH: users/me/ - update profile info

## Borrowings Service:
Managing users' borrowings of books
API:
- POST: borrowings/ - add new borrowing
- GET:  borrowings/  - get borrowings
- GET:  borrowings/id/ - get specific borrowing
- POST: borrowings/id/return/ - return borrowed book