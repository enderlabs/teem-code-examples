# Teem Relay using Python with Flask
This relay example uses the Flask Python microframework to simply receive a
request from the google push service, and then relay it to Teem.

Dependencies for this project are found in the requirements.txt. This is
specifically Requests and Flask. pip install -r requirements.txt will install
needed dependencies to your python path.

## Deployment
Because this uses the Flask microframework, Flask provides multiple simple
options for deploying this code, from various hosted options such as Heroku and
PythonAnywhere, to self-hosted options such as Apache or Gunicorn. For more
details [please see their documentation directly](http://flask.pocoo.org/docs/0.12/deploying/)

## Licensing
[Flask is licensed under their three clause BSD license](http://flask.pocoo.org/docs/0.12/license/#flask-license).
[Requests is licensed under their Apache2 License](http://docs.python-requests.org/en/master/user/intro/#requests-license)
Teem provides this software under a MIT license. Please see LICENSE.md for
details.
