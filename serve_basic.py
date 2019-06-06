from flask import Flask
from flask_graphql import GraphQLView
import graphene
from query import Query


class Serve:
    app = None
    schema = None

    def __init__(self):
        self.app = Flask("Serve")
        self.app.debug = False
        self.app.add_url_rule('/', 'about', self.about)
        self.app.run()

    def about(self):
        return "about page"












