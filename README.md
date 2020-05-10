# SETUP

```
cat <<EOT >> ~/.bashrc
export MMO_RECRUITMENT_DB_NAME=mmo_recruitment
export MMO_RECRUITMENT_DB_USERNAME=makoto
export MMO_RECRUITMENT_DB_PASSWORD=makoto
export MMO_RECRUITMENT_DB_PGADMIN_PASSWORD=makoto
EOT

source ~/.bashrc

python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

docker-compose up

python manage.py migrate

python manage.py runserver
```
