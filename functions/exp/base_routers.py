import functools
import re

class Router:
    def __init__(self):
        self._routes = {}
        self._default_route = None
        self.DefaultRoute = self._defaultRoute()
    
    def Route(self, routeId):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._routes[routeId] = wrapfunc
            return wrapfunc
        return decorator
    
    def _defaultRoute(self):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._default_route = wrapfunc
            return wrapfunc
        return decorator

    def handle(self, routeId, *args, **kwargs):
        if routeId in self._routes:
            return self._routes[routeId](*args, **kwargs)
        else:
            if callable(self._default_route):
                return self._default_route(*args, **kwargs)
            else:
                return None

class LinearSearchRouter(object):
    def __init__(self):
        self._routes = {}
        self._default_route = None
        self.DefaultRoute = self._defaultRoute()
    
    def Route(self, key):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._routes[key] = wrapfunc
            return wrapfunc
        return decorator
    
    def _defaultRoute(self):
        def decorator(f):
            @functools.wraps(f)
            def wrapfunc(*args, **kwargs):
                return f(*args, **kwargs)
            self._default_route = wrapfunc
            return wrapfunc
        return decorator

    def match(self, key, target):
        return key == target

    def handle(self, target, *args, **kwargs):
        try:
            for key in self._routes.keys():
                if self.match(key, target):
                    return self._routes[key](*args, **kwargs)
        except TypeError:
            pass
        return self.handle_default_route(*args, **kwargs)

    def handle_default_route(self, *args, **kwargs):
        if callable(self._default_route):
            return self._default_route(*args, **kwargs)
        else:
            return None

class RegexRouter(LinearSearchRouter):
    def __init__(self, regex_flags = 0):
        super(RegexRouter, self).__init__()
        self.regex_flags = regex_flags
        self._compiled = {}
    
    def Route(self, regex):
        self._compiled[regex] = re.compile(regex, flags = self.regex_flags)
        return super(RegexRouter, self).Route(regex)
    
    def match(self, regex, target):
        compiled_regex = self._compiled[regex]
        return compiled_regex.match(target)