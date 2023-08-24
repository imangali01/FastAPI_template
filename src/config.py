import os

from dotenv import load_dotenv


if os.environ.get('PROD'):
    load_dotenv('.env.prod')
else:
    load_dotenv('.env')


TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')