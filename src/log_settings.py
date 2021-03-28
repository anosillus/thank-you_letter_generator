#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File name: log_settings.py
# First Edit: 2021-03-25
# Last Change: 2021-03-25

import logzero
import logging

log_format = "%(color)s[%(levelname)1.1s %(asctime)s %(name)s %(module)s %(funcName)s:%(lineno)d]%(end_color)s %(message)s"
formatter = logzero.LogFormatter(fmt=log_format)

DEFAULT_LOG_SETTINGS = {
    "logfile": "./logs/logger.log",
    "formatter": formatter,
    "maxBytes": 10000,
    "backupCount": 3,
    "level": logging.DEBUG,
    "fileLoglevel": logging.DEBUG,
}

# vim: ft=python ts=4 sw=4 sts=4 tw=88 fenc=utf-8 ff=unix si et:
