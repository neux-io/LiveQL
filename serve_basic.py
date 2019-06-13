from flask import Flask
from flask_graphql import GraphQLView
import graphene
import logging
import sys
import os
import logging
import graphene
from graphene import relay


class ServeDebugGraphql(Flask):
    app = None
    schema = None

    def __init__(self, *args, **kwargs):
        super(ServeDebugGraphql, self).__init__(*args, **kwargs)

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

        #logging.basicConfig(filename='/Users/piotrek/.liveql/error.log',level=logging.DEBUG)

    def start_graphql_endpoint(self):
        self.app.run()

class QueryDebug(graphene.ObjectType):
    node = relay.Node.Field()


class ServeDebugAbout(Flask):
    app = None
    schema = None

    def __init__(self, *args, **kwargs):
        super(ServeDebugAbout, self).__init__(*args, **kwargs)
        os.environ["WERKZEUG_RUN_MAIN"] = "true"
        self.app = Flask("ServeBasic")
        self.app.debug = False


        log = logging.getLogger('werkzeug')
        log.disabled = True
        self.app.logger.disabled = True

        self.app.debug = False
        self.app.use_reloader=False

        self.app.add_url_rule('/', 'about', self.about)

    def about(self):
        return "about page"

















