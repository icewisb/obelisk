#!/usr/bin/env python3
# -*- coding: utf-8 -*-

config = {
    'SQLALCHEMY_BINDS': {},
    'SQLALCHEMY_ECHO': False,
}

try:
    from local_settings import config as local_config
    config.update(local_config)
except ImportError:
    pass

try:
    from dev_settings import config as dev_config
    config.update(dev_config)
except ImportError:
    pass

try:
    from prod_settings import config as prod_config
    config.update(prod_config)
except ImportError:
    pass
