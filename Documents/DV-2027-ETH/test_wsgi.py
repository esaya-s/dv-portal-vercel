#!/usr/bin/env python
"""
Simple test WSGI to isolate the issue
"""

def application(environ, start_response):
    """Simple WSGI application for testing"""
    
    # Get the request method and path
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')
    
    # Simple response
    if path == '/':
        response_body = b"""
        <html>
        <head><title>Django Test</title></head>
        <body>
            <h1>Django Test Page</h1>
            <p>WSGI is working!</p>
            <p>Method: """ + method.encode() + b"""</p>
            <p>Path: """ + path.encode() + b"""</p>
            <p>Time: """ + str(__import__('datetime').datetime.now()).encode() + b"""</p>
        </body>
        </html>
        """
    else:
        response_body = b"<h1>404 - Page Not Found</h1>"
    
    # Set response headers
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    
    start_response(status, headers)
    return [response_body]