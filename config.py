import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_USER = os.environ.get('DB_USER') or 'admin'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or ''
    DB_URL = os.environ.get('DB_URL') or 'localhost:5432'
    DB_NAME = os.environ.get('DB_NAME') or 'spatial_map'
    POSTGRES_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=DB_USER,pw=DB_PASSWORD,url=DB_URL,db=DB_NAME)
    SQLALCHEMY_DATABASE_URI = POSTGRES_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

