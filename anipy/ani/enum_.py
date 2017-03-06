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