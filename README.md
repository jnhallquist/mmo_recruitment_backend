# SETUP

### Quick Setup
```
cat <<EOT >> ~/.bashrc
# MMO_RECRUITEMENT ENV VARS
export MMO_RECRUITMENT_DB_NAME=mmo_recruitment
export MMO_RECRUITMENT_DB_USERNAME=makoto
export MMO_RECRUITMENT_DB_PASSWORD=makoto
export MMO_RECRUITMENT_PGADMIN_DEFAULT_PASSWORD=makoto
export MMO_RECRUITMENT_PGADMIN_DEFAULT_EMAIL=makoto
EOT

source ~/.bashrc

python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

docker-compose up

python manage.py migrate

python manage.py runserver

app: localhost:8000
db: localhost:5050
```

### PGAdmin Server

Connecting to the Postgres Server

* Create Server

```
General
Name: mmo_recruitment

Connection
Host: db
Port: 5432
Username: whatever MMO_RECRUITMENT_DB_USERNAME is or makoto
Password: whatever MMO_RECRUITMENT_DB_PASSWORD is or makoto
```

* Click Save
