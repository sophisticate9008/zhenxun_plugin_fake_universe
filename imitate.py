import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .process import Process

def compare_priority(obj):#对奇物优先级进行排序
    return obj.priority


from .msg_utils import *
from .pic_utils import *
#0是击碎破坏物函数  #1是获得战斗后函数 #2是获得后立刻生效的函数 #3是回合结束后结算的函数
async def obtain_qiwu(obj: 'Process', type=0):#按照优先度获取奇物使用函数进行叠加
    obj.name_into_obj()
    sorted_list = sorted(obj.have_instance_qiwu_list, key=compare_priority)
    for i in sorted_list:
        self_type = i.type
        if self_type == type:
            await i.use(obj)



async def attack_monster(obj : 'Process', is_elite, is_thing = 0):
    
    if is_thing == 0:
        await obtain_qiwu(obj, 1)#战斗胜利
  
    gold_append = random.randint(28 * obj.julebuquan_multi, 32 * obj.julebuquan_multi)
    if is_elite == 1:
        gold_append = random.randint(int(140 * obj.julebuquan_multi), int(150 * obj.julebuquan_multi))
    if obj.have_tianshi_xingxie_zhai_faxingji == 1:
        gold_append = 0
    msg_merge(obj.my_dict,"战斗胜利获得宇宙碎片", gold_append)
    obj.gold += gold_append
    gold_spend = 0
    star = "随机"
    if is_elite == 1 or obj.have_fulingjiao:
        star = "三星"
    for i in range(obj.get_bless_count):        
        if obj.refresh_free == 1:
            result = obj.get_bless("随机", star)
            msg_merge(obj.my_dict,"可选祝福为",result)
            await push_image(obj.my_dict, obj.bot, obj.event, pic2b64(make_choose_bless_card(result, obj.gold)))
            msg_merge(obj.my_dict,"刷新(3) 选择(012)")
            sel = await get_answer(obj.my_dict, obj.bot, obj.event, 4)
            if "3" in sel:
                await obj.get_thing_bless("随机", star, type=0)
            else:
                obj.choose_bless(result[int(sel)])
        else:
            await obj.get_thing_bless("随机", star, type=0)

            
        obj.gold -= gold_spend
        



#0是获得金币的击碎物  #1是绿紫瓶
async def attack_crush(obj : 'Process', type):
    
    gold_append = random.randint(13, 16) * obj.multi
    if type == 1:
        gold_append = 0
    msg_merge(obj.my_dict,"击碎破坏物,获得宇宙碎片",gold_append)    
    obj.gold += gold_append
    await obtain_qiwu(obj, 0)#击碎
    await obtain_qiwu(obj, 2)#立即生效

async def turn_end(obj: 'Process'):
    await obtain_qiwu(obj, 3)#回合结束
    obj.leg_count += 1        
async def  shop(obj: 'Process'):
    msg_merge(obj.my_dict,"进入商店")
    msg_merge(obj.my_dict,f"80碎片购买一星祝福(0), 120购买一个奇物(1), 180强化两个随机祝福(2),当前碎片{obj.gold}, 离开(3)")
    sel = await get_answer(obj.my_dict, obj.bot, obj.event, 4)
    if "0" in sel and obj.gold >= 80:
        obj.gold -= 80
        await obj.get_thing_bless("随机","一星")
    elif "1" in sel and obj.gold >= 120:
        obj.gold -= 120
        await obj.get_thing_qiwu()
    elif obj.gold >= 180 and "2" in sel:
        obj.gold -= 180
        await obj.upgrade_bless("随机")
        await obj.upgrade_bless("随机")
    else:
        pass
    await obtain_qiwu(obj, 2)#立即生效
    await obtain_qiwu(obj, 2)#立即生效
    
async def relax_leg(obj: 'Process', is_end=0):
    if is_end == 0:
        
        msg_merge(obj.my_dict,"进入修整关")
        msg_merge(obj.my_dict,"进入商店在破坏三个破坏物(0), 击碎三个破坏物再进入商店(1)")
        sel = await get_answer(obj.my_dict, obj.bot, obj.event, 2)
        if "0" in sel:
            await shop(obj)
            for i in range(3):
                await attack_crush(obj, 1)
        else:
            for i in range(3):
                await attack_crush(obj, 1)  
            await shop(obj)  
        await turn_end(obj)    
    else:
        msg_merge(obj.my_dict,"将在击碎三个破坏物后结算")
        for i in range(3):
            await attack_crush(obj, 3)
        await obj.dir_end(100)



async def thing_leg(obj: 'Process', type = 0):

    crush_num = random.randint(1, 2 * obj.multi - 1)
    text = f"本关生成{crush_num}个可破坏物"
    msg_merge(obj.my_dict,text)
    msg_merge(obj.my_dict,"输入01序列来决定顺序,破坏物为0,事件为1,破坏物种类随机") 
    while True:
        input_crush_num = 0
        input_thing_num = 0
        order = await get_answer(obj.my_dict, obj.bot, obj.event, 2)
        for i in order:
            if i == '0':
                input_crush_num += 1
            else:
                input_thing_num += 1
        if input_crush_num == crush_num and input_thing_num == 1:
            break
        else:
            msg_merge(obj.my_dict,"不满足输入条件请重新输入")  
    for i in order:
        if i == "0":
            await attack_crush(obj, random.randint(0,1))
        else:
            await obj.trigger_thing(type=type)
    await obtain_qiwu(obj, 2)#立即生效

    await turn_end(obj)
    
async def normal_leg(obj: 'Process', monster_num=3):
    await obtain_qiwu(obj, 2)#立即生效

    crush_num = random.randint(1, 2 * obj.multi)
    rand = random.randint(1,100)
    text = f"本关生成{crush_num}个可破坏物,{monster_num}个怪物"
    if rand <= 8:
        text = f"本关生成{crush_num}个可破坏物,{monster_num}个怪物,1只小猪"
        monster_num += 1
    msg_merge(obj.my_dict,text)
    msg_merge(obj.my_dict,"输入01序列来决定顺序破坏物为0,怪物和猪为1,破坏物种类随机")
    order = 0
    while True:
        input_crush_num = 0
        input_monster_num = 0
        order = await get_answer(obj.my_dict, obj.bot, obj.event, 2)
        for i in order:
            if i == '0':
                input_crush_num += 1
            else:
                input_monster_num += 1
        if input_crush_num == crush_num and input_monster_num == monster_num:
            break
        else:
            msg_merge(obj.my_dict,"不满足输入条件请重新输入")
    for i in order:
        if i == '0':
            if random.randint(1,100) < 70:
                await attack_crush(obj, 0)
            else:
                await attack_crush(obj, 1)
        else:
            await attack_monster(obj, 0)
    await turn_end(obj)


from .process import Process
async def imitate(bot, event, my_dict):
    obj = Process(my_dict, bot, event)
    init_qiwu_list = random.sample(obj.normal_qiwu_list, 3)
    temp_count = 0
    while "银河大乐透" not in init_qiwu_list and temp_count < 10: #10倍权值出银河大乐透
        init_qiwu_list = random.sample(obj.normal_qiwu_list, 3)
        temp_count += 1
    #开局
    mingtu_list = ["存护", "记忆", "虚无", "丰饶", "巡猎", "毁灭", "欢愉"]
    msg_merge(obj.my_dict,f"选择你的命途(0123456){mingtu_list}")
    choose_mingtu = await get_answer(my_dict,bot, event,7)
    obj.mingtu = int(choose_mingtu)
    obj.weights[obj.mingtu] = 3
    mingtu = mingtu_list[int(choose_mingtu)]
    msg_merge(obj.my_dict,f"你选择了{mingtu}命途,获得对应祝福概率提升")
    msg_merge(obj.my_dict,"选择(012)",init_qiwu_list)
    choose_qiwu = await get_answer(my_dict,bot, event,3)
    init_qiwu_name = init_qiwu_list[int(choose_qiwu)]
    obj.have_qiwu_list.append(init_qiwu_name)
    obj.normal_qiwu_list.remove(init_qiwu_name)
    msg_merge(obj.my_dict,f"开局获得{init_qiwu_name}")
    
    #第一关
    await normal_leg(obj, 3)
    #第二关
    msg_merge(obj.my_dict,"选择战斗或事件(0 1)")
    sel = await get_answer(my_dict,bot, event,2)
    if "0" in sel:
        await normal_leg(obj, 3)
    else:
        await thing_leg(obj)
    
    
    #第三关
    msg_merge(obj.my_dict,"选择战斗或事件(0 1)")
    sel = await get_answer(my_dict,bot, event,2)
    if "0" in sel:
        await normal_leg(obj, 2)
    else:
        await thing_leg(obj)  
    #第四关
    msg_merge(obj.my_dict,"进入精英关")
    await attack_monster(obj, 1)
    await obj.get_thing_qiwu()
    await obtain_qiwu(obj, 2)#立即生效

    await turn_end(obj)
    
    #第五关
    await relax_leg(obj)
    #第六关

    choose_list = ["遭遇","事件","战斗"]
    result = random.sample(choose_list, 2)
    if "遭遇" in choose_list:
        choose_list.remove("遭遇")
    msg_merge(obj.my_dict,"选择(01)",result)
    sel = await get_answer(my_dict,bot, event,2)
    if "事件" in result[int(sel)]:
        await thing_leg(obj, 0)
    elif "遭遇" in result[int(sel)]:
        await thing_leg(obj, 1)
    elif "战斗" in result[int(sel)]:
        await normal_leg(obj, 2)
    #第七关
    obj.normal_thing_list.append("阮.梅")
    result = random.sample(choose_list, 2)
    if "遭遇" in choose_list:
        choose_list.remove("遭遇")
    msg_merge(obj.my_dict,"选择(01)",result)
    sel = await get_answer(my_dict,bot, event,2)
    if "事件" in result[int(sel)]:
        await thing_leg(obj, 0)
    elif "遭遇" in result[int(sel)]:
        await thing_leg(obj, 1)
    elif "战斗" in result[int(sel)]:
        await normal_leg(obj, 2)        
    #第八关
    msg_merge(obj.my_dict,"进入精英关")
    await attack_monster(obj, 1)
    await obj.get_thing_qiwu()
    await obtain_qiwu(obj, 2)#立即生效

    await turn_end(obj)
    #第九关
    await relax_leg(obj)
    #第十关
    choose_list.append("交易")
    result = random.sample(choose_list, 2)
    if "遭遇" in choose_list:
        choose_list.remove("遭遇")
    if "交易" in choose_list:
        choose_list.remove("交易")
    msg_merge(obj.my_dict,"选择(01)",result)
    sel = await get_answer(my_dict,bot, event,2)
    if "事件" in result[int(sel)]:
        await thing_leg(obj, 0)
    elif "遭遇" in result[int(sel)]:
        await thing_leg(obj, 1)
    elif "战斗" in result[int(sel)]:
        await normal_leg(obj, 2)
    elif "交易" in result[int(sel)]:
        await thing_leg(obj, 2)
    #第十一关
    result = random.sample(choose_list, 2)
    if "遭遇" in choose_list:
        choose_list.remove("遭遇")
    if "交易" in choose_list:
        choose_list.remove("交易")
    msg_merge(obj.my_dict,"选择(01)",result)
    sel = await get_answer(my_dict,bot, event,2)
    if "事件" in result[int(sel)]:
        await thing_leg(obj, 0)
    elif "遭遇" in result[int(sel)]:
        await thing_leg(obj, 1)
    elif "战斗" in result[int(sel)]:
        await normal_leg(obj, 2)
    elif "交易" in result[int(sel)]:
        await thing_leg(obj, 2)
    #第十二关
    result = random.sample(choose_list, 2)
    msg_merge(obj.my_dict,"选择(01)",result)
    sel = await get_answer(my_dict,bot, event,2)
    if "事件" in result[int(sel)]:
        await thing_leg(obj, 0)
    elif "遭遇" in result[int(sel)]:
        await thing_leg(obj, 1)
    elif "战斗" in result[int(sel)]:
        await normal_leg(obj, 2)
    elif "交易" in result[int(sel)]:
        await thing_leg(obj, 2)
    await obj.dir_end(100)
    

