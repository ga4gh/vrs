# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import subprocess
# import sys
# sys.path.insert(0, os.path.abspath('.'))

def _get_git_tag():
    res = subprocess.run("git describe --tags --always".split(), capture_output=True)
    tag = res.stdout.decode().strip()
    return tag

def _parse_release_as_version(rls):
    m = re.match("^(\d+\.\d+)", rls)
    if m:
        return m.group(1)
    return "unknown"


# -- Project information -----------------------------------------------------

project = 'vr-spec'
copyright = '2019, GA4GH'
author = 'Committers'
master_doc = 'index'
#release = _get_git_tag()
# version = _parse_release_as_version(release)
release = "6.7.8-dev.1"
version = release

# -- Schema doc paths --------------------------------------------------------

rst_epilog_fn = os.path.join(os.path.dirname(__file__), 'rst_epilog')
rst_epilog = open(rst_epilog_fn).read().format(release=release)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# TODO directive output
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = 'images/GA-logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Sidebars

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }
