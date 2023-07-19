import asyncio
from nonebot.adapters.onebot.v11 import (
    GROUP,
    Bot,
    GroupMessageEvent,
    Message,
    MessageSegment,
    )
from nonebot_plugin_apscheduler import scheduler
from .imitate import imitate
from utils.data_utils import init_rank
from utils.utils import scheduler
from nonebot import on_command,on_message
from nonebot.adapters.onebot.v11.exception import ActionFailed
from utils.utils import get_message_text
from utils.message_builder import image
from .json_util import *
from models.bag_user import BagUser
group_hook = {}

__zx_plugin_name__ = "模拟模拟宇宙"
__plugin_usage__ = """
usage:
    发送模拟模拟宇宙,一个群同时只有一人可玩，限时20分钟，当出现错误指令或者时间到会重置游戏
    开局后仅开局玩家可录入指令
    发送模拟模拟宇宙排行榜,可查看前10排名,一周刷新一次,按照排行每天晚上进行奖励发放
""".strip()
__plugin_des__ = "模拟模拟宇宙"
__plugin_cmd__ = ["模拟模拟宇宙", "模拟模拟宇宙排行榜"]
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
    text = get_message_text(event.json())
    text.strip()
    data = read_json_file(record_dir)
    group = str(event.group_id)
    id = str(event.user_id)
    if "排行榜" in text:
        rank_image = await init_rank("模拟模拟宇宙伤害排行榜", [int(item) for item in list(data[group]["rank"].keys())], list(data[group]["rank"].values()),event.group_id, 10)
        if rank_image:
            await fake_universe.finish(image(b64=rank_image.pic2bs4()))
    else:
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
        

@scheduler.scheduled_job("cron", day_of_week='mon', hour=6)
async def _():
    data = read_json_file(record_dir)
    for i in data:
        data[i] = {}
    write_json_file(record_dir)
@scheduler.scheduled_job(
    "cron",
    hour=22,
    minute=1,
)
async def _():
    data = read_json_file(record_dir)
    for i in data:
        gold_add = 150
        for j in data[i]["rank"]:
            group = int(i)
            id = int(j)
            await BagUser.add_gold(id, group, gold_add)
            gold_add -= 10

