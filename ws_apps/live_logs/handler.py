import json
import tornado.websocket, abc
from sql_module.models import Log, Password

class WSHandler(tornado.websocket.WebSocketHandler, abc.ABC):
    PATH = '/live-logs'

    def open(self, *args: str, **kwargs: str):
        print(args, kwargs)

    def on_message(self, message):
        if self.get_secure_cookie('JWT') is None:
            return self.redirect('/login')

        if self.get_secure_cookie('JWT').decode() == Password.get_password():
            data = json.loads(message)
            print(data)
            if data['type'] == 'GET_DATA':
                new_logs = Log.get_new_messages(int(data['last_id']), for_logs=data['for_logs'])
                if len(new_logs) > 0:
                    self.write_message(json.dumps(new_logs))

        else:
            self.close()