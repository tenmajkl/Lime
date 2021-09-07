from Dispatcher import Dispatcher

class Route:

    routes = []

    @staticmethod
    def setRoute(path:str, methods, action):
        Route.routes.append({"path": path, "methods": methods, "action": action})

    @staticmethod
    def get(path:str, **options):
        if "controller" in options:
            Route.setRoute(path, ("GET"), options["controller"])
        def decorator(action):
            Route.setRoute(path, ("GET"), action)
            return action
        return decorator



    @staticmethod
    def post(path:str, action):
        Route.setRoute(path, ("POST"), action)

    @staticmethod
    def any(path:str, action):
        Route.setRoute(path, ("GET", "POST", "PUT", "HEAD", "DELETE", "PATCH", "OPTIONS"), action)

    @staticmethod
    def use(methods:tuple, path:str, action):
        Route.setRoute(path, methods, action)

    @staticmethod
    def execute():
        dispatcher = Dispatcher(Route.routes)
        dispatcher.run()

