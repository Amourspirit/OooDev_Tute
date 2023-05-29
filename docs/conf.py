# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tute'
copyright = '2023, flywire'
author = 'flywire'
release = '0.0.1'

ooodev_url = "https://python-ooo-dev-tools.readthedocs.io/en/latest/"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
#     "sphinx_toolbox.collapse",
#     "sphinx_toolbox.more_autodoc.autonamedtuple",
#     "sphinx_toolbox.more_autodoc.typevars",
#     "sphinx_toolbox.more_autodoc.autoprotocol",
#     "sphinx_toolbox.more_autodoc.overloads",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
#     "sphinx.ext.extlinks",
#     "sphinx.ext.intersphinx",
#     "sphinx_autodoc_typehints",
    "sphinx_tabs.tabs",
#     "sphinx_design",
#     "sphinxcontrib.spelling",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
]

templates_path = ['_templates']
exclude_patterns = []

# copybutton_exclude = '.linenos, .gp, .go'
copybutton_prompt_text = r">>> ?|\.\.\. ?|\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'

# region css/js extras
html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"]
if html_theme == "sphinx_rtd_theme":
    html_css_files.append("css/readthedocs_custom.css")

if "sphinx_rtd_dark_mode" in extensions:
    html_css_files.append("css/readthedocs_dark.css")

html_css_files.append("css/style_custom.css")

html_js_files = [
    "js/custom.js",
]
# endregion css/js extras

numfig = True

# region Global Roles
# https://stackoverflow.com/questions/9698702/how-do-i-create-a-global-role-roles-in-sphinx
# custom global roles or any other rst to include

# sphinx includes s5defs.txt that has baked in roles but must be included.
# style_custom.css contains the colors that match these roles
# https://stackoverflow.com/questions/3702865/sphinx-restructuredtext-set-color-for-a-single-word/60991308#60991308
rst_prolog = ""
rst_prolog_lst = [
    ".. include:: <s5defs.txt>",
    "",
    ".. |odev| replace:: OooDev",
    f".. _odev: {ooodev_url}",
    "",
    ".. |ooouno| replace:: ooouno library",
    ".. _ooouno: https://pypi.org/project/ooouno/",
    "",
]

rst_prolog += "\n" + "\n".join(rst_prolog_lst)
# endregion Global Roles

# region intersphinx
intersphinx_mapping = {"ooodev": (ooodev_url, None)}

# endregion intersphinx