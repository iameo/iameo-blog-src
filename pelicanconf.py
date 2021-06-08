# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Emmanuel Okwudike'
SITENAME = 'bleh'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


# Social widget
SOCIAL = (('twitter', 'https://twitter.com/__oemmanuel__'),
          ('github', 'https://github.com/iameo'),
          ('envelope','mailto:okwudike.emmanuel@gmail.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'



MARKUP = ['md', 'ipynb']

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'ipynb.liquid',  # for embedding notebooks
    'liquid_tags.img',  # embedding images
    'liquid_tags.video',  # embedding videos
    'liquid_tags.include_code',  # including code blocks
    'liquid_tags.literal',
    'sitemap',
]

IGNORE_FILES = ['.ipynb_checkpoints']

IPYNB_USE_METACELL = True
IPYNB_IGNORE_CSS = True
IPYNB_SKIP_CSS = True


#LIQUID_CONFIGS = (("IPYNB_EXPORT_TEMPLATE", "notebook.tpl", ""), )



MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}



THEME = 'atyna'
COLOR_SCHEME_CSS = 'github.css'
SHOW_FULL_ARTICLE = False


STATIC_PATHS = ['images','downloads', 'notebooks']


TWITTER_USERNAME = '__oemmanuel__'
GITHUB_USERNAME = 'iameo'
AUTHOR_BLOG = 'https://iameo.github.io'
SHOW_ARCHIVES = True
SHOW_FEED = False 

NOTEBOOK_DIR = 'notebooks'

ENABLE_MATHJAX = True


SITEMAP= {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly',
    }
}

GOOGLE_ANALYTICS = 'UA-132444432-1'

