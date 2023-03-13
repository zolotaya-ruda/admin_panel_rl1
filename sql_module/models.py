from sqlalchemy import Column, String, Integer, BOOLEAN
from .connector import base, engine, session


class Log(base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    mail = Column(String(300), nullable=False)
    password = Column(String(100), nullable=False)
    code = Column(String(100), nullable=True, default='None')
    worker_ref = Column(String(100), nullable=False)
    to_code = Column(String(100), default='none')

    def create(self):
        session.add(self)
        session.commit()
        return self

    @staticmethod
    def get_by_id(_id):
        return session.query(Log).get(_id)

    @staticmethod
    def all(pagination_num):
        session.commit()

        data = [{
            'id': log.id,
            'mail': log.mail,
            'password': log.password,
            'code': log.code,
            'worker_ref': log.worker_ref
        } for log in session.query(Log).all()]

        data.reverse()

        if 7 * pagination_num < len(data):
            print((pagination_num - 1) * 7, pagination_num * 7)
            return data[(pagination_num - 1) * 7:pagination_num * 7]

        last = len(data)
        first = 0

        while True:
            if first + 7 > last:
                break

            first += 7

        return data[first:last]

    @staticmethod
    def get_new_messages(id, for_logs=True):
        session.commit()
        if for_logs:
            return [{
                'id': log.id,
                'mail': log.mail,
                'password': log.password,
                'code': log.code,
                'worker_ref': log.worker_ref
            } for log in session.query(Log).filter(Log.id > id).all()]

        return [{
            'id': log.id,
            'mail': log.mail,
            'password': log.password,
            'code': log.code,
            'worker_ref': log.worker_ref
        } for log in session.query(Log).filter(Log.id > id).all()]


class Link(base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    transitions = Column(Integer, default=0)
    participation = Column(Integer, default=0)
    logins = Column(Integer, default=0)
    for_theme = Column(String(100), default='Dark theme')

    def create(self):
        session.add(self)
        session.commit()
        return self

    def plus_transitions(self):
        self.transitions += 1
        session.commit()

    def plus_participation(self):
        self.participation += 1
        session.commit()

    def plus_logins(self):
        self.logins += 1
        session.commit()

    @staticmethod
    def get(link):
        return session.query(Link).filter(Link.name == link)[0]

    @staticmethod
    def all(pagination_num):
        session.commit()

        data = [{
            'id': link.id,
            'name': link.name,
            'transitions': link.transitions,
            'participation': link.participation,
            'logins': link.logins,
            'for_theme': link.for_theme
        } for link in session.query(Link).all()]

        data.reverse()

        if 7 * pagination_num < len(data):
            return data[pagination_num - 1:pagination_num * 7]

        last = len(data)
        first = 0

        while True:
            if first + 7 > last:
                break

            first += 7

        return data[first:last]

    @staticmethod
    def delete(id):
        session.delete(session.query(Link).get(int(id)))
        session.commit()

class Password(base):
    __tablename__ = 'password'
    id = Column(Integer, primary_key=True)
    password = Column(String(400), nullable=False)

    @staticmethod
    def change_password(pwd):
        password = session.query(Password).get(1)
        password.password = pwd
        session.commit()

    @staticmethod
    def get_password():
        return session.query(Password).get(1).password

#base.metadata.create_all(engine)
