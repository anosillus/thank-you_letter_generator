#!/usr/bin/env python #
# -*- coding: utf-8 -*-
# File name: test_open_selecter_view.py
# First Edit: 2021-03-25
# Last Change: 2021-03-25

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
from logzero import setup_logger
from log_settings import DEFAULT_LOG_SETTINGS
import PySimpleGUI as sg

logger = setup_logger(name=__name__, **DEFAULT_LOG_SETTINGS)

# ウィンドウの内容を定義する
layout = [
    [sg.Text("お名前は何ですか？")],
    [sg.Input(key="-入力-")],
    [sg.Text(size=(55, 1), key="-出力-")],
    [sg.Button("はい"), sg.Button("終了")],
]

# ウィンドウを作成する
window = sg.Window("ウィンドウタイトル", layout)

# イベントループを使用してウィンドウを表示し、対話する

while True:
    event, values = window.read()
    # ユーザーが終了したいのか、ウィンドウが閉じられたかどうかを確認してください

    if event == sg.WINDOW_CLOSED or event == "終了":
        break

    # Output a message to the window
    window["-出力-"].update("ハロー " + values["-入力-"] + "! PySimpleGUI をお試しいただきありがとうございます")

# 画面から削除して終了
window.close()

# vim: ft=python ts=4 sw=4 sts=4 tw=88 fenc=utf-8 ff=unix si et:
