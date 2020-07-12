# -*- coding: utf-8 -*-

project = 'sopn-publish-date'
copyright = '2020, Alex Wilson'
author = 'Alex Wilson'

# The short X.Y version
version = '1.4'
# The full version, including alpha/beta/rc tags
release = '1.4.1'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'recommonmark',
    'sphinx_markdown_tables'
]

templates_path = ['_templates']

source_suffix = ['.rst', '.md']

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


master_doc = 'index'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sopn-publish-datedoc'

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.

epub_title = project
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
