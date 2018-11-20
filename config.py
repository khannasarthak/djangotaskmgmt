import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # app.config['MONGO _DBNAME'] = 'taskmgmt'
    # app.config['MONGO_URI'] = 'mongodb://sarthak:qwerty123@ds157843.mlab.com:57843/taskmgmt'