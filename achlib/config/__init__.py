import sys
import os
import ConfigParser
from ConfigParser import SafeConfigParser
from logging import *

import pkg_resources

'''
set logging and config parsers
'''
LOCAL_CONFIG = "/app/config-local.ini"

def file_config():
    cfg = SafeConfigParser()
    cfg.readfp(pkg_resources.resource_stream(__name__, "config.ini"))
    if os.path.isfile(LOCAL_CONFIG):
        cfg.readfp(open(LOCAL_CONFIG))
    return cfg
