import logging

import tornado.web
from icew.sqlalchemy import ICEWSQLAlchemy

import settings as icew_settings


db = ICEWSQLAlchemy()


class Router(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=False,
        )

        handlers = []
        super().__init__(handlers, **settings)

    def route(self, url):
        def register(handler):
            self.add_handlers(".*$", [(url, handler)])
            return handler
        return register

    @staticmethod
    def ready():
        global db

        db.configure(icew_settings.config)


app = Router()
