import os
basedir = os.path.abspath(os.path.dirname(__file__))

username = 'ds4a'
password = 'ds4A-7eaM79'
url = 'ds4a.cm1dcdf7pnnv.us-east-2.rds.amazonaws.com'
port = 5432
database = 'team_79'

connection_string = f'{username}:{password}@{url}:{port}/{database}'

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://' + connection_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
