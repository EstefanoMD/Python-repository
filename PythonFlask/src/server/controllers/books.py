from flask import Flask
from flask_restplus import Api, resource

from server.instance import Server

app,api = Server.api , Server.api

books_db = [
    {'id': 0 , 'title' : 'War and Peace'},
    {'id' : 1 , 'title' : 'Chainsaw'}
]
@api.route('/books')
class BookList(resource):
    def get(self):
        return books_db