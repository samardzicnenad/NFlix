The elements of this project were started during my first (out of 3) course at The Hackerati academy.
The goal of the course was to learn Python and to get introduced to a Django framework.
The idea for the project was to build a Netflix-like movie recommendation engine in Python and to implement it as a Django application.
Data set used was taken from the GroupLense research and I used MovieLens 100k (consists of 100,000 ratings from 1000 users on 1700 movies.). The original data files' coding had to be changed, so I'm providing encoded data files to be used.

In order to use the application it is necessary to create an appropriate mySQL database.
A file with SQL scripts is provided (Steps.txt).

The application was built using local Django development server with default parameters.
It provides possibility of user registration, signing in and out, rating exiting and/or new movies and getting (parameter is set to 25) recommended unseen movies.

MVC pattern is followed. CSS is used to separate the presentation parameterization

Some elements od the settings.py file need to be updated (see multiple x):
ADMINS = (
    ('XXXXX', 'xxxxx@xxxxx.xxx'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'nflix',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'xxxxx',
        'PASSWORD': 'XXXXX',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}