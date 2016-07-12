import requests

from enum import Enum

from anipy.core import Resource
from anipy.utils import underscore_to_camelcase
from anipy.exception import raise_from_respose


class ListStatus(Enum):
    """Enumeration for entry's list status."""
    watching = 'watching'
    completed = 'completed'
    onHold = 'on-hold'
    dropped = 'dropped'
    planToWatch = 'plan to watch'
    # none = None # uncomments if errors

class AnimeListResource(Resource):
    """docstring for AnimeListResource"""

    _all_lists_key = 'lists'
    _watching_key = 'watching'
    _completed_key = 'completed'
    _on_hold_key = 'on_hold'
    _dropped_key = 'dropped'
    _plan_to_watch_key = 'plan_to_watch'

    def __init__(self):
        super(AnimeListResource, self).__init__()
        self._getUrl = self._baseUrl + 'user/%s/animelist/'
        self._postUrl = self._baseUrl + 'animelist/'

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
        data = {
            'id': entry.anime.id,
            'list_status': entry.listStatus.value
            'score': entry.score
            'score_raw': entry.scoreRaw
            'episodes_watched': entry.episodesWatched
            'rewatched': entry.rewatched
            'notes': entry.notes
            'advanced_rating_scores': entry.advancedRatingScores
            'custom_lists': entry.customLists
            'hidden_default': entry.hiddenDefault }

        response = requests.put(self._postUrl, data=data, headers=self._headers)
        raise_from_respose(response)

        return response

    def create(self, entry):
        data = {
            'id': entry.anime.id,
            'list_status': entry.listStatus.value
            'score': entry.score
            'score_raw': entry.scoreRaw
            'episodes_watched': entry.episodesWatched
            'rewatched': entry.rewatched
            'notes': entry.notes
            'advanced_rating_scores': entry.advancedRatingScores
            'custom_lists': entry.customLists
            'hidden_default': entry.hiddenDefault }

        response = requests.post(self._postUrl, data=data, headers=self._headers)
        raise_from_respose(response)

        return response

    def create(self, entry):
        data = {
            'id': entry.anime.id,
            'list_status': entry.listStatus.value
            'score': entry.score
            'score_raw': entry.scoreRaw
            'episodes_watched': entry.episodesWatched
            'rewatched': entry.rewatched
            'notes': entry.notes
            'advanced_rating_scores': entry.advancedRatingScores
            'custom_lists': entry.customLists
            'hidden_default': entry.hiddenDefault }

        response = requests.post(self._postUrl, data=data, headers=self._headers)
        raise_from_respose(response)

        return response

    def delete(self, entry):
        response = requests.delete(self._postUrl + str(entry.anime.id), headers=self._headers)
        raise_from_respose(response)

        return response

    def _listByUserIdAndListKey(self, id_, key):
        return list(ListEntry.fromResponse(item) for item in self._requestByUserIdOrDisplayName(id_).json()[self._all_lists_key][key])

    def _requestByUserIdOrDisplayName(self, displayName, raw=False):
        url = self._getUrl % str(displayName)
        if raw:
            url += 'raw'

        response = requests.get(self._getUrl % displayName, headers=self._headers)
        raise_from_respose(response)

        return response

class ListEntry(object):
    """docstring for ListEntry"""

    _animeListResource = AnimeListResource()

    def __init__(self, dic=None, **kwargs):
        super(ListEntry, self).__init__()
        if not dic is None:
            kwargs = dic

        listStatus = kwargs.get('listStatus', None)
        if not isinstance(listStatus, ListStatus and not listStatus is None):
            listStatus = ListStatus(listStatus)

        self._recordId = kwargs.get('recordId', None)
        self._listStatus = listStatus
        self._score = kwargs.get('score', None)
        self._priorty = kwargs.get('priorty', None)
        self._rewatched = kwargs.get('rewatched', None)
        self._notes = kwargs.get('notes', None)
        self._private = kwargs.get('private', None)
        self._updatedTime = kwargs.get('updatedTime', None)
        self._addedTime = kwargs.get('addedTime', None)
        self._scoreRaw = kwargs.get('scoreRaw', None)
        self._advancedRatingScores = kwargs.get('advancedRatingScores', None)
        self._episodesWatched = kwargs.get('episodesWatched', None)
        self._chaptersRead = kwargs.get('chaptersRead', None)
        self._volumesRead = kwargs.get('volumesRead', None)
        self._hiddenDefault = kwargs.get('hiddenDefault', None)
        self._customLists = kwargs.get('customLists', None)
        self._anime = kwargs.get('anime', None)

    @classmethod
    def fromResponse(cls, response):
        if isinstance(response, requests.Response):
            response = response.json()
        dic = {}

        for k in response:
            if k == 'anime':
                dic[k] = SmallAnime.fromResponse(response.get(k))
            else:
                dic[underscore_to_camelcase(k)] = response.get(k, None)

        return cls(dic=dic)

    @property
    def save(self):
        self._animeListResource(self)

    @property
    def recordId(self):
        return self._recordId
    
    @recordId.setter
    def recordId(self, recordId):
        self._recordId = recordId

    @property
    def listStatus(self):
        return self._listStatus
    
    @listStatus.setter
    def listStatus(self, listStatus):
        self._listStatus = listStatus

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    @property
    def priorty(self):
        return self._priorty
    
    @priorty.setter
    def priorty(self, priorty):
        self._priorty = priorty

    @property
    def rewatched(self):
        return self._rewatched
    
    @rewatched.setter
    def rewatched(self, rewatched):
        self._rewatched = rewatched

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, notes):
        self._notes = notes

    @property
    def private(self):
        return self._private
    
    @private.setter
    def private(self, private):
        self._private = private

    @property
    def updatedTime(self):
        return self._updatedTime
    
    @updatedTime.setter
    def updatedTime(self, updatedTime):
        self._updatedTime = updatedTime

    @property
    def addedTime(self):
        return self._addedTime
    
    @addedTime.setter
    def addedTime(self, addedTime):
        self._addedTime = addedTime

    @property
    def scoreRaw(self):
        return self._scoreRaw
    
    @scoreRaw.setter
    def scoreRaw(self, scoreRaw):
        self._scoreRaw = scoreRaw

    @property
    def advancedRatingScores(self):
        return self._advancedRatingScores
    
    @advancedRatingScores.setter
    def advancedRatingScores(self, advancedRatingScores):
        self._advancedRatingScores = advancedRatingScores

    @property
    def episodesWatched(self):
        return self._episodesWatched
    
    @episodesWatched.setter
    def episodesWatched(self, episodesWatched):
        self._episodesWatched = episodesWatched

    @property
    def chaptersRead(self):
        return self._chaptersRead
    
    @chaptersRead.setter
    def chaptersRead(self, chaptersRead):
        self._chaptersRead = chaptersRead

    @property
    def volumesRead(self):
        return self._volumesRead
    
    @volumesRead.setter
    def volumesRead(self, volumesRead):
        self._volumesRead = volumesRead

    @property
    def hiddenDefault(self):
        return self._hiddenDefault
    
    @hiddenDefault.setter
    def hiddenDefault(self, hiddenDefault):
        self._hiddenDefault = hiddenDefault

    @property
    def customLists(self):
        return self._customLists
    
    @customLists.setter
    def customLists(self, customLists):
        self._customLists = customLists

    @property
    def anime(self):
        return self._anime
    
    @anime.setter
    def anime(self, anime):
        self._anime = anime
