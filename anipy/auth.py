import requests

from abc import ABCMeta
from abc import abstractmethod
from enum import Enum
from datetime import datetime

from anipy.exception import raise_from_respose

_URL = 'https://anilist.co/api/auth/access_token'

class GrantType(Enum):
    """Enum for Authentication grant type."""
    authorizationCode = 'authorization_code'
    authorizationPin = 'authorization_pin'
    clientCredentials = 'client_credentials'
    refreshToken = 'refresh_token'

class Authentication(object):
    """Represents a Anilist authentication response """

    def __init__(self, response=None, dic=None, **kwargs):
        super(Authentication, self).__init__()

        if not response is None:
            kwargs = response.json()
        elif not dic is None:
            kwargs = dic

        self._accessToken = kwargs.get('access_token', None)
        self._tokenType = kwargs.get('token_type', None)
        self._expiresIn = kwargs.get('expires_in', None)
        self._refreshToken = kwargs.get('refresh_token', None)
        exp = kwargs.get('expires', None)
        self._expires = exp if exp is None else datetime.fromtimestamp(exp)

    def refresh(self):
        newAuth = AuthenticationProvider.getInstance().refresh(self.refreshToken)
        self._accessToken = newAuth.accessToken
        self._tokenType = newAuth.tokenType
        self._expiresIn = newAuth.expiresIn
        self._expires = newAuth.expires

    @classmethod
    def provider(cls, grantType):
        return AuthenticationProvider(grantType)

    @property
    def accessToken(self):
        return self._accessToken

    @property
    def tokenType(self):
        return self._tokenType

    @property
    def expires(self):
        return self._expires

    @property
    def expiresIn(self):
        return self._expiresIn

    @property
    def refreshToken(self):
        return self._refreshToken

    def isExpired(self):
        return self.expires < datetime.now()


class AuthenticationProvider(object):
    """AuthenticationProvider(GrantType) -> Authentication.

    (Singleton) Builder for the Authentication class"""

    clientId = None
    clientSecret = None
    redirectUri = None

    def __new__(type, grantType):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def __init__(self, grantType):
        super(AuthenticationProvider, self).__init__()

        self._grantType = grantType
        if grantType is GrantType.authorizationCode:
            self.authenticate = self._codeRequest
        elif grantType is GrantType.authorizationPin:
            self.authenticate = self._pinRequest
        elif grantType is GrantType.clientCredentials:
            self.authenticate = self._clientCredentialsRequest
        elif grantType is GrantType.refreshToken:
            self.authenticate = self._refreshRequest
        else:
            raise ValueError('Invalid grant type.')

    @classmethod
    def config(cls, clientId, clientSecret, redirectUri):
        cls.clientId = clientId
        cls.clientSecret = clientSecret
        cls.redirectUri = redirectUri

    @classmethod
    def getInstance(cls):
        return cls._instance

    def refresh(self, refreshToken, clientId=None, clientSecret=None):
        return self._refreshRequest(refreshToken, clientId, clientSecret)

    def _refreshRequest(self, refreshToken, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        print(refreshToken)
        url = _URL
        data = {
            'grant_type': GrantType.refreshToken.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'refresh_token': refreshToken}

        response = requests.post(url, data=data)

        if response.status_code != 200:
            raise_from_respose(response)

        dicResponse = response.json()
        dicResponse['refresh_token'] = refreshToken

        return Authentication(dic=dicResponse)

    def _codeRequest(self, code, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        url = _URL
        data = {
            'grant_type': GrantType.authorizationCode.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': code}

        response = requests.post(url, data=data)

        if response.status_code != 200:
            raise_from_respose(response)

        return Authentication(response=response)

    def _pinRequest(self, pin, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        url = _URL
        data = {
            'grant_type': GrantType.authorizationPin.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': pin}

        response = requests.post(url, data=data)

        if response.status_code != 200:
            raise_from_respose(response)

        return Authentication(response=response)

    def _clientCredentialsRequest(self, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret

        url = _URL
        data = {
            'grant_type': 'client_credentials',
            'client_id': clientId,
            'client_secret': clientSecret}

        response = requests.post(url, data=data)

        if response.status_code != 200:
            raise_from_respose(response)

        return Authentication(response=response)
