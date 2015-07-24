__author__ = 'felix.shaw@tgac.ac.uk - 23/07/15'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'uids',
        'USER': 'fshaw',
        'PASSWORD': '',
        'Host': '127.0.0.1',
        'Port': '',
        'init_command' :'SET storage_engine=MyISAM',
    }
}