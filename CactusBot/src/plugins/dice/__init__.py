"""
Nonebot 2 Dice Plugin
Author: XZhouQD
Since: 16 May 2021
"""
from pathlib import Path
import nonebot
from .handler import dice

# store all subplugins
_sub_plugins = set()
# load sub plugins
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

__version__ = '0.1.0'

__plugin_name__ = "XZhouQD's Roll"

__plugin_usage__ = "输入/roll help获取使用方法"

nonebot.export().roll = dice