# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import alabaster
import datetime as dt
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "TPA Stream Developer Toolkit"
copyright = "2020, TPA Stream"
author = "TPA Stream"
master_doc = 'index'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["build"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_theme_path = [alabaster.get_path()]
html_show_sourcelink = False
templates_path = ["_templates"]
copyright = f'{dt.datetime.now():%Y} TPA Stream, Inc.'

html_theme_options = {
    "logo": "tpastream-logo-hori-RGB.179x33.png",
    "description": "Developer Toolkit",
    "description_font_style": "italic",
    "extra_nav_links": {
        "TPA Stream": "https://app.tpastream.com/login",
        "JavaScript SDK on NPM": "https://www.npmjs.com/package/easyenrollsdk",
    },
    "github_repo": "TPAStream/developer-docs",
    "github_banner": True,
}