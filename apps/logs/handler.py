import json

import tornado.web, abc
from sql_module.models import Log, Password, session


class PathsHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/logs'

    def get(self):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            logs = Log.all(1)
            return self.render('templates/page.html', logs=logs)
        self.redirect('/login')

class RequestHandler(tornado.web.RequestHandler, abc.ABC):
    PATH = '/logs-handler'

    def get(self):
        _type = self.get_argument('type')

        if _type == 'paginate':
            prev_page_num = self.get_argument('prev_page_num')
            pagination_type = self.get_argument('pagination_type')

            if pagination_type == 'DataTables_Table_0_next':
                data = Log.all(int(prev_page_num) + 1)
                return self.write(json.dumps(data))

            elif pagination_type == 'DataTables_Table_0_previous':
                data = Log.all(int(prev_page_num) - 1)
                return self.write(json.dumps(data))

        elif _type == 'to_code':
            log_type = self.get_argument('log_type')
            print(log_type)
            log = Log.get_by_id(int(self.get_argument('log_id')))
            log.to_code = log_type
            session.commit()