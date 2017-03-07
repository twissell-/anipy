import logging
from enum import Enum

from ..core import Resource
from ..utils import camelcase_to_underscore


logger = logging.getLogger(__name__)


class QueryFileld(object):
    """
    This class decorates Browser's setters to automatically populate ``_query`` dict.
    """

    _logger = logging.getLogger(__name__ + '.QueryField')

    def __init__(self, setter):
        self._setter = setter
        self._key = camelcase_to_underscore(self._setter.__name__)
        self._logger.debug('Query field created: ' + self._setter.__name__)

    def __call__(self, *args):
        self._setter(*args)
        if isinstance(args[1], Enum):
            args[0]._query[self._key] = args[1].value
        else:
            args[0]._query[self._key] = args[1]

        self._logger.debug('Query field changed: ' + str(args[0].updateData))


class Browser(Resource):

    _ENDPOINT = '/browse/'
    _DESC = '-desc'

    def __init__(self):
        super().__init__()
        self._query = {}
        self._isAsc = True

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    @property
    def query(self):
        if self.isAsc is False and self.sort:
            self.sort += Browser._DESC
        return self._query

    @property
    def year(self):
        return self._year

    @year.setter
    @QueryFileld
    def year(self, value):
        self._year = value

    @property
    def season(self):
        return self._season

    @season.setter
    @QueryFileld
    def season(self, value):
        self._season = value

    @property
    def mediaType(self):
        return self._mediaType

    @mediaType.setter
    @QueryFileld
    def mediaType(self, value):
        self._mediaType = value

    @property
    def status(self):
        return self._status

    @status.setter
    @QueryFileld
    def status(self, value):
        self._status = value

    # TODO: genres and genres_exlclude

    @property
    def sort(self):
        return self._sort

    @sort.setter
    @QueryFileld
    def sort(self, value):
        self._sort = value

    @property
    def isAsc(self):
        return self._isAsc

    @isAsc.setter
    def isAsc(self, value):
        self._isAsc = value

    @property
    def airingData(self):
        """
        If true includes anime airing data in small models
        """
        return self._airingData

    @airingData.setter
    @QueryFileld
    def airingData(self, value):
        self._airingData = value

    @property
    def fullPage(self):
        """
        If true returns all available results. Ignores pages.
        Only available when status is "Currently Airing" or season is included
        """
        return self._fullPage

    @fullPage.setter
    @QueryFileld
    def fullPage(self, value):
        self._fullPage = value

    @property
    def page(self):
        return self._page

    @page.setter
    @QueryFileld
    def page(self, value):
        self._page = value