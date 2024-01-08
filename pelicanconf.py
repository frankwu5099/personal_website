AUTHOR = 'PK Wu'
SITENAME = 'PK WU 學習筆記'
SITEURL = "."

PATH = "content"

TIMEZONE = 'America/Los_Angeles'
ABOUT_ME = """
Research Scientist<br/>
資料科學、機器學習<br/>
脫離學術的物理PhD<br/>
<br/>
電影、閱讀、學習心得</br>

"""

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/frankwu5099"),
    ("Linkedin", "https://www.linkedin.com/in/po-kuan-wu/"),
)

TWITTER_CARDS = True
DEFAULT_PAGINATION = 10
THEME = 'pelican-themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['i18n_subsites', 'render_math']

I18N_TEMPLATES_LANG = 'en'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PYGMENTS_STYLE = 'vim'
BOOTSTRAP_THEME  = 'yeti'
CUSTOM_CSS = 'static/css/custom.css'
STATIC_PATHS = [
  'images',
  'static'
]
#EXTRA_PATH_METADATA = {
#    'extra/custom.css': {'path': 'static/css/custom.css'}
#}
