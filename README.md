# Anipy
[![Python Version](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5-blue.svg)]()
[![Project License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/twissell-/anipy/master/LICENSE)


Anipy is a python library that wraps and organize the [Anilist] rest api into modules, classes and functions so it can be used quick, easy, and right out of the box. You can take a look at the api [official docs]. **Anilist is a [Josh Star]'s project**


## Table of contents

  * [Installation](#installation)
  * [Usage](#usage)
    * [Authentication](#authentication)
    * [Resources](#resources)
  * [Roadmap](#roadmap)


## Installation

For now the only available versions are alphas. You can Instaled the las by:
```bash
$ git clone https://github.com/twissell-/anipy.git
$ cd anipy
$ python setup.py # Be sure using Python 3
```

## Usage

I've tried to keep the developer interface as simple as possible.

### Authentication

Before you can access any Anilist resource you have to get authenticated. Once you have [created a client] you must configure ```auth.AuthenticationProvider``` class with your credentials.

Now you can get authenticated with any of the available [grant types]. Aditionaly, Anipy have a ```GrantType.refreshToken``` in case you have saved a refresh token from a previous authentication. *Note that only code and pin authentication gives you a refresh token.*

```python
from anipy.auth import AuthenticationProvider
from anipy.auth import Authentication
from anipy.auth import GrantType

AuthenticationProvider.config('your-client-id', 'your-client-secret', 'your-redirect-uri')

auth = Authentication.fromCredentials()
# or
auth = Authentication.fromCode('code')
# or
auth = Authentication.fromPin('pin')

# Now you can save the refresh token
refresh_token = auth.refreshToken

auth = Authentication.fromRefreshToken(refresh_token)
```

Authentication expires after one hour and will refresh automatically, nevertheless you can do it manually at any time, ie.:

```python
if auth.isExpired:
    auth.refresh()

```

### Resources

Resources are one of the most important parts of the library. The are in charge of go an get the data from the Anilist API. Each domain class have a resource, you can compare it to *Data Access Objects*.

In order to keep things simple you can access the resource from class it serves

```python
# Current logged user
user = User.resource().principal()
# A user for his Id or Display Name
user = User.resource().byId(3225)
user = User.resource().byDisplayName('demo')
```

Some resources are injected in other classes also in order to keep things simple (ie. ```AnimeListResource```). So if you want to get de watching list of a user you can do:

```python
# The long way
resource = AnimeListResource()
watching_list = resource.byUserId(user.id)
# Or the short way
watching_list = user.watching
```

## Roadmap

Here is a sumary of the project state.

### Next Release: 0.1

  - [x] **Authentication**
    - [x] Authorization Code
    - [x] Authorization Pin
    - [x] Client Credentials
  - [x] **User**
    - [x] Basics
  - [ ] **User Lists**
    - [ ] Animelist
    - [ ] Mangalist
    - [ ] Remove entry
    - [ ] List Scores
  - [ ] **Anime**
    - [ ] Basics
    - [ ] Airing
    - [ ] Search
  - [ ] **Manga**
    - [ ] Basics
    - [ ] Search

### Future Features

  - **User**
    - Activity
    - Followers & Following
    - Follow/Unfollow
    - Favourites
    - Notifications
    - Airing
    - Search
  - **Anime**
    - Characters / Staff
    - Browse
    - Favourite
  - **Manga**
    - Characters / Staff
    - Browse
    - Favourite
  - **Characters**
    - Favourite
    - Search
  - **Staff**
    - Favourite
    - Search
  - **Studio**
    - Search
  - **Reviews**
    - Review
    - Anime/Manga Reviews
    - User Reviews
    - Rate Review
    - Remove Review
  - **Forum**
    - Feeds
    - Thread
    - Create thread
    - Edit thread
    - Remove thread
    - Thread subscribe
    - Create comment
    - Edit comment
    - Remove comment
    - Search


[Anilist]: http://Anilist.co
[official docs]: https://anilist-api.readthedocs.io
[Josh Star]: https://github.com/joshstar

[created a client]: https://anilist-api.readthedocs.io/en/latest/introduction.html#creating-a-client
[grant types]:https://anilist-api.readthedocs.io/en/latest/authentication.html#which-grant-type-to-use
