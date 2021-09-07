import re
from wsgiref.simple_server import make_server

class Dispatcher:

    def __init__(self, routes) -> None:
        self.routes = routes

    def __matchUri(self, uri):
        matched_routes = []
        params = []
        for route in self.routes:
            path = re.sub("^<[^>]+>", "(.+)", route["path"])
            matches = re.findall("^" + path + "$", uri)
            if matches:
                matched_routes.append(route)
                matches.pop(0)
                params = matches
        
        return (matched_routes, params)
    
    def application(self, environ, start_response):
        matched_routes = self.__matchUri(environ["PATH_INFO"])
        headers = [('Content-type', 'text/html')]
        if not matched_routes[0]:
            status = "404 Not Found"
            body = b"<h1>404 Not Found</h1><hr>Lime"
            start_response(status, headers)
            return [body]            
        

        for route in matched_routes[0]:
            if environ["REQUEST_METHOD"] not in route["methods"]:
                status = "400 Bad Request"
                body = b"<h1>404 Not Found</h1><hr>Lime"
                start_response(status, headers)
                return [body]
            
            status = "200 OK"
            body = bytes(route["action"](), "utf-8")
            start_response(status, headers)
            return [body]
        
    def run(self):
       httpd = make_server("localhost", 8000, self.application)
       httpd.serve_forever()
