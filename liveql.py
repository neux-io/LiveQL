import Live
from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
#sys.path.append('/Users/piotrek/Library/Python/2.7/lib/python/site-packages/multiprocessing')
import os
#import multiprocessing
import threading
#from serve import Serve
from serve_basic import ServeDebugAbout
import time
import logging
import sys



class LiveQL(ControlSurface):

    serve = None
    thread_serve = None
    logging = None

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)



        #self.serve = Serve("Serve")
        #d = multiprocessing.Process(name='FlaskDaemon', initializer=mute, target=self.serve.start_graphql_endpoint)
        #d.daemon = True
        #d.start()

        #self.serve = Serve("Serve")
        #self.thread_serve = threading.Thread(target=self.serve.start_graphql_endpoint)
        #self.thread_serve.daemon = True
        #self.thread_serve.start()

        #self.serve = ServeDebugAbout("ServeBasic")
        #d = multiprocessing.Process(name='FlaskDaemon', target=self.serve.app.run())
        #d.daemon = True
        #d.start()

        self.serve = ServeDebugAbout("Serve")
        self.thread_serve = threading.Thread(target=self.serve.app.run)
        self.thread_serve.daemon = True
        self.thread_serve.start()

        #self.thread_serve = ServeDebugAbout()
        #self.thread_serve.ServeDebugAbout()

            #self.log_message(sys.path)
            #self.log_message("LOADING....")

            #t = self.getTracks()[0]
            #self.log_message("TRACK: {0}".format(t.name))

        self.getTracks()[0].clip_slots[0].create_clip(4)

#    def getSet(self):
#        return Live.Application.get_application().get_document()
#
    def update_display(self):
        self.log_message(self.thread_serve.isAlive())
        #time.sleep(80)

    def getTracks(self):
        return Live.Application.get_application().get_document().tracks

    def is_extension(self):
        return False

'''
class StreamToLogger(object):
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
    filename="threading.log",
    filemode='a'
)

class JobProcess(multiprocessing.Process):
    def __init__(self):
        super(JobProcess, self).__init__()
        self.s = Serve("Serve")
        self.name = 'FlaskDaemon'


    def run(self):
        thread_logger = logging.getLogger(self.name)
        sys.stdout = StreamToLogger(thread_logger, logging.INFO)
        sys.stderr = StreamToLogger(thread_logger, logging.ERROR)
        thread_logger.info("Starting " + self.name + "...")
        self.s.start_graphql_endpoint()
'''