import os

from anipy import (
    AuthenticationProvider,
    Authentication
)

assert_msg = '\nActual: {actual}\nExpected: {expected}'

AuthenticationProvider.config(
    os.environ.get('CLIENT_ID'),
    os.environ.get('CLIENT_SECRET'),
    os.environ.get('CLIENT_REDIRECT_URI')
)

Authentication.fromRefreshToken(os.environ.get('REFRESH_TOKEN'))


def assertDataType(name, obj, cls):
    assert isinstance(obj, cls), '{name} ({value}) is {real}, not {expected}.'.format(
        name=name,
        value=obj,
        real=type(obj),
        expected=cls)