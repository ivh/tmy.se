#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Marquart'
SITENAME = u'tmy.se'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'en'

OUTPUT_RETENTION = ['t','tmp']
#STATIC PATHS
STATIC_PATHS = [
    'pic',
#    'static',
    'robots.txt',
    'favicon.ico',
    'keybase.txt',
    't',
    'tmp',
]

DELETE_OUTPUT_DIRECTORY = False
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CONTENT_CACHING_LAYER = 'reader' #'generator' # 'reader' otherwise
WITH_FUTURE_DATES = False

DEFAULT_METADATA = {
        'status': 'draft',
        'author': AUTHOR,
        'title': ' ',
}

RELATIVE_URLS = True
INDEX_SAVE_AS = 'index'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}'
PAGE_SAVE_AS = '{slug}'
PAGE_URL = '{slug}'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}'
CATEGORY_URL = 'tag/{slug}'
CATEGORY_SAVE_AS = 'tag/{slug}'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}'
AUTHOR_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = 'tags'

TYPOGRIFY = False
DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = None

THEME= 'theme/chunk'
SITESUBTITLE = None
FOOTER_TEXT = 'Built with <a href="http://getpelican.com">Pelican</a>, served by <a href="https://caddyserver.com/">Caddy</a>.'
DISPLAY_CATEGORIES_ON_MENU = False
LINKS = (('email: blog@tmy.se', 'mailto:blog@tmy.se'),('about','/about'))
SINGLE_AUTHOR = True
MINT = False

PLUGIN_PATHS = ['plugins']
PLUGINS = ["photos"] # "representative_image"

PHOTO_LIBRARY = "content/pic/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = ( 590, 900, 80)
PHOTO_THUMB = (92, 84, 60)
PHOTO_RESIZE_JOBS = 1
PHOTO_WATERMARK = False
PHOTO_WATERMARK_TEXT = ''
PHOTO_WATERMARK_IMG = ''

# Feed generation is usually not desired when developing
FEED_RSS = None
FEED_ATROM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
