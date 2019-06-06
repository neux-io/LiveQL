from flask import Flask
from flask_graphql import GraphQLView
import graphene
from query import Query

class Serve(object):
    app = None
    schema = None

    def __init__ (self):
        self.app = Flask(__name__)
        self.app.debug = True
        self.schema = graphene.Schema(query=Query)

        self.app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=self.schema,
                graphiql=True # for having the GraphiQL interface
            )
        )

        self.app.run()

