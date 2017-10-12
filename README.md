# YCCM Cafe

## Table of Contents
- [Overview](#overview)
- [Getting started](#getting_started)
- [Features](#features)
- [Contributing](#contributing)
- [Licensing](#licensing)

## Overview - Why this project is here -
This is the cafe project for the Filipino American Alliance Church's Youth/College-Career Ministry (FAAC: YCCM).
This readme is for the purposes of development (really a message for myself) and is intended to aid in headache operations
such as database migrations.

This is also my first open source project to which I will try to be actively contributing, so I'm still trying to get the best practices down in both my code AND general open source project practices.

## Getting started 
This is the way I recommend setting up this project for development purposes:

1. Create a virtual environment

For reasons why, go to this blog post: http://docs.python-guide.org/en/latest/dev/virtualenvs/

2. Import all the requirements 

```
pip install -r requirements.txt
```

Note: For Linux developers, the psycopg2 package is different. Install the requirements.txt, fix the settings.py and try to run the server. Look up the exception thrown and fix accordingly. I forget the steps to fix this problem. I will update when I have the time. 

3. Fix your setup.py

The main settings.py file is found in the YCCM_Cafe project directory. We are all smart developers here, do not use the same development database as the production database. Keep your server keys secret. Blah blah blah.

I recommend having two branches, a production and a development branch, for this purpose. On the production, keep your credentials a secret (I personally like the secret JSON approach, in which you take all sensitive information encoded into a JSON file which is not shared within the repository).

Currently, the project uses only PostgreSQL databases. Maybe for a future feature, we can have this interchangeable with other SQL compliant databases. But since, I'm the sole developer at the moment, PostgreSQL it is!

Tada! You should be good to go.

## Features

## Contributing

## Licensing

This project is licensed under Unlicense license. This license does not require you to take the license with you to your project.

