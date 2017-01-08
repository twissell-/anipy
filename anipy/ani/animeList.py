import logging

from anipy.core import Resource
from anipy.core import Updatable
from anipy.utils import underscore_to_camelcase
from anipy.ani.list import ListEntry
from anipy.ani.serie import SmallAnime

logger = logging.getLogger(__name__)


class AnimeListResource(Resource):
    """docstring for AnimeListResource"""

    _GET_ENDPOINT = '/api/user/%s/animelist/'
    _ENDPOINT = '/api/animelist/'
    
    _all_lists_key = 'lists'
    _watching_key = 'watching'
    _completed_key = 'completed'
    _on_hold_key = 'on_hold'
    _dropped_key = 'dropped'
    _plan_to_watch_key = 'plan_to_watch'

    def __init__(self):
        super().__init__()

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def watchingByUserId(self, id_):
        return self._listByUserIdAndListKey(id_, self._watching_key)

    def completedByUserId(self, id_):
        return self._listByUserIdAndListKey(id_, self._completed_key)

    def onHoldByUserId(self, id_):
        return self._listByUserIdAndListKey(id_, self._on_hold_key)

    def droppedgByUserId(self, id_):
        return self._listByUserIdAndListKey(id_, self._dropped_key)

    def planToWatchByUserId(self, id_):
        return self._listByUserIdAndListKey(id_, self._plan_to_watch_key)

    def allByUserId(self, id_):
        rtn = {}
        listsDic = self._requestByUserIdOrDisplayName(id_).json()[self._all_lists_key]
        for k, v in listsDic:
            rtn[underscore_to_camelcase(k)] = (ListEntry.fromResponse(item) for item in v)
        return rtn

    def _listByUserIdAndListKey(self, id_, key):
        try:
            return list(AnimeListEntry.fromResponse(item) for item in self._requestByUserIdOrDisplayName(id_)[self._all_lists_key][key])
        except TypeError as e:
            logger.warning('User has no anime lists.')
            logger.debug(e)
            return []
        except KeyError as e:
            logger.warning('Anime list \'%s\' is empty.' % key)
            logger.debug(e)
            return []

    def _requestByUserIdOrDisplayName(self, displayName, raw=False):
        url = self._GET_ENDPOINT % str(displayName)
        if raw:
            url += 'raw'

        return self.get(endpoint=url)


class AnimeListEntry(ListEntry):
    """docstring for AnimeListEntry"""

    __composite__ = {'anime': SmallAnime}
    _resource = AnimeListResource()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._anime = kwargs.get('anime')
        self._episodesWatched = kwargs.get('episodesWatched', 0)
        self._rewatched = kwargs.get('rewatched', 0)

        self._updateData['id'] = self._anime.id

    def __repr__(self):
        return '<%s \'%s\' %d>' % (
            self.__class__.__name__,
            self.anime.titleRomaji,
            self.episodesWatched)

    @property
    def anime(self):
        return self._anime

    @property
    def episodesWatched(self):
        return self._episodesWatched

    @property
    def rewatched(self):
        return self._rewatched

    @anime.setter
    def anime(self, anime):
        self._anime = anime

    @episodesWatched.setter
    @Updatable
    def episodesWatched(self, episodesWatched):
        self._episodesWatched = episodesWatched

    @rewatched.setter
    @Updatable
    def rewatched(self, rewatched):
        self._rewatched = rewatched
