"""
Gunicorn configuration for MMIT Central Institutional Library.
"""
import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 60
keepalive = 5
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "/var/log/gunicorn/mmit_library_access.log"
errorlog = "/var/log/gunicorn/mmit_library_error.log"
loglevel = "info"

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

