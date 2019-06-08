from flask import Flask
from flask_graphql import GraphQLView
import graphene
from query import Query
import logging
import sys
import os



class Serve(object):
    app = None
    schema = None

    def __init__ (self):

        os.environ["WERKZEUG_RUN_MAIN"] = "true"
        self.app = Flask(__name__)

        log = logging.getLogger('werkzeug')
        log.disabled = True
        self.app.logger.disabled = True

        self.app.debug = False
        self.app.use_reloader=False
        self.schema = graphene.Schema(query=Query)

        self.app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view(
                'graphql',
                schema=self.schema,
                graphiql=True # for having the GraphiQL interface
            )
        )

        logging.basicConfig(filename='/Users/piotrek/.liveql/error.log',level=logging.DEBUG)
        self.app.run(threaded=True)

