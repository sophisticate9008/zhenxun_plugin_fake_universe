
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .process import Process
import random
from .msg_utils import *



async def zhuchengzhe(obj: 'Process'):
    msg_merge(obj.my_dict,"筑城者事件触发")
    msg_merge(obj.my_dict,"获得一个奇物(0), 离开,获得150宇宙碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_qiwu()
    else:
        obj.gold += 150
        
  
    
async def niuzai(obj: 'Process'):
    from .imitate import attack_monster
    msg_merge(obj.my_dict,"我们是牛仔事件触发,丢失50%碎片(0) 进入精英怪战斗, 概率结束战斗20% (1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        obj.gold *= 0.5
    else:
        await obj.dir_end(20)
        await attack_monster(obj, 1)
    

async def jiemuhakeyujiemuhaer(obj: 'Process'):
    msg_merge(obj.my_dict,"杰姆.哈克与杰姆.哈尔事件触发")
    msg_merge(obj.my_dict,"获得一个1-2星祝福(0), 转身走开,获得100宇宙碎片(1)")
    sel_0 = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel_0:
        await obj.get_thing_bless("随机", "随机")
    else:
        obj.gold += 100
        
        
        

async def xugoushixuejia(obj: 'Process'):
    msg_merge(obj.my_dict,"虚构史学家事件触发(改)")
    msg_merge(obj.my_dict,"强化三个一星(0) 强化两个二星(1) 强化一个三星(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        obj.upgrade_bless("随机",star="一星")
        obj.upgrade_bless("随机",star="一星")
        obj.upgrade_bless("随机",star="一星")
    elif "1" in sel:
        obj.upgrade_bless("随机",star="二星")
        obj.upgrade_bless("随机",star="二星")
    else:
        obj.upgrade_bless("随机",star="三星")

async def youmukuanggong(obj: 'Process'):
    msg_merge(obj.my_dict,"游牧矿工事件触发")
    msg_merge(obj.my_dict,"强化两个随机祝福(0), 获得一个二星存护祝福(1),后续(012)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        obj.upgrade_bless("随机")
        obj.upgrade_bless("随机")
    else:
        await obj.get_thing_bless("存护", "二星")
        
        
    
    

async def ruanmei(obj: 'Process'):
    msg_merge(obj.my_dict,"阮.梅事件触发")
    
    xingshen = random.choice(["巡猎,虚无,记忆,存护,欢愉,丰饶,毁灭"])
    msg_merge(obj.my_dict,f"获得全部{xingshen}祝福(0), 2000碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        for i in obj.all_bless:
            if xingshen in i:
                obj.choose_bless(i)
    else:
        obj.gold += 2000
            

async def hudongzhishu(obj: 'Process'):
    msg_merge(obj.my_dict,"互动艺术事件触发")
    msg_merge(obj.my_dict,"获得一个二星欢愉(0),获得一个二星巡猎(1),选择祝福时(012)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        await obj.get_thing_bless("欢愉","二星")
    else:
        await obj.get_thing_bless("巡猎", "二星")

async def dianshigouwupindao(obj: 'Process'):
    msg_merge(obj.my_dict,"电视购物频道事件触发")
    msg_merge(obj.my_dict,"莲花(0), 机械匣子(1)")
    
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        sel_1 = random.randint(1, 2)
        if sel_1 == 1:
            msg_merge(obj.my_dict,"丢弃一星获得两星")
            await obj.throw_bless(1,0,0)
            await obj.get_thing_bless("随机","两星")
        else:
            msg_merge(obj.my_dict,"丢弃两星获得一星")
            await obj.throw_bless(0,1,0)
            await obj.get_thing_bless("随机","一星")          
    else:
        sel_1 = random.randint(1, 2)
        if sel_1 == 1:
            await obj.get_thing_qiwu(1)
        else:
            await obj.get_thing_qiwu()
async def shangjinlieren(obj: 'Process'):
    msg_merge(obj.my_dict,"赏金猎人事件触发")
    msg_merge(obj.my_dict,"舍弃一个奇物,并获得200宇宙碎片(0), 离开(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        
        qiwu_list = obj.have_qiwu_list[:]
        ex_list = ["虫网", "机械咕咕钟", "公司咕咕钟", "永动咕咕钟", "黑森林咕咕钟", "卜筮咕咕钟","无限递归的代码", "有点蹊跷的代码",
                        "乱七八槽的代码", "没有注释的代码", "精确优雅的代码", "中规中矩的代码","天使型谢债发行机"]
        _list = list(set(qiwu_list) - set(ex_list))
        choose_list = random.sample(_list, len(_list))
        msg_merge(obj.my_dict,f"结果如下{choose_list}","按照012选择") 
        sel_1 = await get_answer(obj.my_dict,obj.bot,obj.event,3)
        obj.have_qiwu_list.remove(choose_list[int(sel_1)])
        obj.gold += 200
    else:
        pass

async def wujinheian(obj: 'Process'):
    msg_merge(obj.my_dict,"无尽黑暗事件触发")
    msg_merge(obj.my_dict,"负面奇物(0), 10%概率结束模拟(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_qiwu(1)
    else:
        await obj.dir_end(10)

async def fenhuagong(obj: 'Process'):
    msg_merge(obj.my_dict,"焚化工事件触发")
    msg_merge(obj.my_dict,"舍弃一个1-2星祝福,并获得一个1-3星祝福(0), 获得80宇宙碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.throw_bless(1,1,0)
        await obj.get_thing_bless("随机","随机",three_prob=20)
    else:
        obj.gold += 80

async def chongchao(obj: 'Process'):
    msg_merge(obj.my_dict,"虫巢事件触发")
    msg_merge(obj.my_dict,"深入(0), 止步于此,获得100碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        msg_merge(obj.my_dict,"获得负面奇物:虫网,并获得一个三星祝福(0),  获得一个二星祝福(1)")
        sel_1 = await get_answer(obj.my_dict,obj.bot,obj.event,2)
        if "0" in sel_1:
            await obj.get_thing_bless("随机","三星")
            obj.have_qiwu_list.append("虫网")
            
        else:
            await obj.get_thing_bless("随机","二星")
    else:
        gold += 100
    pass

async def diaoxiang(obj: 'Process'):
    msg_merge(obj.my_dict,"雕像事件触发")
    msg_merge(obj.my_dict,"获得一个二星祝福(0),获得一个三星祝福, 5%结束模拟(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_bless("随机","二星")
    else:
        await obj.get_thing_bless("随机","三星")
        await obj.dir_end(5)

async def sanzhixiaozhu(obj: 'Process'):
    from .imitate import attack_monster
    msg_merge(obj.my_dict,"三只小猪事件触发100%抓住第一只,50%抓住第两只 30%抓住第三只")
    rand = random.randint(1,100)
    num = 0
    if rand < 100:
        num += 1
    if rand < 70:
        num += 1
    if rand < 30:
        num += 1
    await attack_monster(obj, 0, 0)
    for i in range(num - 1):
        await attack_monster(obj, 0, 1)
    

async def shehuixingmengjing(obj: 'Process'):
    msg_merge(obj.my_dict,"社会性梦境事件触发")
    msg_merge(obj.my_dict,"获得随机负面奇物,并获得300宇宙碎片(0), 获得100宇宙碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        neg_qiwu = random.choice(obj.negative_qiwu_list)
        msg_merge(obj.my_dict,f"获得{neg_qiwu}")
        obj.have_qiwu_list.append(neg_qiwu)
        obj.negative_qiwu_list.remove(neg_qiwu)
        obj.gold += 1
    else:
        obj.gold += 100
async def ahawanou(obj: 'Process'):
    msg_merge(obj.my_dict,"啊哈玩偶事件触发")
    msg_merge(obj.my_dict,"可能获得150, 400碎片,也有可能一无所获")
    rand = random.randint(1,9)
    if rand <= 3:
        msg_merge(obj.my_dict,"获得150碎片")
        obj.gold += 150
    elif rand <= 6:
        msg_merge(obj.my_dict,"获得400碎片")
        obj.gold += 400
    else:
        msg_merge(obj.my_dict,"你一无所获")

async def zimiezhedehuozhong(obj: 'Process'):
    msg_merge(obj.my_dict,"自灭者的火种事件触发")
    msg_merge(obj.my_dict,"获得随机负面奇物，并获得一个三星祝福(0), 获得100宇宙碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_qiwu(1)
    else:
        obj.gold += 100
    pass

async def saliao(obj: 'Process'):
    msg_merge(obj.my_dict,"萨里奥事件触发")
    msg_merge(obj.my_dict,"获得一个奇物(0), 丢弃一个奇物,获得一个2星祝福(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_qiwu()
    else:
        qiwu_list = obj.have_qiwu_list[:]
        ex_list = ["虫网", "机械咕咕钟", "公司咕咕钟", "永动咕咕钟", "黑森林咕咕钟", "卜筮咕咕钟","无限递归的代码", "有点蹊跷的代码",
                        "乱七八槽的代码", "没有注释的代码", "精确优雅的代码", "中规中矩的代码","天使型谢债发行机"]
        _list = list(set(qiwu_list) - set(ex_list))
        result = random.sample(_list, 3 if len(_list) >= 3 else len(_list))
        msg_merge(obj.my_dict,"选择丢弃(01...)", result)
        sel_1 = await get_answer(obj.my_dict,obj.bot,obj.event,len(result))
        obj.have_qiwu_list.remove(result[int(sel_1)])
        obj.normal_qiwu_list.append(result[int(sel_1)])
        await obj.get_thing_bless("随机", "二星")
        


async def cuowudaoju(obj: 'Process'):
    msg_merge(obj.my_dict,"错误道具事件触发")
    msg_merge(obj.my_dict,"选择代码(0),退出(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        daima = random.sample(obj.code_qiwu_list, 3)
        msg_merge(obj.my_dict,f"请选择{daima}")
        sel_1 = await get_answer(obj.my_dict,obj.bot,obj.event,3)
        result = daima[int(sel_1)]
        obj.have_qiwu_list.append(result)
        obj.code_qiwu_list.remove(result)
    else:
        pass

async def sali(obj: 'Process'):
    msg_merge(obj.my_dict,"萨里事件触发")
    msg_merge(obj.my_dict,"获得一个奇物(0), 获得100碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        await obj.get_thing_qiwu()
    else:
        obj.gold += 100

async def nierdisipai(obj: 'Process'):
    from .imitate import attack_monster
    msg_merge(obj.my_dict,"尼尔迪斯牌事件触发")
    prob = 40
    fail = 0
    qiwu_list = obj.have_qiwu_list[:]
    while fail == 0:
        msg_merge(obj.my_dict,f"进行翻牌,成功获得随机奇物,失败进入精英怪战斗,15%概率直接结束模拟,当前失败概率{prob}% (0), 离开(1)")
        sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
        if "0" in sel:
            rand = random.randint(1, 100)
            if rand < prob:
                fail = 1
                await attack_monster(obj, 1, 1)
            else:
                qiwu = random.choice(obj.normal_qiwu_list)
                obj.normal_qiwu_list.remove(qiwu)
                msg_merge(obj.my_dict,"获得奇物为", qiwu)
                obj.have_qiwu_list.append(qiwu)
            prob += 20
        else:
            break
    

async def liao(obj: 'Process'):
    msg_merge(obj.my_dict,"里奥事件触发")
    msg_merge(obj.my_dict,"100碎片(0), 舍弃一个奇物,获得二星祝福(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        obj.gold += 100
    else:
        qiwu_list = obj.have_qiwu_list[:]
        ex_list = ["虫网", "机械咕咕钟", "公司咕咕钟", "永动咕咕钟", "黑森林咕咕钟", "卜筮咕咕钟","无限递归的代码", "有点蹊跷的代码",
                        "乱七八槽的代码", "没有注释的代码", "精确优雅的代码", "中规中矩的代码","天使型谢债发行机"]
        _list = list(set(qiwu_list) - set(ex_list))
        result = random.sample(_list, 3 if len(_list) >= 3 else len(_list))
        msg_merge(obj.my_dict,"选择丢弃(01...)", result)
        sel_1 = await get_answer(obj.my_dict,obj.bot,obj.event,len(result))
        obj.have_qiwu_list.remove(result[int(sel_1)])
        obj.normal_qiwu_list.append(result[int(sel_1)])
        await obj.get_thing_bless("随机", "二星")    


async def xiezhaifaxingji(obj: 'Process'):
    msg_merge(obj.my_dict,"谢债发行机事件触发")
    msg_merge(obj.my_dict,"获得奇物天使型谢债发行机(0), 100碎片(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        obj.have_qiwu_list.append("天使型谢债发行机")
    else:
        obj.gold += 100

async def yinheshangren(obj: 'Process'):
    msg_merge(obj.my_dict,"银河商人事件触发")
    msg_merge(obj.my_dict,f"100碎片购买金属许愿瓶(0), 200碎片购买银矿许愿瓶(1), 走开,当前碎片{obj.gold}(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if obj.gold < 100:
        sel = "2"
    if obj.gold < 200 and "1" in sel:
        sel = "2"
    if "0" in sel:
        obj.gold -= 100
        await obj.get_thing_bless("随机","一星")
    elif "1" in sel:
        neg_qiwu = random.choice(obj.negative_qiwu_list)
        msg_merge(obj.my_dict,"获得", neg_qiwu)
        obj.have_qiwu_list.append(neg_qiwu)
        obj.negative_qiwu_list.remove(neg_qiwu)
    else:
        pass
        

async def caiquanyouxi(obj: 'Process'):
    from .imitate import attack_monster
    msg_merge(obj.my_dict,"猜拳游戏事件触发")
    msg_merge(obj.my_dict,f"进入战斗,10%概率结束模拟(0), 失去100宇宙碎片,当前碎片{obj.gold}(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if obj.gold < 100:
        sel == "0"
    if "0" in sel:
        await obj.dir_end(15)
        await attack_monster(obj, 0)
    else:
        obj.gold += 100
    
        
 

async def yinhehuyou(obj: 'Process'):
    msg_merge(obj.my_dict,"银河忽悠事件触发")
    msg_merge(obj.my_dict,"消耗100碎片,获得捉摸不透的奇物(0) ,消耗100碎片, 获得梦幻的祝福(1), 离开(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if obj.gold < 100:
        sel = "2"
    if "0" in sel:
        await obj.get_thing_qiwu()
        obj.gold -= 100
    elif "1" in sel:
        await obj.get_thing_bless("随机","随机")
        obj.gold -= 100
    else:
        pass

async def xiangsusijie(obj: 'Process'):
    msg_merge(obj.my_dict,"像素世界事件触发,200碎片(0), 2个一星祝福(1)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,2)
    if "0" in sel:
        obj.gold += 200
    else:
        result = obj.get_bless("随机","一星", 2)
        result = random.sample(result, 2)
        for i in result:
            msg_merge(obj.my_dict,"获得", i)
            obj.choose_bless(result)          

async def yinhehaoren(obj: 'Process'):
    msg_merge(obj.my_dict,"银河好人事件触发")
    msg_merge(obj.my_dict,"消耗10碎片,购买钻石盒子(0), 原矿盒子(1), 离开(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        obj.gold -= 10
        for i in range(3):
            obj.upgrade_bless()
    elif "1" in sel:
        await obj.get_thing_bless("随机","三星")

async def laijiaohuanliwuba(obj: 'Process'):
    msg_merge(obj.my_dict,"来交换礼物吧事件触发")
    msg_merge(obj.my_dict,"祝福重铸(0),祝福交换(1), 离开(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        await obj.throw_bless(0,0,1)
        await obj.get_thing_bless("随机","三星")
    elif "1" in sel:
        await obj.throw_bless(1,1,0)
        await obj.get_thing_bless("随机","随机")
    else:
        pass

async def xugeyuanba(obj: 'Process'):
    msg_merge(obj.my_dict,"许个愿吧事件触发")
    msg_merge(obj.my_dict,"获得2星祝福%5几率结束模拟(0), 获得三星祝福%10几率结束模拟(1), 离开(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        await obj.dir_end(5)
        await obj.get_thing_bless("随机","二星")
    elif "1" in sel:
        await obj.dir_end(10)
        await obj.get_thing_bless("随机","二星")
    else:
        pass
    
    

async def jiqirenxiaoshouzhongduan(obj: 'Process'):
    msg_merge(obj.my_dict,"机器人销售终端事件触发")
    msg_merge(obj.my_dict,"消耗50宇宙碎片获得1-2星祝福(0) 100碎片获得1-3星祝福(1)  离开(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        await obj.get_thing_bless("随机", "随机")
    elif "1" in sel:
        obj.gold -= 100
        await obj.get_thing_bless("随机", "随机", three_prob=10)
    else:
        pass

async def jiuguan(obj: 'Process'):
    
    msg_merge(obj.my_dict,"酒馆事件触发")
    msg_merge(obj.my_dict,"获得一个记忆祝福(0) 获得一个毁灭祝福(1)  两个都要,15%几率结束模拟(2)")
    sel = await get_answer(obj.my_dict,obj.bot,obj.event,3)
    if "0" in sel:
        await obj.get_thing_bless("记忆", "随机",three_prob=30)
    elif "1" in sel:
        await obj.get_thing_bless("毁灭", "随机",three_prob=30)
    else:
        await obj.dir_end(15)
        await obj.get_thing_bless("记忆", "随机",three_prob=30)
        await obj.get_thing_bless("毁灭", "随机",three_prob=30)
async def zhouqixingdamowang(obj: 'Process'):
    from .imitate import attack_monster
    msg_merge(obj.my_dict,"周期性大魔王事件触发")
    msg_merge(obj.my_dict,"进行一次精英怪战斗(先加等同于精英怪的钱再扣钱), 40%几率追加祝福选择")
    await attack_monster(obj, 1)
    obj.gold -= 120
    if random.randint(1,100) <= 40:
        await obj.get_thing_bless("随机","随机",three_prob=30)
            

