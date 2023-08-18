from fastapi import FastAPI

# import asyncio
# import json
import logging

# import socket
# import sys

# from concurrent.futures import ThreadPoolExecutor
# from contextlib import suppress
# from datetime import date, datetime
# from typing import Optional
from typing import Union


from config import settings as s

# from src.infra.database.repository import Empresa, Usuario
# from src.infra.mongo import mongo_logs
# from src.lib import relatorios


# class MongoDBHandler(logging.Handler):
#     def emit(self, record):
#         if record.levelno > logging.INFO:
#             log_entry = self.format(record)
#             with suppress(Exception):
#                 log_entry = json.loads(log_entry)

#             user_id = None
#             with suppress(Exception):
#                 user_id = g.get("user_id")

#             error_message: Union[dict, str] = ""
#             if user_id and isinstance(user_id, int):
#                 user = Usuario.find_one(id=user_id)

#                 if user is not None and user.id is not None:
#                     empresa = Empresa.get(usuario_id=user.id)
#                     error_message = relatorios.render_template(
#                         "error/log.json.jinja2",
#                         user=user,  # type: ignore
#                         empresa=empresa,  # type: ignore
#                         request=request,  # type: ignore
#                     )
#                     with suppress(Exception):
#                         error_message = json.loads(error_message)

#             with suppress(Exception):
#                 log_entry = self.format(record)
#                 with suppress(Exception):
#                     log_entry = json.loads(log_entry)

#                 mongo_logs.insert_one(
#                     {
#                         "entry": log_entry,
#                         "errorData": error_message,
#                         "mode": s.MODE,
#                         "datetime": datetime.utcnow(),
#                         "date": date.today().isoformat(),
#                     }
#                 )


# class LogstashHandler(logging.Handler):
#     def emit(self, record):
#         if record.levelno > logging.INFO:
#             log_entry = self.format(record)
#             with suppress(Exception):
#                 log_entry = json.loads(log_entry)

#             user_id = None
#             with suppress(Exception):
#                 user_id = g.get("user_id")

#             error_message: Union[dict, str] = ""
#             if user_id and isinstance(user_id, int):
#                 user = Usuario.find_one(id=user_id)

#                 if user is not None and user.id is not None:
#                     empresa = Empresa.get(usuario_id=user.id)
#                     error_message = relatorios.render_template(
#                         "error/log.json.jinja2",
#                         user=user,  # type: ignore
#                         empresa=empresa,  # type: ignore
#                         request=request,  # type: ignore
#                     )
#                     with suppress(Exception):
#                         error_message = json.loads(error_message)

#             with suppress(Exception):
#                 log_entry = self.format(record)
#                 with suppress(Exception):
#                     log_entry = json.loads(log_entry)

#                 payload = json.dumps(
#                     {
#                         "entry": log_entry,
#                         "errorData": error_message,
#                         "mode": s.MODE,
#                         "datetime": datetime.utcnow().isoformat(),
#                     }
#                 )

#                 logstash_host = "logstash"
#                 logstash_port = 5000
#                 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                 sock.connect((logstash_host, logstash_port))
#                 sock.sendall(payload.encode("utf-8"))
#                 sock.close()

#                 # sys.stdout = sys.stderr = log_to_logstash


def init_app(app: Union[FastAPI, None] = None):
    logger = logging.getLogger("CHICKIE_LOGGER")
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    datefmt = "[%d/%m/%Y] [%Hh%Mmin%Ss]"
    codes = {
        "CRITICAL": 50,
        "FATAL": 50,
        "ERROR": 40,
        "WARNING": 30,
        "WARN": 30,
        "INFO": 20,
        "DEBUG": 10,
        "NOTSET": 0,
        "OFF": 0,
    }

    log_level = codes[str(s.LOG_LEVEL).upper()]
    if log_level == 0:
        return None

    logging.basicConfig(format=fmt, datefmt=datefmt, level=log_level)
    logger.setLevel(log_level)
    # logger.addHandler(MongoDBHandler())
    logger.info(f"Logging inicializado em level {str(s.LOG_LEVEL).upper()}")

    if app is not None:
        app._logger = logger

    return logger
