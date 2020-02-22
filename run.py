import pkgutil
from tornado.ioloop import IOLoop

from obelisk import app
from obelisk import handlers


def load_handlers(module):
    for _, name, ispkg in pkgutil.iter_modules(module.__path__):
        module_name = '%s.%s' % (module.__name__, name)

        if not (name and name.endswith('handler')):
            continue

        _module = __import__(module_name, fromlist=[''])

        if ispkg:
            load_handlers(_module)


if __name__ == '__main__':
    load_handlers(handlers)
    app.ready()
    app.listen(8888)
    IOLoop.current().start()
