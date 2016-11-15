from urllib3_mock import Responses
from datetime import datetime

from anipy import AuthenticationProvider
from anipy import Authentication


class TestAuthentication(object):

    responses = Responses('urllib3')

    @responses.activate
    def testValidAuthentication(self):
        TestAuthentication.responses.add(
            'POST', '/api/auth/access_token',
            body=b'{"access_token":"anaccesstoken","token_type":"Bearer","expires_in":3600,"expires":9999999999}',
            status=200,
            content_type='application/json')

        AuthenticationProvider.config('clientId', 'clientSecret', 'redirectUri')

        auth = Authentication.fromCode('authenticationcode')

        assert auth.accessToken == 'anaccesstoken'
        assert auth.tokenType == 'Bearer'
        assert auth.expiresIn == 3600
        assert auth.expires == datetime.fromtimestamp(9999999999)
        assert not auth.isExpired


