#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Marquart'
SITENAME = u'tmy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@ivh', 'https://twitter.com/ivh'),
          ('Github', 'https://github.com/ivh'),)
GITHUB_URL = 'https://github.com/ivh/'
TWITTER_USERNAME = 'ivh'

#STATIC PATHS
STATIC_PATHS = [
    'pic',
    'static',
    'robots.txt',
    'favicon.ico',
]

RELATIVE_URLS = True
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
#CONTENT_CACHING_LAYER = 'generator'
#WITH_FUTURE_DATES = False

DEFAULT_METADATA = {
        'status': 'draft',
        'author': AUTHOR,
}

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
TYPOGRIFY = True
DEFAULT_PAGINATION = 4
USE_FOLDER_AS_CATEGORY = True
#THEME= '/home/tom/pelican-themes/blue-penguin'


