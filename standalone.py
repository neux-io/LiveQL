from serve_basic import Serve
import os
import time



pid=os.fork()
if pid == 0:
    s = Serve()
    # parent



while True:
    print("I'm the parent")
    time.sleep(0.5)

