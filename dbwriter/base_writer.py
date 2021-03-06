# -*- coding: UTF-8 -*-


class WriterBase(object):

    # 构造函数
    def __init__(self, host, port, dbname, username, password,magic_field_name):
        self._host = host
        self._port = port
        self._dbname = dbname
        self._username = username
        self._password = password

        self._magic_field_name=magic_field_name

        self._connection = None

    def connect(self):
        pass

    def close(self):
        pass

    def drop_table(self, table_name):
        pass

    def create_table(self, create_table_sql):
        pass

    def insert_value(self, insert_sql, rows):
        pass

    # 装饰器 host
    @property
    def host(self):
        return self._host

    # 装饰器 port
    @property
    def port(self):
        return self._port

    # 装饰器 dbname
    @property
    def dbname(self):
        return self._dbname

    # 装饰器 username
    @property
    def username(self):
        return self._username

    # 装饰器 password
    @property
    def password(self):
        return self._password

    # 装饰器 connection
    @property
    def connection(self):
        return self._connection

    # 装饰器 magic_field_name
    @property
    def magic_field_name(self):
        return self._magic_field_name