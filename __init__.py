import asyncio
from nonebot.adapters.onebot.v11 import (
    GROUP,
    Bot,
    GroupMessageEvent,
    Message,
    MessageSegment,
    )
from .imitate import imitate

from nonebot import on_command,on_message
from nonebot.adapters.onebot.v11.exception import ActionFailed
from utils.utils import get_message_text
group_hook = {}

__zx_plugin_name__ = "模拟模拟宇宙"
__plugin_usage__ = """
usage:
    发送模拟模拟宇宙,一个群同时只有一人可玩，限时20分钟，当出现错误指令或者时间到会重置游戏
    开局后仅开局玩家可录入指令
""".strip()
__plugin_des__ = "模拟模拟宇宙"
__plugin_cmd__ = ["模拟模拟宇宙", "0123"]
__plugin_type__ = ("群内小游戏",)
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": __plugin_cmd__,
}
fake_universe = on_command("模拟模拟宇宙", permission=GROUP,priority=5,block=True)


def get_status(event:GroupMessageEvent):
    global group_hook
    if group_hook.get(event.group_id) and group_hook[event.group_id]["player"] == event.user_id:
        return True
    else:
        return False
input_arg = on_message(permission=GROUP,priority=996,rule=get_status)




@fake_universe.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    global group_hook
    if group_hook.get(event.group_id):
        await fake_universe.finish("该群已经在进行模拟模拟宇宙了,请等待时间结束或结算")
    else:
        group_hook[event.group_id] = {}
        group_hook[event.group_id]["player"] = event.user_id
        group_hook[event.group_id]["msg"] = ""
        group_hook[event.group_id]["answer_id"] = 0
        group_hook[event.group_id]["answer"] = {}
        group_hook[event.group_id]["log"] = ""
    async_list = [imitate(bot, event, group_hook[event.group_id]), jishiqi(event.group_id)]
    try:
        await asyncio.gather(*async_list)
    except ActionFailed:
        pass
    except Exception as e:
        print(e)
        group_hook[event.group_id] = {}
        await fake_universe.finish("模拟结束，可以进行新的了")


    
@input_arg.handle()
async def _(bot:Bot, event: GroupMessageEvent):
    global group_hook
    text = get_message_text(event.json())
    text.strip()
    id = group_hook[event.group_id]["answer_id"]
    group_hook[event.group_id]["answer"][id] = text
    await input_arg.finish()

        
        
async def jishiqi(group_id):
    global group_hook
    cd = 1200
    while cd > 0:
        cd -= 1
        await asyncio.sleep(1)
    group_hook[group_id] = {}
        


