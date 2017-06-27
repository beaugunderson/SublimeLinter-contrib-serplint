#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Beau Gunderson
# Copyright (c) 2017 Beau Gunderson
#
# License: MIT
#

"""This module exports the Serplint plugin class."""

from SublimeLinter.lint import PythonLinter, util


class Serplint(PythonLinter):
    """Provides an interface to serplint."""

    syntax = 'serpent'
    cmd = 'serplint -'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.1.0'
    regex = (
        r'^.+?:'
        r'(?P<line>\d+):'
        r'(?P<col>\d+) '
        r'(?:(?P<error>[EF])|(?P<warning>[WCN]))\d+ '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
    check_version = False
