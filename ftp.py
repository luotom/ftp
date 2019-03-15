import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import logger
import pymysql
from config import *


def get_teacher_msgs():
    try:
        db = pymysql.connect(host=db_host, user=db_user,
               password=db_password, db=db_name, port=db_port)
    except Exception as error:
        logger.error(error)
        return None
    cur = db.cursor()
    sql = "select userName, password, name  from teacher"
    try:
        cur.execute(sql)
        results = cur.fetchall()
    except Exception as error:
        logger.error(error)
        results = None
    finally:
        db.close()
    return results


def main():
    # 新建一个用户组
    users = DummyAuthorizer()
    handler = FTPHandler
    users.add_anonymous("/home/teaching/app", perm="el")
    results = get_teacher_msgs()
    if results:
        for row in results:
            users.add_user(row[0], row[1], f"/home/teaching/app/{row[2]}", perm="elrwdmf")
            users.override_perm('anonymous', f"/home/teaching/app/{row[2]}/上传",
                                perm="elw", recursive=True)
            users.override_perm('anonymous', f"/home/teaching/app/{row[2]}/下载",
                                perm="elr", recursive=True)
    handler.authorizer = users
    return handler


if __name__ == '__main__':
    logging.basicConfig(filename='./log/ftpsever.log', level=logging.DEBUG)
    main_handler = main()
    server = FTPServer(sever_ip, main_handler)
    server.max_cons = max_cons
    server.max_cons_per_ip = max_cons_per_ip
    # _log_start()-> FTPServer._log_start(self)
    server.serve_forever()
