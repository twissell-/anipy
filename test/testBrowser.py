from . import assert_msg

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

    def testQuery(self):

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

        query = Query(SeriesType.anime)
        query\
            .year(2014)\
            .season(Season.fall)\
            .type(MediaType.tv)\
            .status(AnimeStatus.finishedAiring)\
            .sort(SortBy.popularity.desc)\
            .airingData(False).fullPage(False).page(1)

        assert query.query == expected, \
            assert_msg.format(actual=query.query, expected=expected)
        assert query.serieType == SeriesType.anime, \
            assert_msg.format(actual=query.serieType, expected=SeriesType.anime)

    def testBrowser(self, ):

        browser = Browser()
        browser.executeQuery(Query(SeriesType.anime))
