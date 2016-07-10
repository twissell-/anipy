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

auth = Authentication.provider(GrantType.clientCredentials).authenticate()

auth = Authentication.provider(GrantType.authorizationCode).authenticate('code')

auth = Authentication.provider(GrantType.authorizationPin).authenticate('pin')

# Now you can save the refresh token
refresh_token = auth.refreshToken

auth = Authentication.provider(GrantType.refreshToken).authenticate(auth.refreshToken)
```

Authentication expires after one hour and will refresh automatically, nevertheless you can do it manually at any time, ie.:

```python
if auth.isExpired:
    auth.refresh()

```

### Resources

## Roadmap

Here is a sumary of the project state.

  - [x] **Authentication**
    - [x] Authorization Code
    - [x] Authorization Pin
    - [x] Client Credentials
  - [ ] **User**
    - [x] User Basics
    - [ ] Activity
    - [ ] Notifications
    - [ ] Followers & Following
    - [ ] Follow/Unfollow
    - [ ] Favourites
    - [ ] Airing
    - [ ] Search
  - [ ] **User Lists**
    - [ ] Animelist
    - [ ] Mangalist
    - [ ] Remove entry
    - [ ] List Scores
  - [ ] **Anime**
    - [ ] Characters / Staff
    - [ ] Airing
    - [ ] Browse
    - [ ] Favourite 
    - [ ] Search
  - [ ] **Manga**
    - [ ] Characters / Staff
    - [ ] Browse
    - [ ] Favourite
    - [ ] Search
  - [ ] **Characters**
    - [ ] Favourite
    - [ ] Search
  - [ ] **Staff**
    - [ ] Favourite
    - [ ] Search
  - [ ] **Studio**
    - [ ] Search
  - [ ] **Reviews**
    - [ ] Review
    - [ ] Anime/Manga Reviews
    - [ ] User Reviews
    - [ ] Rate Review
    - [ ] Remove Review
  - [ ] **Forum**
    - [ ] Feeds
    - [ ] Thread
    - [ ] Create thread
    - [ ] Edit thread
    - [ ] Remove thread
    - [ ] Thread subscribe
    - [ ] Create comment
    - [ ] Edit comment
    - [ ] Remove comment
    - [ ] Search


[Anilist]: http://Anilist.co
[official docs]: https://anilist-api.readthedocs.io
[Josh Star]: https://github.com/joshstar

[created a client]: https://anilist-api.readthedocs.io/en/latest/introduction.html#creating-a-client
[grant types]:https://anilist-api.readthedocs.io/en/latest/authentication.html#which-grant-type-to-use