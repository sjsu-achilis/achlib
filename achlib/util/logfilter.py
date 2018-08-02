# -*- coding: utf-8 -*-
import uuid
from logging import Filter

class FlaskLogFilter(Filter):
    def __init__(self, flask, **kwargs):
        super(FlaskLogFilter, self).__init__(**kwargs)
        self.flask = flask

    def filter(self, record):
        # check if inside request context
        if not self.flask.request:
            record.request_id = ""
            return True

        # check incoming request id
        incoming_request_id = self.flask.request.headers.get("X-Request-Id")
        if incoming_request_id:
            record.request_id = incoming_request_id
            return True

        # ref. http://flask.pocoo.org/docs/0.12/api/#application-globals
        # check stored request id
        stored_request_id = self.flask.g.get("request_id")
        if stored_request_id:
            record.request_id = stored_request_id
            return True

        # generate and store request id
        record.request_id = self.flask.g.request_id = str(uuid.uuid4())
        return True
