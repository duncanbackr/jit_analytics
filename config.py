import os
import environ

env_file = os.path.join(os.getcwd(), ".env")
env = environ.Env()
env.read_env(env_file)

DB_NAME = env.str('DB_NAME')
DB_USER = env.str('DB_USER')
DB_HOST = env.str('DB_HOST')
DB_PASSWORD = env.str('DB_PASSWORD')
ENV = env.str('ENV')
BACKREST_URL = env.str('BACKREST_URL')