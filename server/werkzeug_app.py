#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )

#run_simple() a method that runs a server for a one-page
#application; not intended to support many users - just to develop
#a simple web page

#run simple arguments:
#hostname - localhost ; typically used in loca development
#port - the given 'extension' to access the resources for our server
#application - the whole application define somewhere else 
#in the code; in our case, its titled application