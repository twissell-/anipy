from anipy.auth import Authentication
from anipy.auth import AuthenticationProvider
from anipy.user import User
from anipy.core import underscore_to_camelcase

from anipy.animeList import AnimeListResource


AuthenticationProvider.config('demo-vfxpa', 'mpnPS782wW47vwRMVOUQYJ6w0XszH', 'http://localhost:5000/ani/auth')

REFRESH_TOKEN = 'n1McU2cLdAplKjUaeBiDuEdwPiYno2r39rWk8DE4'

auth = Authentication.fromRefreshToken(REFRESH_TOKEN)

user = User.resource().principal()
print('id', user.id)
print('displayName', user.displayName)
for record in user.watching:
    print(record.anime.titleRomaji)
