import random
import nonebot

default_start = list(nonebot.get_driver().config.command_start)[0]


async def roll_dice(xdy_asb: str):
    a, b, x, y = parse_cmd(xdy_asb)

    if x < 1 or y < 1:
        help_text = await get_help()
        return help_text
    if a == 0 and b == 0:
        result = f'{x}d{y} ='
    elif a != 0 and b == 0:
        result = f'{x}d{y}+{a} ='
    elif a == 0 and b != 0:
        result = f'{x}d{y}+S{b} ='
    else:
        result = f'{x}d{y}+{a}S{b} ='

    rolls = []
    num_sum = 0
    for i in range(x):
        z = random.randint(1, y) + a
        num_sum += z
        rolls.append(str(z))

    if b == 0:
        result = f'{result} {",".join(rolls)}, Sum = {num_sum}'
    else:
        result = f'{result} {",".join(rolls)}, Sum = {num_sum} + {b} = {num_sum + b}'

    return result


def parse_cmd(xdy_asb):
    xdy_list = xdy_asb.split('+')
    xdy = xdy_list[0].split('d')
    try:
        x = int(xdy[0])
        y = int(xdy[1])
        if len(xdy_list) > 1:
            aSb = xdy_list[1].split('S')
            try:
                a = int(aSb[0])
            except:
                a = 0
            try:
                b = int(aSb[1])
            except:
                b = 0
        else:
            a = 0
            b = 0
    except:
        a, b, x, y = 0, 0, 0, 0

    return a, b, x, y


async def get_help():
    return f'掷x个y面骰，为每个骰子增加附加值a，增加总和附加值b，' \
           f'使用{default_start}roll xdy+aSb'
