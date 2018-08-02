# -*- coding: utf-8 -*-
import os
import sys

import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from achlib.config import file_config
from achlib.util import logger

log = logger.getLogger(__name__)
config = file_config()

POOL = ThreadedConnectionPool(1,100, dbname=config.get('DB','dbname'), \
       user=config.get('DB','user'), password=config.get('DB','pswd'), \
       host=config.get('DB','host') , port=config.get('DB','port'))


def db_fetch(query, fetch='all'):
    conn = POOL.getconn()
    cur = conn.cursor()
    try:
        cur.execute("{}".format(query))
        if fetch=='all':
            res = cur.fetchall()
        else:
            res = cur.fetchmany(fetch)
    except:
        log.error('could not fetch result')
    finally:
        log.info('putback connection')
        POOL.putconn(conn)

    return res


def db_insup(query):
    conn = POOL.getconn()
    cur = conn.cursor()
    try:
        cur.execute("{}".format(query))
        conn.commit()
    except:
        log.error('could not execute query')
        return False
    finally:
        log.info('putback connection')
        POOL.putconn(conn)

    return True


def close_pool():
    try:
        POOL.closeall()
        log.info('db connection pool closed')
    except:
        log.exception('could not close db connection pools')
    return True
