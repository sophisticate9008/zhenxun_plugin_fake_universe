from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .process import Process
from .msg_utils import msg_merge

async def broken_yinhedaletou(obj: 'Process'):
    msg_merge(obj.my_dict,"银河大乐透损坏")
    await obj.dir_end(obj.leg_count * 2)
    
async def broken_jiangwei_touzi(obj: 'Process'):
    obj.bless_count = 3
    obj.get_bless_count = 1
    msg_merge(obj.my_dict,"降维骰子损坏")

async def broken_fuling_jiao(obj: 'Process'):
    obj.have_fulingjiao = 0
    msg_merge(obj.my_dict,"福灵胶损坏")
    
async def broken_tianshi_xingxie_zhai_faxingji(obj: 'Process'):
    obj.have_tianshi_xingxie_zhai_faxingji = 0
    obj.gold *= 2
    msg_merge(obj.my_dict,"天使型谢债发行机发动")