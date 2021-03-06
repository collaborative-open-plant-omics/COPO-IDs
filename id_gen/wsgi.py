"""
WSGI config for id_gen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/var/www/copo_www/IDS')
#sys.path.append('/var/www/copo_www/IDS/make_id')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "id_gen.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()