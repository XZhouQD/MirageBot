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

default_start = list(nonebot.get_driver().config.command_start)[0]
__usage__ = f'掷x个y面骰，为每个骰子增加附加值a，增加总和附加值b，使用{default_start}roll xdy+aSb'

__help_version__ = '0.1.0'

__help_plugin_name__ = "XZhouQD's Dice"

nonebot.export().roll = dice
