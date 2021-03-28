#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File name: test_open_selecter_view.py
# First Edit: 2021-03-25
# Last Change: 2021-03-25

__description__ = ""
__author__ = "@anosillus"
__license__ = "MIT"
__email__ = "anosillus@gmail.com"
__status__ = "Production"

import logging
import itertools
import os
from collections import Counter
from dataclasses import dataclass
from typing import Callable
from typing import Final
from typing import NamedTuple
from typing import TypedDict
from typing import Union
from logzero import logger
import logzero
from logzero import setup_logger
from src.log_settings import DEFAULT_LOG_SETTINGS
from src.open_selecter_view import *


logger = setup_logger(name=__name__, **DEFAULT_LOG_SETTINGS)


logzero.loglevel(logging.INFO)


def test_main():
    assert 5 == 5
    logger.debug("hello")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")


# vim: ft=python ts=4 sw=4 sts=4 tw=88 fenc=utf-8 ff=unix si et:
