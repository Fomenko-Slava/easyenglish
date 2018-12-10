#!/bin/sh
/usr/local/bin/gunicorn wsgi -w 1 -b 0.0.0.0:5000 --chdir=/app --timeout 100 --log-level debug