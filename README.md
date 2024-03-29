# ZC_LMS

An LMS slightly modelled after the I4G/Zuri LMS by design.

Built with Django!

## SETTING UP

- Clone repository to choice folder in local machine
```
git clone https://github.com/3k3n3/zc_lms.git
```
- Install [requirements/dependencies](requirements.txt)
```
pip install -r requirements. txt
```
- Set up SMTP and cloud storage for media (eg Cloudinary) and database and update .env file with necessary credentials.
See [template](.env.template).
- Running the project locally without any external DB connection will also generate an SQLite database.
```
py manage.py runserver
```
- Migrate database models
```
py manage.py migrate
```
- Popilate country and state/region tables in DB for registration page. See docs on [django-cities-light](https://pypi.org/project/django-cities-light/) for details. 
```
py manage.py cities_light --progress
```
Voila!
You are good to go!

[Contact me](https://github.com/3k3n3/3k3n3) if you run into any trouble setting up.

Suggestions (and corrections) are also very welcome!

### [Design credits](https://twitter.com/Vic_easy/status/1564833547029995520?s=20)