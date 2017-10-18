import logging


class DCCHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(DCCHandler, self).__init__(stream)

    def emit(self, record):
        msg = self.format(record)
