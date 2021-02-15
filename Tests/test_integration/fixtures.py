import pytest

class Flask_Request:
    def __init__(self, request_dict):
        self.args = request_dict
        self.method = 'Not OPTIONS'