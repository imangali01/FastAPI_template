from fastapi import HTTPException

from src import config



class Hallo:
    '''Class to work with Trello'''

    @staticmethod
    async def print():
        return 'Hallo World'
        