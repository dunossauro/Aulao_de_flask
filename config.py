from os import path
dirname = path.dirname(__file__)



class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{dirname}/db.sqlite3'
    BATATINHAS = 3


class development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class production(Config):
    DEBUG = False
