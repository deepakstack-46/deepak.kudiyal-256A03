# deepak.kudiyal-256A03

# Happy camp - Volunteer Event Management

A Django web application for managing volunteer events

## Live Application
Access the application at: http://143.198.40.218:15091
Port: 15091

## Tech Stack
- Python / Django
- Docker
- MySQL (Digital Ocean)
- Github actions 

## User Roles
- **Administrator** - manages events, users and position
- **Member**  - has option to register for events and view reports
- **Volunteer** - can only register for events

## Seed Data Credentials
| Role | Email | Password |
|------|-------|----------|
| Administrator | admin@admin.com | Pa55worD |
| Member | a@b.ca | Pa55worD |
| Member | b@b.ca | Pa55worD |
| Volunteer | vol1@b.ca | Pa55worD |
| Volunteer | vol2@b.ca | Pa55worD |

## Setup

1. Clone the repo
```
git clone https://github.com/deepakstack-46/deepak.kudiyal-256A03.git
cd deepak.kudiyal-256A03
```
2. Install dependencies
```
uv sync 
Key dependencies: `django`, `mysqlclient`, `python-dotenv`, `whitenoise`, `coverage`
```
3. Create `.env` file with your own database credentials
```
DB_NAME=dk_happy_camp
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=25060
SECRET_KEY=your_secret_key
DEBUG=True
```

4. Run migrations
```
uv run manage.py migrate
```
5. Seed the database
```
uv run manage.py seed_data
```
6. Run the server
```
uv run manage.py runserver
```

## Docker

Build and run Docker:
```
docker compose up --build -d
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