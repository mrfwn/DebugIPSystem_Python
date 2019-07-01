DEBUG = True

USERNAME = 'mrfwn'
PASSWORD = 'mrfwn'
SERVER = 'localhost'
DB = 'debugip'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "chave_secreta"