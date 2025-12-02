import os
basedir  =os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    JWT_SECRET_KEY = 'secret' 
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # token 过期时间（秒）
    