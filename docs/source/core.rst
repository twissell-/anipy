Behind the curtain
==================

Here is how Anipy works underneath, more aimed to developers than common users of the library.

.. automodule:: anipy.core
   :members:

===========================
Entity and Resource classes
===========================

Almost any class in Anipy inherint from one of this two abstract base classes.

.. autoclass:: anipy.core.Entity
   :private-members:
   :special-members: __init__

.. autoclass:: anipy.core.Resource
   :members: request, get, post, put, delete, _headers, _URL, _ENDPOINT

==============
Authentication
==============

.. autoclass:: anipy.core.AuthenticationProvider
   :members:

.. autoclass:: anipy.core.Authentication
   :members:
   :undoc-members:

.. autoclass:: anipy.core.GrantType
   :members:
