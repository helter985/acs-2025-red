import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/acs_db?client_encoding=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    # PostgreSQL specific configuration
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     'pool_size': 10,
    #     'max_overflow': 20,
    #     'connect_args': {
    #         'client_encoding': 'utf8'
    #     }
    # }

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
