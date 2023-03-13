import json

import tornado.web
import abc
from sql_module.models import Password


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/change-password'

    def get(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            return self.render('templates/page.html')

        self.redirect('/login')

    def post(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            old_pwd = self.get_argument('old_pwd')

            if old_pwd == Password.get_password():
                new_pwd = self.get_argument('new_pwd')
                Password.change_password(new_pwd)
                self.set_secure_cookie('JWT', new_pwd)
                self.write(json.dumps({
                    'type': 'OK'
                }))

            else:
                self.write(json.dumps({
                    'type': 'INVALID_OLD_PWD'
                }))