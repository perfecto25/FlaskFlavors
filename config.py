SECRET_KEY = 'flavorflav'
WTF_CSRF_ENABLED = True
PORT = 5700
APP_DIR = '/home/user/flavor'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + APP_DIR + '/app/auth/users.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

