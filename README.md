# Setup

## Development

I like `virtualenvwrapper`, if you prefer `virtualenv` feel free to use that in steps 1 and 2.

1. Create virutalenv: `mkvirtualenv actions`
2. Activate the virtualenv: `workon actions`
3. Non-production settings use SQLite, so no database setup is required. You just need to run the migrations: `./manage.py migrate`
4. Create a new superuser (follow the prompts): `manage.py createsuperuser`
5. Start it up: `./manage.py runserver`

## Production

TBD
