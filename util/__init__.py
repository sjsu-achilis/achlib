# -*- coding: utf-8 -*-
import time
import sys
import socket
import os
import datetime
import subprocess
import shlex

from achlib.config import file_config
from achlib.util import logger

log = logger.getLogger(__name__)
config = file_config()

def timit(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        log.info('{} transaction took {:.3f} seconds'.format(f.func_name, (time2-time1)))
        return ret

    return wrap


def get_host_details():
    host = {
        'host_name': None,
        'host_ip': None
    }
    try:
        host['host_name'] = socket.gethostname()
        host['host_ip'] = socket.gethostbyname(socket.gethostname())
    except:
        pass

    return host


def run_command(command, async=True):
    process = subprocess.Popen(shlex.split(command), preexec_fn=os.setpgrp, stdout=subprocess.PIPE)
    while not async:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()

    return process,rc

def get_log_file():
    log_base = os.environ.get("LOG_BASE")
    log_dir = log_base + '/applogs'
    if not os.path.exists(os.path.abspath(log_dir)):
        os.makedirs(os.path.abspath(log_dir))

    return log_dir+'/log_'+datetime.datetime.today().strftime('%Y%m%d') \
           +'.log'
