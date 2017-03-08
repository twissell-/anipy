import logging
from enum import Enum

from ..core import Resource

from ..utils import camelcase_to_underscore


logger = logging.getLogger(__name__)


def QueryFileld(setter):
    """
    This function decorates Query's setters to automatically populate ``_query`` dict.
    """

    _logger = logging.getLogger(__name__ + '.QueryField')

    def wrapper(self, *args):

        setter(self, *args)

        key = camelcase_to_underscore(setter.__name__)
        if isinstance(args[0], Enum):
            self._query[key] = args[0].value
        else:
            self._query[key] = args[0]

        _logger.debug('Query field changed: ' + str(self._query))

        return self

    return wrapper


class Browser(Resource):

    _ENDPOINT = '/browse/'

    def __init__(self):
        super().__init__()

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def executeQuery(self, query):
        self.get()


class Query(object):
    
    def __init__(self):
        self._query = {}

    @QueryFileld
    def year(self, value):
        self._year = value

    @QueryFileld
    def season(self, value):
        self._season = value

    @QueryFileld
    def type(self, value):
        """
        Use with MediaType Enum
        """
        self._type = value

    @QueryFileld
    def status(self, value):
        self._status = value

    # TODO: genres and genres_exlclude

    @QueryFileld
    def sort(self, value):
        self._sort = value

    @QueryFileld
    def airingData(self, value):
        """
        If true includes anime airing data in small models
        """
        self._airingData = value

    @QueryFileld
    def fullPage(self, value):
        self._fullPage = value

    @QueryFileld
    def page(self, value):
        self._page = value
        return self

