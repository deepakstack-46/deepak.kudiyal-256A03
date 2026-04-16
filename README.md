# deepak.kudiyal-256A03

# Happy camp - Volunteer Event

A Django web application for managing volunteer events

## Tech Stack
- Python / Django
- Docker
- MySQL (Digital Ocean)
- Github actions 

## User Roles
- **Administrator** - manages events, users and position
- **Member**  - has option to register for events and view reports
- **Volunteer** - can only register for events

## Access the application
Application is running on Digital Ocean at: 

## Setup

1. Clone the repo
```
git clone https://github.com/deepakstack-46/deepak.kudiyal-256A03.git
cd deepak.kudiyal-256A03
```
2 .Install dependencies
```
uv init 
uv sync 
uv venv
```
3. Create `.env` file with your own database credentials

4. Run migrations
```
uv run manage.py migrate
```
5. Seed the database
```
uv run manage.py seed_data
```
6. Sun the server
```
uv run manage.py runserver
```

## Docker

Build and run Docker:
```
docker-compose up --build
```

## CI/CD Pipeline
Github actions pipeline runs with every push to main:
1. Run tests with 50% minimum code coverage
2. If passes build Docker image

## Tests
Run tests with coverage:
```
uv run coverage run --rcfile=.coveragerc manage.py test
uv run coverage report --rcfile=.coveragerc
```