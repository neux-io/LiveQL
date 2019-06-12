from serve_basic import ServeDebugGraphql
import time
import threading
import multiprocessing
import logging
import sys
print "Starting GraphQL Endpoint: http://localhost:5000/graphql"


#s=ServeDebugGraphql("ServeBasic")
#d = multiprocessing.Process(name='FlaskDaemon', target=s.start_graphql_endpoint)
#d.daemon = True
#d.start()



#s=ServeDebugGraphql("ServeBasic")
#t1 = threading.Thread(target=s.start_graphql_endpoint)
#t1.start()




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
        self.s = ServeDebugGraphql("ServeBasiccc")
        self.name = 'FlaskDaemon'


    def run(self):
        thread_logger = logging.getLogger(self.name)
        sys.stdout = StreamToLogger(thread_logger, logging.INFO)
        sys.stderr = StreamToLogger(thread_logger, logging.ERROR)
        thread_logger.info("Starting " + self.name + "...")
        self.s.start_graphql_endpoint()

print "Notice how regular print statements don't go to the log."
#testing_module = __import__("test_thread")

test_job = JobProcess()
test_job.start()
print "Process queued!"

x = True
while x:
    time.sleep(3)
    print "Wait 3s ..."