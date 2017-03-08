
from anipy import (
    Browser,
    Query
)

from anipy.ani.enum_ import (
    Season,
    MediaType,
    SeriesType,
    AnimeStatus,
    MangaStatus,
    SortBy
)


class TestBrowser(object):

    def TestQuery(self):

        expected = {
            'year': 2014,
            'season': 'fall',
            'type': 0,
            'status': 'finished airing',
            'sort': 'popularity-desc',
            'airing_data': False,
            'full_page': False,
            'page': 1
        }


        query = Query()
        query\
            .year(2014)\
            .season(Season.fall)\
            .type(MediaType.tv)\
            .status(AnimeStatus.finishedAiring)\
            .sort(SortBy.popularity.desc)\
            .airingData(False).fullPage(False).page(1)

        print(query._query)
        print(expected)

        assert query._query == expected
