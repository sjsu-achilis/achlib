# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import json
import requests
import socket

from synthetic.config import file_config
from synthetic.util import logger

log = logger.getLogger(__name__)
config = file_config()

SLACK_URL = config.get('URL','slack_hook')

class SlackPost(object):
    def __init__(self):
        self.name = "#synmon"

    def write(self, x):
        self.post(x)

    def post(self, text, username="synbot"):
        channel = self.name
        text = text.strip()
        if not text: return
        post_json = {
            "channel": channel,
            "username": username,
            "text": text
        }

        try:
            headers = {'content-type': 'application/json'}
            requests = urllib2.Request(SLACK_URL, json.dumps(post_json),headers)
            x=urllib2.urlopen(requests)
            y = x.read()
        except urllib2.HTTPError as e:
            y = e.read()
        if y != "ok":
            raise ValueError(y)
        return

if __name__ == '__main__':
    slack_poster = SlackPost()
    slack_poster.post(sys.argv[2])
