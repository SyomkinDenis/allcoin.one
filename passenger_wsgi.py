# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2302776/data/www/allcoin.one/allcoin')
sys.path.insert(1, '/var/www/u2302776/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'allcoin.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()