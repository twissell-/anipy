import requests
import json
import urllib3
import logging
import pprint

from enum import Enum
from datetime import datetime
from abc import ABCMeta

from anipy.utils import underscore_to_camelcase
from anipy.utils import dic_to_json
from anipy.utils import response_to_dic
from anipy.exception import raise_from_respose
from anipy.exception import NotAuthenticatedException

logger = logging.getLogger(__name__)


class Resource(object):
    """
    Abstract resource class. 

    Works as a base class for all other resources, keeping the generic and re-usable functionality
    """

    _URL = 'http://anilist.co'

    def __init__(self):
        super(Resource, self).__init__()
        self._pool = urllib3.connectionpool.connection_from_url(Resource._URL, maxsize=5)

    @property
    def _headers(self):
        auth = AuthenticationProvider.currentAuth()

        return {
            'Authorization': '%s %s' % (auth.tokenType, auth.accessToken),
            'Content-Type': 'application/json'}

    def request(self, method, endpoint=None, data=None, headers=None):
        headers = self._headers if headers is None else headers
        endpoint = self._ENDPOINT if endpoint is None else endpoint
        data = dic_to_json(data)

        logger.debug('Resource request: %s %s' % (method, endpoint))
        logger.debug('Resource request body: %s' % str(data))
        logger.debug('Resource request headers: %s' % ((headers)))

        response = self._pool.request(
            method,
            endpoint,
            body=data,
            headers=headers)
        raise_from_respose(response)

        response = response_to_dic(response)
        logger.debug('Resource response: \n' + pprint.pformat(response))
        return response

    def get(self, endpoint=None, data=None):
        return self.request('GET', endpoint=endpoint, data=data)

    def post(self, endpoint=None, data=None):
        return self.request('POST', endpoint=endpoint, data=data)

    def put(self, endpoint=None, data=None):
        return self.request('PUT', endpoint=endpoint, data=data)

    def delete(self, endpoint=None, data=None):
        return self.request('DELETE', endpoint=endpoint, data=data)


class Entity(metaclass=ABCMeta):
    """Abstract base class for al classes that are mapped from/to an anilist response."""

    __composite__ = {}

    def __init__(self, **kwargs):
        super(Entity, self).__init__()

    @classmethod
    def fromResponse(cls, response):

        if isinstance(response, requests.Response):
            response = response.json()
        dic = {}

        for k in response:
            if k in cls.__composite__:
                dic[underscore_to_camelcase(k)] = cls.__composite__[k].fromResponse(response.get(k))
            else:
                dic[underscore_to_camelcase(k)] = response.get(k, None)

        return cls(**dic)


class GrantType(Enum):
    """Enum for Authentication grant type."""
    authorizationCode = 'authorization_code'
    authorizationPin = 'authorization_pin'
    clientCredentials = 'client_credentials'
    refreshToken = 'refresh_token'


class AuthenticationProvider(object):
    """
    (Singleton) Builder for the Authentication class
    """

    _URL = 'http://anilist.co'
    _ENDPOINT = '/api/auth/access_token'
    _pool = urllib3.connectionpool.connection_from_url(_URL)

    clientId = None
    clientSecret = None
    redirectUri = None

    _logger = logging.getLogger(__name__ + '.AuthenticationProvider')


    def __new__(type, grantType):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def __init__(self, grantType):
        super(AuthenticationProvider, self).__init__()

        self._grantType = grantType
        self._currentAuth = None
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
    def currentAuth(cls):
        auth = cls._instance._currentAuth
        if  auth is None:
            raise NotAuthenticatedException('Current authentication is None.')

        return auth

    @classmethod
    def refresh(cls, refreshToken, clientId=None, clientSecret=None):
        return cls._instance._refreshRequest(refreshToken, clientId, clientSecret)

    def _authRequest(self, data ):
        self._logger.debug('Auth request: \n' + pprint.pformat(data))
        response = self._pool.request(
            'POST',
            self._ENDPOINT,
            fields=data)
        raise_from_respose(response)

        response = response_to_dic(response)
        if data.get('refresh_token') is not None:
            response['refresh_token'] = data.get('refresh_token')

        auth = Authentication(**response)
        self._currentAuth = auth

        self._logger.debug('Auth response: \n' + pprint.pformat(response))
        return auth

    def _refreshRequest(self, refreshToken, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret

        data = {
            'grant_type': GrantType.refreshToken.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'refresh_token': refreshToken}

        return self._authRequest(data)

    def _codeRequest(self, code, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        data = {
            'grant_type': GrantType.authorizationCode.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': code}

        return self._authRequest(data)


    def _pinRequest(self, pin, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        data = {
            'grant_type': GrantType.authorizationPin.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': pin}

        return self._authRequest(data)

    def _clientCredentialsRequest(self, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret

        data = {
            'grant_type': GrantType.clientCredentials.value,
            'client_id': clientId,
            'client_secret': clientSecret}

        return self._authRequest(data)


class Authentication(object):
    """
    Represents a Anilist authentication response.
    """

    def __init__(self, **kwargs):
        super(Authentication, self).__init__()
        self._accessToken = kwargs.get('access_token', None)
        self._tokenType = kwargs.get('token_type', None)
        self._expiresIn = kwargs.get('expires_in', None)
        self._refreshToken = kwargs.get('refresh_token', None)
        exp = kwargs.get('expires', None)
        self._expires = exp if exp is None else datetime.fromtimestamp(exp)

    @classmethod
    def fromCode(cls, code, clientId=None, clientSecret=None, redirectUri=None):
        return AuthenticationProvider(
            GrantType.authorizationCode).authenticate(code, clientId, clientSecret, redirectUri)

    @classmethod
    def fromPin(cls, pin, clientId=None, clientSecret=None, redirectUri=None):
        return AuthenticationProvider(
            GrantType.authorizationPin).authenticate(pin, clientId, clientSecret)

    @classmethod
    def fromCredentials(cls, clientId=None, clientSecret=None):
        return AuthenticationProvider(
            GrantType.clientCredentials).authenticate(clientId, clientSecret)

    @classmethod
    def fromRefreshToken(cls, refreshToken, clientId=None, clientSecret=None):
        return AuthenticationProvider(GrantType.refreshToken).authenticate(refreshToken)

    def refresh(self):
        newAuth = AuthenticationProvider.refresh(self.refreshToken)
        self._accessToken = newAuth.accessToken
        self._tokenType = newAuth.tokenType
        self._expiresIn = newAuth.expiresIn
        self._expires = newAuth.expires

    def __repr__(self):
        return '<%s \'%s\' %s>' % (
            self.__class__.__name__, 
            self.accessToken,
            'Expired' if self.isExpired else 'Not expired')

    @property
    def isExpired(self):
        return self.expires < datetime.now()

    @property
    def accessToken(self):
        if self.isExpired:
            self.refresh()

        return self._accessToken

    @property
    def tokenType(self):
        return self._tokenType.capitalize()

    @property
    def expires(self):
        return self._expires

    @property
    def expiresIn(self):
        return self._expiresIn

    @property
    def refreshToken(self):
        return self._refreshToken
