import  Formating
from Tests.test_formating.fixtures import \
    proccessed_comments_1, formated_comments_1, processed_reply_1,\
    formated_comments_1_with_reply
import pytest


def test_reformat_comments(proccessed_comments_1, formated_comments_1):
    assert  Formating.comments(proccessed_comments_1, {}, {}, False, 0, 100) == formated_comments_1

def test_reformat_comments_with_reply(proccessed_comments_1, \
    processed_reply_1, formated_comments_1_with_reply):
    assert  Formating.comments(proccessed_comments_1, processed_reply_1, {}, False, 0, 100) == formated_comments_1_with_reply
