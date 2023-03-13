import tornado.web
import abc
from sql_module.models import Password
import json


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/login'

    def get(self):
        self.render('templates/page.html')

class RequestHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/login-handler'

    def get(self):
        password = self.get_argument('password')
        if password == Password.get_password():
            self.set_secure_cookie('JWT', password)
            self.write(json.dumps({
                'type': 'OK'
            }))
        else:
            self.write(json.dumps({
                'type': 'INVALID_PASSWORD'
            }))