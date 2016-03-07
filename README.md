# Objective

Create a Django project with an action-tracking application. The goal of the application is to store/manage actions. A user should be able to create, change, and delete actions. Actions can be assigned to any user. Actions should have at least a title and a description, and they should be capable of being displayed as a group in some fashion relative to the current month.

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

# Notes

- You'll need to create additional users via the admin, `/admin/` if you want to test assigning to other users.

- I initially implemented this completely via the admin, because I scaffolds a CRUD interface immediately. However, I realized the implementation and amount of work was pretty minimal.

  While this might be good enough for an informal, internal tool, it's not likely what a customer would like to use. In order to flesh the project out I implemented my own CRUD with Django generics CBV's and Bootstrap.

  In the process, however, I _did_ forget to re-use the sort/group by month feature that I implemented from the admin (`actions.admin.DueByFilter`). I'll be fixing that shortly.

- I developed against SQLite locally, out of expediency. However, one of the migrations had a problem when being run against a PostgreSQL database on Heroku. So, all of the Heroku integration bits are there, however the current site is not working (https://shrouded-wildwood-67165.herokuapp.com/), because migrations have not been successfully run yet.

I'll be finishing that shortly as well.
