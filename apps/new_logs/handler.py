import tornado.web, abc
from sql_module.models import Log, Password


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/new-logs'

    def get(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            logs = Log.all(1)
            return self.render('templates/page.html', logs=logs)

        self.redirect('/login')