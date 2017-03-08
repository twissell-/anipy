from .core import (
    Authentication,
    AuthenticationProvider,
    GrantType
)
from .ani.user import User

from .ani.enum_ import (
    SeriesType,
    ListStatus,
    Smiley,
    Season,
    MediaType,
    AnimeStatus,
    MangaStatus,
    SortBy
)
from .ani.animeList import AnimeListResource

from .ani.browser import (
    Browser,
    Query
)

import logging

logging.basicConfig(
    format='%(levelname)s - %(name)s ln.%(lineno)d - %(message)s',
    level=logging.INFO)

logging.getLogger('anipy.ani.browser').setLevel(logging.DEBUG)

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
