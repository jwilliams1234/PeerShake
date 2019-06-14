# PeerShake
A community-driven peer review system for bioRxiv.

## Development

### Getting Started
```bash
# Setup a python3 virtual environment
python3 -m venv venv
# Activate the environment
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

### Running
```bash
# Activate your python environment
source venv/bin/activate
# Initialize the database schema
python manage.py migrate
# Start the server
python manage.py runserver
```

### Development
When database models change, make sure to run `python manage.py makemigrations`.

### Deployment
```bash
# build docker image
docker-compose build
# run docker image
docker-compose run start
```
