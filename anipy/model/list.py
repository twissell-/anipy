import requests

from anipy.utils import underscore_to_camelcase


class ListEntry(object):
    """docstring for ListEntry"""
    def __init__(self, dic=None, **kwargs):
        super(ListEntry, self).__init__()
        if not dic is None:
            kwargs = dic

        self._recordId = kwargs.get('recordId', None)
        self._listStatus = kwargs.get('listStatus', None)
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
