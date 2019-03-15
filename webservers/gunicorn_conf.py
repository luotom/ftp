from pathlib import Path
import os

__all__ = (
    'chdir',
    'pythonpath',
    'bind',
    'pidfile',
    'accesslog',
    'errorlog',
    'max_requests',
    'workers',
    'worker_class',
    'daemon',
    'user',
    'group'
)

CPU_COUNT = os.cpu_count()
BASE_DIR = Path(__file__).parent.resolve()
APP_DIR = BASE_DIR.parent

chdir = str(APP_DIR)
pythonpath = str(APP_DIR)
# bind = 'unix:' + str(APP_DIR.joinpath('run', 'app.sock'))
# umask = 0o0000
# bind = '127.0.0.1:5000'
bind = '0.0.0.0:2021'
pidfile = str(APP_DIR.joinpath('run', 'app.pid'))
accesslog = str(APP_DIR.joinpath('log', 'access.gunicorn.log'))
errorlog = str(APP_DIR.joinpath('log', 'error.gunicorn.log'))
max_requests = 500
workers = CPU_COUNT if CPU_COUNT > 8 else CPU_COUNT * 2 + 1
worker_class = 'gevent'
daemon = True
user = 'teaching'
group = 'teaching'
