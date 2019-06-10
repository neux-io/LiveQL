from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphene import relay
#from query import LiveQuery
import logging
import sys
import os
import logging


class Serve(Flask):
    app = None
    schema = None

    def __init__(self, *args, **kwargs):
        super(Serve, self).__init__(*args, **kwargs)

        os.environ["WERKZEUG_RUN_MAIN"] = "true"
        self.app = Flask(__name__)

        log = logging.getLogger('werkzeug')
        log.disabled = True
        self.app.logger.disabled = True

        self.app.debug = False
        self.app.use_reloader=False
        self.schema = graphene.Schema(query=QueryDebug)

        self.app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=self.schema,
                graphiql=True # for having the GraphiQL interface
            )
        )

    def start_graphql_endpoint(self):
        self.app.run()

class QueryDebug(graphene.ObjectType):
    node = relay.Node.Field()