# wsgireloader.py - Automatically reload wsgi applications
# Copyright (C) 2013 Marwan Alsabbagh
# license: BSD, see LICENSE for more details.

__version__ = '0.1.dev'

from filewatcher import FileWatcher
from utile import save_args
import sys

SKIP = sorted(sys.modules.keys())


def get_django_app():
    from django.core.wsgi import get_wsgi_application
    return get_wsgi_application()


class Reloader(object):
    @save_args
    def __init__(self, get_app, watch, skip=SKIP, exclude='*.pyc'):
        self.app = self.get_app()
        self.watcher = FileWatcher(watch, exclude=exclude)

    def __call__(self, environ, start_response):
        if self.watcher.changed():
            del self.app
            for i in set(sys.modules.keys()).difference(self.skip):
                del sys.modules[i]
            self.app = self.get_app()
        return self.app(environ, start_response)
