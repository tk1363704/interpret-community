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
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'interpret-community'
copyright = '2020, Microsoft'
author = 'Microsoft'

# The full version, including alpha/beta/rc tags
release = '0.1.0.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks'
]

# enable links to objects in the other standard libraries, e.g., list and str in the Python standard library
intersphinx_mapping = {
    'Python': ('https://docs.python.org/3', None),
    'NumPy': ('http://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'SciPy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'sklearn': ('http://scikit-learn.org/stable', None)
}

# eventually we may be able to use intersphinx for these! TODO
autodoc_mock_imports = ['shap', 'shap.common', 'interpret', 'interpret.utils']

# enable links to objects in the other standard libraries, e.g., list and str in the Python standard library
intersphinx_mapping = {
    'Python': ('https://docs.python.org/3', None),
    'NumPy': ('http://docs.scipy.org/doc/numpy/', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'SciPy': ('http://docs.scipy.org/doc/scipy/reference', None),
    'sklearn': ('http://scikit-learn.org/stable', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# http://www.sphinx-doc.org/en/master/usage/configuration.html
# master doctree document
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
