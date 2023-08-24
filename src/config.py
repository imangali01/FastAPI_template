import os

from dotenv import load_dotenv


if os.environ.get('PROD'):
    load_dotenv('.env.prod')
else:
    load_dotenv('.env')


SECRET1 = os.environ.get('SECRET1')
SECRET2 = os.environ.get('SECRET2')
