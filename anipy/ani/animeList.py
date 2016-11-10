import logging

from anipy.core import Resource
from anipy.utils import underscore_to_camelcase
from anipy.exception import raise_from_response
from anipy.ani.list import ListEntry
from anipy.ani.anime import SmallAnime

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
        super(AnimeListResource, self).__init__()

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

    def allByUserId(self):
        rtn = {}
        listsDic = self._requestByUserIdOrDisplayName(id_).json()[self._all_lists_key]
        for k, v in listsDic:
            rtn[underscore_to_camelcase(k)] = (ListEntry.fromResponse(item) for item in v)
        return rtn

    def update(self, entry):
        return self.put(data=entry.updateData)

    def create(self, entry):
        data = {
            'id': entry.anime.id,
            'list_status': entry.listStatus.value,
            'score': entry.score,
            'score_raw': entry.scoreRaw,
            'episodes_watched': entry.episodesWatched,
            'rewatched': entry.rewatched,
            'notes': entry.notes,
            'hidden_default': entry.hiddenDefault }

        response = requests.post(self._ENDPOINT, data=data, headers=self._headers)
        raise_from_response(response)

        return response

    def delete(self, entry):
        response = requests.delete(self._ENDPOINT + str(entry.anime.id), headers=self._headers)
        raise_from_response(response)

        return response

    def _listByUserIdAndListKey(self, id_, key):
        try:
            return list(AnimeListEntry.fromResponse(item) for item in self._requestByUserIdOrDisplayName(id_)[self._all_lists_key][key])
        except TypeError:
            logger.warning('User has no anime lists.')
            return []
        except KeyError:
            logger.warning('Anime list \'%s\' is empty.' % key)
            return []

    def _requestByUserIdOrDisplayName(self, displayName, raw=False):
        url = self._GET_ENDPOINT % str(displayName)
        if raw:
            url += 'raw'

        return self.get(endpoint=url)


class AnimeListEntry(ListEntry):
    """docstring for AnimeListEntry"""

    __composite__ = {'anime': SmallAnime}
    _animeListResource = AnimeListResource()

    def __init__(self, **kwargs):
        super(AnimeListEntry, self).__init__(**kwargs)
        self._anime = kwargs.get('anime', None)
        self._episodesWatched = kwargs.get('episodesWatched', 0)
        self._rewatched = kwargs.get('rewatched', 0)

        self._updateData = {
            'id': self._anime.id
        }

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
    def episodesWatched(self, episodesWatched):
        self._episodesWatched = episodesWatched
        self._updateData['episodes_watched'] = episodesWatched

    @rewatched.setter
    def rewatched(self, rewatched):
        self._rewatched = rewatched
        self._updateData['rewatched'] = rewatched
