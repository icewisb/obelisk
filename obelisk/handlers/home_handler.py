from obelisk.handlers.base_handler import BaseHandler
from obelisk import db, app


@app.route(r'/')
class HomeHandler(BaseHandler):
    def get(self):
        item = db.session.execute('SELECT * FROM user').fetchone()

        self.write({
            'id': item.id
        })

    def post(self):
        rv = db.session.execute("INSERT INTO user () VALUES ()")
        self.write({
            'rows': rv.lastrowid
        })
