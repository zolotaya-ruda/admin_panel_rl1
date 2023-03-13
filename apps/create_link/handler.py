import json
import tornado.web, abc
from sql_module.models import Link, Password


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/create-link'

    def get(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            return self.render('templates/page.html')

        self.redirect('/login')

    def post(self):
        link = self.get_argument('name')
        theme = self.get_argument('theme')

        try:
            Link(name=link, for_theme=theme).create()
        except Exception as e:
            print(e)
            return self.write(json.dumps({'type': 'ERR'}))

        self.write(json.dumps({'type': 'OK'}))
