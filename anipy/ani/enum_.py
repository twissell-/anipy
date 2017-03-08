from enum import Enum


class SeriesType(Enum):
    """Enumeration for entry's list status."""
    manga = 'manga'
    anime = 'anime'


class ListStatus(Enum):
    """Enumeration for entry's list status."""
    watching = 'watching'
    reading = 'watching'
    completed = 'completed'
    onHold = 'on-hold'
    dropped = 'dropped'
    planToWatch = 'plan to watch'
    planToRead = 'plan to watch'
    # none = None # uncomments if errors

    def __str__(self):
        return self.value


class Smiley(Enum):
    """Enumeration for entry's 5 stars score."""

    like = ':)'
    neutral = ':|'
    unlike = ':('

    def __str__(self):
        return self.value


class Season(Enum):
    """Enumeration for entry's list status."""
    winter = 'winter'
    spring = 'spring'
    summer = 'summer'
    fall = 'fall'


class MediaType(Enum):
    tv = 0
    tvShort = 1
    movie = 2
    special = 3
    ova = 4
    ona = 5
    music = 6
    manga = 7
    novel = 8
    oneShot = 9
    doujin = 10
    manhua = 11
    manhwa = 12


class AnimeStatus(Enum):
    finishedAiring = 'finished airing'
    currentlyAiring = 'currently airing'
    notYetAired = 'not yet aired'
    cancelled = 'cancelled'


class MangaStatus(Enum):
    finishedPublishing = 'finished publishing'
    publishing = 'publishing'
    notYetPublished = 'not yet published'

# TODO: genres and genres_exclude goes here


class SortBy(Enum):
    id = 'id'
    score = 'score'
    popularity = 'popularity'
    startDate = 'start_date'
    endDate = 'end_date'

    @property
    def desc(self):
        return self.value + '-desc'

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value

