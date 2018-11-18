# -*- coding: utf-8 -*-
import os
import sys

import psycopg2
from psycopg2.pool import ThreadedConnectionPool

from achlib.config import file_config
from achlib.util import logger, timit

log = logger.getLogger(__name__)
config = file_config()

'''
POOL = ThreadedConnectionPool(1,100, dbname=config.get('DB','dbname'), \
       user=config.get('DB','user'), password=config.get('DB','pswd'), \
       host=config.get('DB','host') , port=config.get('DB','port'))
'''

def db_connect():
    try:
        log.info('connecting to database')
        conn = psycopg2.connect(dbname=config.get('DB','dbname'), \
               user=config.get('DB','user'), password=config.get('DB','pswd'), \
               host=config.get('DB','host') , port=config.get('DB','port'))
        return conn
    except:
        log.exception('cannot connect to db')

@timit
def db_fetch(query, fetch='all'):
    conn = db_connect()
    cur = conn.cursor()
    try:
        cur.execute("{}".format(query))
        log.info('querry executed')
        if fetch=='all':
            res = cur.fetchall()
        else:
            res = cur.fetchmany(fetch)
    except:
        log.error('could not fetch result')
        raise
    finally:
        log.info('connection terminated')
        conn.close()

    return res


@timit
def db_insup(query):
    conn = db_connect()
    cur = conn.cursor()
    try:
        cur.execute("{}".format(query))
        conn.commit()
        log.info('querry executed and commited')
    except:
        log.error('could not execute query')
        raise
    finally:
        log.info('connection terminated')
        conn.close()

    return True

@timit
def generate_device_key():
    conn = db_connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT nextval('device_key_seq')")
        res = cur.fetchall()
        log.info('device key generated')
    except:
        log.error('could not fetch result')
        raise
    finally:
        log.info('connection terminated')
        conn.close()

    return res[0][0]

'''
def close_pool():
    try:
        POOL.closeall()
        log.info('db connection pool closed')
    except:
        log.exception('could not close db connection pools')
    return True
'''
