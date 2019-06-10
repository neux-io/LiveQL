import Live
from _Framework.ControlSurface import ControlSurface # Central base class for scripts based on the new Framework
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import os
import threading
from serve import Serve
#from serve_basic import ServeDebugGraphql
import time


class LiveQL(ControlSurface):

    serve = None
    thread_serve = None

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)

        self.serve = Serve("Serve")

        self.thread_serve = threading.Thread(target=self.serve.start_graphql_endpoint)
        self.thread_serve.daemon = True
        self.thread_serve.start()





            #self.log_message(sys.path)
            #self.log_message("LOADING....")


            #t = self.getTracks()[0]
            #self.log_message("TRACK: {0}".format(t.name))



        self.getTracks()[0].clip_slots[0].create_clip(4)



#    def getSet(self):
#        return Live.Application.get_application().get_document()
#
    def getTracks(self):
        return Live.Application.get_application().get_document().tracks


