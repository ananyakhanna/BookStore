"""
WSGI config for bookstoreproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys


sys.path.append('C:/Users/will4/book-store/bookstoreproject')
sys.path.append('C:/Users/will4/book-store/bookstoreproject/bookstoreproject')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstoreproject.settings')

application = get_wsgi_application()


