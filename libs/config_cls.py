# Используемый в примерах JSON
# {
#     "server": {
#         "host": "127.0.0.1",
#         "port": 8080
#     },
#     "static_dir": "/var/www/my_app/static/",
#     "templates_path": "/var/www/my_app/templates/",
#     "database": {
#         "host": "127.0.0.1",
#         "port": 5432,
#         "user": "admin",
#         "password": "1234",
#         "name": "my_db"
#     }
# }

import os
import json

class Config:
    # Класс, представляющий собой обертку для удобного 
    # доступа к конфигурационному файлу вебсервера

    ENV_VAR_NAME = "CONFIG_PATH"

    def __init__(self, config_path):
        # Метод__init__ класса Config принимает на вход один
        # дополнительный аргумент, в котором передается путь к файлу с конфигом
        self.path = config_path
        self._data = {}


    def __getitem__(self, item):
        return self._data[item]


    def read(self):
        with open(self.path) as fd:
            self._data = json.load(fd)


    @staticmethod
    def list_static(static_path):
        ret = []
        for path in os.listdir(static_path):
            _, ext = os.path.splitext(path)
            if ext in [".js", ".html", ".png"]:
                ret.append(path)
        return ret
    # >>> cfg = Config("config.json")  # Инициализируем класс
    # >>> print(cfg.db_connection_uri)
    # postgresql://admin:1234@127.0.0.1:5432/my_db


    @classmethod
    def load_from_env(cls):
        config_path = os.environ[cls.ENV_VAR_NAME]
        return cls(config_path)
    # >>> cfg = Config.load_from_env()
    # >>> print(cfg["server"]["port"])
    # 8080


    @property
    def db_connection_uri(self):
        section = self._data["database"]
        return "postgresql://{user}:{password}@{host}:{port}/{name}".format(**section)
    # postgresql://admin:1234@127.0.0.1:5432/my_db
