# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------
#
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
#
# -- Project information -----------------------------------------------------
import os
import sys

from shopyo import __version__

current_dir = os.path.dirname(__file__)
print(current_dir)
target_dir = os.path.abspath(os.path.join(os.path.dirname(current_dir), "shopyo"))
print(target_dir)
sys.path.insert(0, os.path.abspath(target_dir))


# -- Project information -----------------------------------------------------

project = "Shopyo"
# copyright = '2020, Abdur-rahmaanJ'
author = "Abdur-rahmaanJ & Shopyo Team"
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
]

# autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
html_context = {
    "project_links": [
        "Source Code",
        "https://github.com/shopyo/shopyo",
        "Issue Tracker",
        "https://github.com/shopyo/shopyo/issues",
    ]
}
html_logo = "shopyo.png"

# html_sidebars = {
#     "**": ["navigation.html", "searchbox.html"]
# }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# html_theme_options = {
#     "github_repo": "shopyo/shopyo",
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
