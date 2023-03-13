import tornado.web, abc
import json
from sql_module.models import Link, Password


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/links'

    def get(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            links = Link.all(1)
            return self.render('templates/page.html', links=links)

        self.redirect('/login')

class RequestHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/link-handler'

    def get(self):
        _type = self.get_argument('type')

        if _type == 'paginate':
            prev_page_num = self.get_argument('prev_page_num')
            pagination_type = self.get_argument('pagination_type')

            if pagination_type == 'DataTables_Table_0_next':
                data = Link.all(int(prev_page_num) + 1)
                return self.write(json.dumps(data))

            elif pagination_type == 'DataTables_Table_0_previous':
                data = Link.all(int(prev_page_num) - 1)
                return self.write(json.dumps(data))

        elif _type == 'delete_link':
            Link.delete(self.get_argument('id'))