import tornado.web

from obelisk import db


class BaseHandler(tornado.web.RequestHandler):
    def on_finish(self):

        # do commit or rollback
        try:
            db.commit_all()
        except:
            db.rollback_all()
            raise
