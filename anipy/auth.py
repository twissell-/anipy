import requests
import json
import logging

from enum import Enum
from datetime import datetime

BASE_URL = 'https://anilist.co/api/'
CLIENT_ID = 'demo-vfxpa'
CLIENT_SECRET = 'mpnPS782wW47vwRMVOUQYJ6w0XszH'


class GrantType(Enum):
    """Enum for Authorization grant type."""
    authorizationCode = 'authorization_code'
    authorizationPin = 'authorization_pin'
    clientCredentials = 'client_credentials'

class Authorization(object):
    """Represents a response """

    def __init__(self, **kwargs):
        super(Authorization, self).__init__()
        self._accessToken = kwargs.get('accessToken', None)
        self._tokenType = kwargs.get('tokenType', None)
        self._expiresIn = kwargs.get('expiresIn', None)
        self._refreshToken = kwargs.get('refreshToken', None)
        exp = kwargs.get('expires', None)
        if exp is None:
            self._expires = exp
        else:
            self._expires = datetime.fromtimestamp(exp)

    @property
    def accessToken(self):
        return self._accessToken

    @accessToken.setter
    def accessToken(self, accessToken):
        self._accessToken = accessToken

    @property
    def tokenType(self):
        return self._tokenType

    @tokenType.setter
    def tokenType(self, tokenType):
        self._tokenType = tokenType

    @property
    def expires(self):
        return self._expires

    @expires.setter
    def expires(self, expires):
        self._expires = expires

    @property
    def expiresIn(self):
        return self._expiresIn

    @expiresIn.setter
    def expiresIn(self, expiresIn):
        self._expiresIn = expiresIn

    @property
    def refreshToken(self):
        return self._refreshToken

    @refreshToken.setter
    def refreshToken(self, refreshToken):
        self._refreshToken = refreshToken

class AuthorizationBuilder(object):
    """AuthorizationBuilder(GrantType) -> a initialized authorization.

    Builder for the Authorization class"""
    def __init__(self, grantType):
        super(AuthorizationBuilder, self).__init__()

        if grantType is GrantType.authorizationCode:
            self.build = self._codeBuilder
        elif grantType is GrantType.authorizationPin:
            self.build = self._pinBuilder
        elif grantType is GrantType.clientCredentials:
            self.build = self._clientCredentialsBuilder


    def _codeBuilder(self):
        pass

    def _pinBuilder(self):
        pass

    def _clientCredentialsBuilder(self):
        url = BASE_URL + 'auth/access_token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET}

        try:
            response = requests.post(url, data=data).json()
        except Exception as e:
            # TODO: manage this error.
            raise e

        # TODO: Validate response status code. (must be 200)

        return Authorization(
            expiresIn=response.get('expires_in', None), 
            accessToken=response.get('access_token', None), 
            expires=response.get('expires', None), 
            tokenType=response.get('token_type', None))
