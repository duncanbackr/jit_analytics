import pytest
import Format
from Tests.test_formating.fixtures import \
    proccessed_comments_1, formated_comments_1, processed_reply_1,\
    formated_comments_1_with_reply

def test_reformat_comments(proccessed_comments_1, formated_comments_1):
    assert Format.comments(proccessed_comments_1, {}) == formated_comments_1

def test_reformat_comments_with_reply(proccessed_comments_1, \
    processed_reply_1, formated_comments_1_with_reply):
    assert Format.comments(proccessed_comments_1, processed_reply_1) == formated_comments_1_with_reply
