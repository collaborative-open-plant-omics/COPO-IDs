__author__ = 'felix.shaw@tgac.ac.uk - 23/07/15'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'test',
        'USER': 'copo',
        'PASSWORD': 'copo',
        'Host': '127.0.0.1',
        'Port': '',
        'init_command' :'SET storage_engine=MyISAM',
    }
}