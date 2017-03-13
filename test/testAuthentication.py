from urllib3_mock import Responses

from anipy import (
    AuthenticationProvider,
)

import os

# from anipy.exception import AniException
# from anipy.exception import InternalServerError
# from anipy.exception import InvalidGrantException
# from anipy.exception import InvalidRequestException
# from anipy.exception import UnauthorizedException


class TestAuthentication(object):

    responses = Responses('requests.packages.urllib3')

    def testRefreshAuthentication(self):

        auth = AuthenticationProvider.currentAuth()

        assert auth.accessToken
        assert auth.expires
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.refreshToken == os.environ.get('REFRESH_TOKEN')
        assert not auth.isExpired
        assert auth is AuthenticationProvider.currentAuth()

    # @responses.activate
    # def testInternalServerError(self):
    #     TestAuthentication.responses.add(
    #         'POST', '/api/auth/access_token',
    #         status=500)
    #
    #     try:
    #         Authentication.fromCode('authenticationcode')
    #     except Exception as e:
    #         assert isinstance(e, InternalServerError)
    #     else:
    #         assert False
    #
    # @responses.activate
    # def testMethodNotAllowed(self):
    #     TestAuthentication.responses.add(
    #         'POST', '/api/auth/access_token',
    #         status=405)
    #
    #     try:
    #         Authentication.fromCode('authenticationcode')
    #     except Exception as e:
    #         assert isinstance(e, AniException)
    #         assert str(e) == 'HTTP 405 Method not allowed.'
    #     else:
    #         assert False
    #
    # @responses.activate
    # def testInvalidGrantException(self):
    #     TestAuthentication.responses.add(
    #         'POST', '/api/auth/access_token',
    #         body=b'{"error":"invalid_grant"}',
    #         status=400,
    #         content_type='application/json')
    #
    #     try:
    #         Authentication.fromCode('authenticationcode')
    #     except Exception as e:
    #         assert isinstance(e, InvalidGrantException)
    #     else:
    #         assert False
    #
    # @responses.activate
    # def testInvalidRequest(self):
    #     TestAuthentication.responses.add(
    #         'POST', '/api/auth/access_token',
    #         body=b'{"error":"invalid_request"}',
    #         status=400,
    #         content_type='application/json')
    #
    #     try:
    #         Authentication.fromCode('authenticationcode')
    #     except Exception as e:
    #         assert isinstance(e, InvalidRequestException)
    #     else:
    #         assert False
    #
    # @responses.activate
    # def testInvalidUnauthorizedException(self):
    #     TestAuthentication.responses.add(
    #         'POST', '/api/auth/access_token',
    #         body=b'{"error":"unauthorized"}',
    #         status=401,
    #         content_type='application/json')
    #
    #     try:
    #         Authentication.fromCode('authenticationcode')
    #     except Exception as e:
    #         assert isinstance(e, UnauthorizedException)
    #     else:
    #         assert False
