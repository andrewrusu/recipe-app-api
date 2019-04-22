from model_mommy import mommy

import pytest

from rest_framework.test import APIClient


@pytest.fixture()
def api_client():
    '''Rest Framework's client class which extends Django's'''
    return APIClient()

# add basic support for numbers to model mommy


def gen_number(_next=[7788480000]):
    # use mutable arg as a sequence to avoid dupe numbers
    value = '+1 {}'.format(_next[0])
    _next[0] += 1
    return value


print("*******" * 20)
mommy.generators.add('phonenumber_field.modelfields.PhoneNumberField', gen_number)
