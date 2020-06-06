import os

Params = {
    "server": "127.0.0.1",
    "port": 8080,
    'url': '/assets/report/',
    'request_timeout': 30,
}

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
