from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .process import Process
import random
from .msg_utils import msg_merge
def use_yinhedaletou(obj: 'Process'):
    a = random.randint(1, 100)
    result = 0
    if a < 15:
        result = 1
    elif a < 20:
        msg_merge(obj.my_dict,f"银河大乐透生效")
        obj.normal_qiwu_list.remove("闪耀的偏方三八面骰")
        obj.normal_qiwu_list.remove("空无烛剪")
        for i in range(obj.multi):
            qiwu_name = random.choice(obj.normal_qiwu_list)
            obj.normal_qiwu_list.remove(qiwu_name)
            obj.have_qiwu_list.append(qiwu_name)
            msg_merge(obj.my_dict,f"获得{qiwu_name}")
        obj.normal_qiwu_list.append("闪耀的偏方三八面骰")
        obj.normal_qiwu_list.append("空无烛剪")
        
    return result
    
    
def use_jiangwei_touzi(obj: 'Process'):
    obj.bless_count = 2
    obj.get_bless_count = 2
    return 1  

def use_hundun_yunzhi(obj: 'Process'):
    obj.refresh_free = 1
    return 0

def use_yueqian_fuyan(obj: 'Process'):
    obj.upgrade_1 = 1
    return 0

def use_yimu_guoshi(obj: 'Process'):
    
    return 0

def use_cebuzhun_xia(obj: 'Process'):
    num = random.randint(1,2)
    bless_list = obj.get_bless("随机","随机", 3, three_prob=5)
    choose_list = random.sample(bless_list, num)
    msg_merge(obj.my_dict,"获得祝福", choose_list)
    for i in choose_list:
        obj.choose_bless(i)
    return 1

def use_xiangxian_ganlao(obj: 'Process'):

    return 0

def use_fuling_jiao(obj: 'Process'):
    obj.have_fulingjiao = 1
    return 1

def use_yongbutingzui_de_yangpijuan(obj: 'Process'):
    
    return 0

def use_boshi_zhipao(obj: 'Process'):
    
    return 0

def use_julebu_quan(obj: 'Process'):
    obj.julebuquan_multi = 1.75
    return 0
def use_xinyang_zhaiquan(obj: 'Process'):
    obj.xinyangzhaiquan_multi = 0.7
    return 1

def use_chunmei_zhipao(obj: 'Process'):
    
    return 0
def use_fenlie_jinbi(obj: 'Process'):
    obj.gold *= (1 + 0.06)
    obj.gold = int(obj.gold)
    return 1

def use_kongwu_zhujian(obj: 'Process'):
    repaired_qiwu_list = obj.repair_qiwu()
    msg_merge(obj.my_dict,repaired_qiwu_list)
    return 1
    
def use_tianwai_chongsheng_dadie(obj: 'Process'):
    
    return 0

def use_wanxiang_wuchang_tou(obj: 'Process'):
    for i in range(2):
        obj.upgrade_bless("随机")   
    return 1

def use_shanyao_de_pianfang_sanbamian_tou(obj: 'Process'):
    qiwu_num = len(obj.have_qiwu_list)
    obj.init_qiwu_list()
    obj.init_all_status()
    obj.normal_qiwu_list.remove("闪耀的偏方三八面骰")
    obj.init_all_instance_qiwu()
    new_list = random.sample(obj.normal_qiwu_list , qiwu_num)
    msg_merge(obj.my_dict,"获得", new_list)
    for i in new_list:
        obj.normal_qiwu_list.remove(i)
        obj.have_qiwu_list.append(i)
    return 1
def use_cunhu_huoqi(obj: 'Process'):
    obj.weights[1] += 1
    result = obj.get_bless("存护","随机", 1, three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_huanyu_huoqi(obj: 'Process'):
    obj.weights[6] += 1 
    result = obj.get_bless("欢愉","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_xunlie_huoqi(obj: 'Process'):
    obj.weights[0] += 1 
    result = obj.get_bless("巡猎","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_huimie_huoqi(obj: 'Process'):
    obj.weights[3] += 1
    result = obj.get_bless("毁灭","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_jiyi_huoqi(obj: 'Process'):
    obj.weights[5] += 1
    result = obj.get_bless("记忆","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_xuwu_huoqi(obj: 'Process'):
    obj.weights[4] += 1
    result = obj.get_bless("虚无","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_fengrao_huoqi(obj: 'Process'):
    obj.weights[2] += 1
    result = obj.get_bless("丰饶","随机", 1,three_prob=10)
    result = random.choice(result)
    obj.choose_bless(result)
    msg_merge(obj.my_dict,"获得",result)
    return 1

def use_luanqibajiao_de_daima(obj: 'Process'):
    
    return 0

def use_youdian_xiqiqiao_de_daima(obj: 'Process'):
    
    return 0

def use_zhongguizhongju_de_daima(obj: 'Process'):
    
    return 0

def use_jingque_youya_de_daima(obj: 'Process'):
    
    return 0

def use_wuxian_digui_de_daima(obj: 'Process'):
    
    return 0

def use_suixing_fangyv(obj: 'Process'):
    
    return 0

def use_yanmie_zhujian(obj: 'Process'):
    obj.yanmie_zhujian += obj.multi
    return 1

def use_chongwang(obj: 'Process'):
    
    return 0

def use_tianshi_xingxie_zhai_faxingji(obj: 'Process'):
    obj.have_tianshi_xingxie_zhai_faxingji = 1
    return 0

def use_huanjing_guiguan(obj: 'Process'):
    
    return 0

def use_shikong_lengjing(obj: 'Process'):
    
    return 0

def use_wanshi_nang(obj: 'Process'):
    obj.multi = 2
    return 0

def use_bushi_gugu_zhong(obj: 'Process'):
    
    return 0

def use_heisenlin_gugu_zhong(obj: 'Process'):
    
    return 0

def use_yongdong_gugu_zhong(obj: 'Process'):
    obj.gold *= 0.95
    obj.gold = int(obj.gold)
    return 0

def use_pengke_luode_jingshen(obj: 'Process'):
    
    return 0

def use_xinbiao_zhaoseji(obj: 'Process'):
    obj.upgrade_random = 1
    return 0

def use_gongsigu_gugu_zhong(obj: 'Process'):
        
    return 0

def use_jixie_gugu_zhong(obj: 'Process'):
        
    return 0

def use_meiyou_zhushi_de_daima(obj: 'Process'):
        
    return 0
