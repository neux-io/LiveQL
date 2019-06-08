from flask import Flask
import logging
import os




class Serve:
    app = None
    schema = None

    def __init__(self):
        os.environ["WERKZEUG_RUN_MAIN"] = "true"
        self.app = Flask("ServeBasic")
        self.app.debug = False


        log = logging.getLogger('werkzeug')
        log.disabled = True
        self.app.logger.disabled = True

        self.app.debug = False
        self.app.use_reloader=False

        self.app.add_url_rule('/', 'about', self.about)
        self.app.run()

    def about(self):
        return "about page"















