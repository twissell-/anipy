from urllib3_mock import Responses
from datetime import datetime

from anipy import AuthenticationProvider
from anipy import Authentication
from anipy.exception import AniException
from anipy.exception import InternalServerError
from anipy.exception import InvalidGrantException
from anipy.exception import InvalidRequestException
from anipy.exception import UnauthorizedException


class TestAuthentication(object):

    responses = Responses('urllib3')
    AuthenticationProvider.config('clientId', 'clientSecret', 'redirectUri')

    @responses.activate
    def testValidAuthenticationFromCode(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"access_token":"anaccesstoken","token_type":"Bearer","expires_in":3600,"expires":9999999999,\
                "refresh_token":"refreshtoken"}',
            status=200,
            content_type='application/json')

        auth = Authentication.fromCode('authenticationcode')

        assert auth.accessToken == 'anaccesstoken'
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.refreshToken == 'refreshtoken'
        assert auth.expires == datetime.fromtimestamp(9999999999)
        assert not auth.isExpired
        assert auth is AuthenticationProvider.currentAuth()

    @responses.activate
    def testValidAuthenticationFromPin(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"access_token":"anaccesstoken","token_type":"Bearer","expires_in":3600,"expires":9999999999,\
                "refresh_token":"refreshtoken"}',
            status=200,
            content_type='application/json')

        auth = Authentication.fromPin('pin')

        assert auth.accessToken == 'anaccesstoken'
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.refreshToken == 'refreshtoken'
        assert auth.expires == datetime.fromtimestamp(9999999999)
        assert not auth.isExpired
        assert auth is AuthenticationProvider.currentAuth()

    @responses.activate
    def testValidAuthenticationCredentials(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"access_token":"anaccesstoken","token_type":"Bearer","expires_in":3600,"expires":9999999999}',
            status=200,
            content_type='application/json')

        auth = Authentication.fromCredentials()

        assert auth.accessToken == 'anaccesstoken'
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.expires == datetime.fromtimestamp(9999999999)
        assert not auth.isExpired
        assert auth is AuthenticationProvider.currentAuth()

    @responses.activate
    def testRefreshAuthentication(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"access_token":"anaccesstoken","token_type":"Bearer","expires_in":3600,"expires":9999999999,\
                "refresh_token":"refreshtoken"}',
            status=200,
            content_type='application/json')

        auth = Authentication.fromRefreshToken('refreshtoken')

        assert auth.accessToken == 'anaccesstoken'
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.refreshToken == 'refreshtoken'
        assert auth.expires == datetime.fromtimestamp(9999999999)
        assert not auth.isExpired
        assert auth is AuthenticationProvider.currentAuth()

    @responses.activate
    def testInternalServerError(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            status=500)

        try:
            Authentication.fromCode('authenticationcode')
        except Exception as e:
            assert isinstance(e, InternalServerError)
        else:
            assert False

    @responses.activate
    def testMethodNotAllowed(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            status=405)

        try:
            Authentication.fromCode('authenticationcode')
        except Exception as e:
            assert isinstance(e, AniException)
            assert str(e) == 'HTTP 405 Method not allowed.'
        else:
            assert False

    @responses.activate
    def testInvalidGrantException(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"error":"invalid_grant"}',
            status=400,
            content_type='application/json')

        try:
            Authentication.fromCode('authenticationcode')
        except Exception as e:
            assert isinstance(e, InvalidGrantException)
        else:
            assert False

    @responses.activate
    def testInvalidRequest(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"error":"invalid_request"}',
            status=400,
            content_type='application/json')

        try:
            Authentication.fromCode('authenticationcode')
        except Exception as e:
            assert isinstance(e, InvalidRequestException)
        else:
            assert False

    @responses.activate
    def testInvalidGrantException(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"error":"unauthorized"}',
            status=401,
            content_type='application/json')

        try:
            Authentication.fromCode('authenticationcode')
        except Exception as e:
            assert isinstance(e, UnauthorizedException)
        else:
            assert False
