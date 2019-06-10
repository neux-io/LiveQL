from serve_basic import ServeDebugGraphql
import time
import threading
print "Starting GraphQL Endpoint: http://localhost:5000/graphql"
s=ServeDebugGraphql("ServeBasic")

t1 = threading.Thread(target=s.start_graphql_endpoint)
t1.start()

x = True
while x:
    time.sleep(3)
    print "Wait 3s ..."