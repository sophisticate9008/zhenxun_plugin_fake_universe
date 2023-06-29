from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .process import Process
from .msg_utils import msg_merge

async def broken_yinhedaletou(obj: 'Process'):
    
    await obj.dir_end(obj.leg_count * 2)
    
async def broken_jiangwei_touzi(obj: 'Process'):
    obj.bless_count = 3
    obj.get_bless_count = 1
    

async def broken_fuling_jiao(obj: 'Process'):
    obj.have_fulingjiao = 0
    
    
async def broken_tianshi_xingxie_zhai_faxingji(obj: 'Process'):
    obj.have_tianshi_xingxie_zhai_faxingji = 0
    obj.gold *= 2
    