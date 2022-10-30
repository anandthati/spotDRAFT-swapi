# spotDRAFT-swapi
Steps to run the application on local

Step-1: Clone the git repo

`git clone https://github.com/anandthati/spotDRAFT-swapi.git`

Step-2: on the command line change the directory

`cd ~/<root-path>/spotDRAFT-swapi/`

Step-3: Create virtual env

`python3 -m venv venv`

Step-4: Install packages from requirements.txt

`pip3 install -r requirements.txt`

Step-5: Run the following commands

`cd swapi/`

This will create default users to start

`python manage.py create_default_users`

Migrate and run server

`python manage.py migrate`

`python manage.py runserver localhost:8088`

Step-6: test from postman collection
There is a postman collection file included in the root path spotDRAFT-swapi/swpi-spotDraft.postman_collection.json

Each request contains different responses with possible combinations like passing user and search parameters.

