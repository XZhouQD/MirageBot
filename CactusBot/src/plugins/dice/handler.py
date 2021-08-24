from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.log import logger

from .processor import get_help, roll_dice


dice = on_command("roll", priority=1, aliases={"掷骰", "骰子"})


@dice.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    logger.info(args)
    if args:
        state["content"] = args


@dice.got("content", prompt="输入指令内容！")
async def get_result(bot: Bot, event: Event, state: T_State):
    if state.get("content") in ('help', 'h'):
        at_user = MessageSegment.at(event.get_user_id())
        result = await get_help()
    else:
        at_user = MessageSegment.at(event.get_user_id())
        roll_result = await roll_dice(state.get("content"))
        result = MessageSegment.text(roll_result)
    await dice.finish(Message().append(at_user).append(result))
