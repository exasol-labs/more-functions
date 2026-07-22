import os
import sys

sys.path.insert(0, os.path.abspath("../"))

project = "More Functions"
copyright = "2026, Exasol"  # pylint: disable=redefined-builtin
author = "Exasol"

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design",
    "exasol.toolbox.sphinx.multiversion",
]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

todo_include_todos = True
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".build-docu",
    "changesets/**",
    "design.md",
    "system_requirements.md",
    "system_requirements/**",
]

html_theme = "shibuya"
html_static_path = ["_static"]
html_title = "More Functions"
html_theme_options = {
    "github_url": "https://github.com/exasol/more-functions",
    "accent_color": "grass",
}

linkcheck_rate_limit_timeout = 60
linkcheck_timeout = 15
linkcheck_delay = 30
linkcheck_retries = 2
linkcheck_anchors = False
linkcheck_ignore: list[str] = []
linkcheck_allowed_redirects = {r"https://github\.com/.*": r"https://github\.com/login*"}
