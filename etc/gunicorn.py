from __future__ import absolute_import

from shipment import __version__

import gunicorn
gunicorn.SERVER_SOFTWARE = 'Shipment/' + __version__
del gunicorn

proc_name = 'gunicorn-shipment'
umask = 0o022
bind = '127.0.0.1:8000'
workers = 2
worker_class = 'sync'
worker_connections = 100
debug = False
daemon = False
loglevel = 'info'
accesslog = '/opt/shipment/var/log/shipment.access.log'
errorlog = '/opt/shipment/var/log/shipment.error.log'
access_log_format = '"%(h)s %({X-FORWARDED-FOR}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
x_forwarded_for_header = 'X-FORWARDED-FOR'
forwarded_allow_ips = '127.0.0.1'
graceful_timeout = 10
