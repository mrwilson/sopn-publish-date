# -*- coding: utf-8 -*-

project = 'sopn-publish-date'
copyright = '2019, Alex Wilson'
author = 'Alex Wilson'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.2'


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'recommonmark'
]

templates_path = ['_templates']

source_suffix = '.rst'

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