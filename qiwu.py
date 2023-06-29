from .qiwu_use import *
from .qiwu_broken import *
from .msg_utils import *
class Qiwu:
    character_arg = 0
    def __init__(self, name, broke_count,priority,type,use_func, broken_func = None):
        self.name = name
        self.broke_count = broke_count
        self.use_func = use_func
        self.priority = priority
        self.type = type
        self.broken_func = broken_func
    async def use(self, *args, **kwargs):
        text = ""
        if(self.broke_count > 0):
            result = await self.use_func(*args, **kwargs)
            self.broke_count -= result
        elif self.broke_count == 0:
            if "火漆" not in self.name and "测不准" not in self.name:    
                text += f"{self.name}损坏"
            self.broke_count -= 1
            await self.broken(*args, **kwargs)
        else:
            pass
        return text
    async def broken(self, *args, **kwargs):
        if self.broken_func is not None:  
            return await self.broken_func(*args, **kwargs)
        

def get_all_qiwu_list() -> list:
    qiwu_list = []
    yinhedaletou = Qiwu("银河大乐透", 1, 2,  0, use_yinhedaletou, broken_func=broken_yinhedaletou)
    jiangwei_touzi = Qiwu("降维骰子", 2, 3,  1, use_jiangwei_touzi, broken_func=broken_jiangwei_touzi)
    hundun_yunzhi = Qiwu("混沌云芝", 999, 999,  2, use_hundun_yunzhi)
    yueqian_fuyan = Qiwu("跃迁复眼", 999, 999,  2, use_yueqian_fuyan)
    yimu_guoshi = Qiwu("异木果实", 999, 999,  4, use_yimu_guoshi)
    cebuzhun_xia = Qiwu("测不准匣", 1, 999,  2, use_cebuzhun_xia)
    xiangxian_ganlao = Qiwu("香涎干酪", 999, 999,  4, use_xiangxian_ganlao)
    fuling_jiao = Qiwu("福灵胶", 1, 999,  1, use_fuling_jiao, broken_func=broken_fuling_jiao)
    yongbutingzui_de_yangpijuan = Qiwu("永不停嘴的羊皮卷", 999, 999,  4, use_yongbutingzui_de_yangpijuan)
    boshi_zhipao = Qiwu("博士之袍", 999, 999,  4, use_boshi_zhipao)
    julebu_quan = Qiwu("俱乐部券", 999, 999,  2, use_julebu_quan)
    xinyang_zhaiquan = Qiwu("信仰债券", 999, 999,  2, use_xinyang_zhaiquan)
    chunmei_zhipao = Qiwu("纯美之袍", 999, 999,  4, use_chunmei_zhipao)
    fenlie_jinbi = Qiwu("分裂金币", 999, 999,  3, use_fenlie_jinbi)
    kongwu_zhujian = Qiwu("空无烛剪", 1, 1,  2, use_kongwu_zhujian)
    tianwai_chongsheng_dadie = Qiwu("天外重声大碟", 999, 999,  1, use_tianwai_chongsheng_dadie)
    wanxiang_wuchang_tou = Qiwu("万象无常骰", 1, 999,  2, use_wanxiang_wuchang_tou)
    shanyao_de_pianfang_sanbamian_tou = Qiwu("闪耀的偏方三八面骰", 999, 999,  2, use_shanyao_de_pianfang_sanbamian_tou)
    cunhu_huoqi = Qiwu("存护火漆", 1, 999,  2, use_cunhu_huoqi)
    huanyu_huoqi = Qiwu("欢愉火漆", 1, 999,  2, use_huanyu_huoqi)
    xunlie_huoqi = Qiwu("巡猎火漆", 1, 999,  2, use_xunlie_huoqi)
    huimie_huoqi = Qiwu("毁灭火漆", 1, 999,  2, use_huimie_huoqi)
    jiyi_huoqi = Qiwu("记忆火漆", 1, 999,  2, use_jiyi_huoqi)
    xuwu_huoqi = Qiwu("虚无火漆", 1, 999,  2, use_xuwu_huoqi)
    fengrao_huoqi = Qiwu("丰饶火漆", 1, 999,  2, use_fengrao_huoqi)
    luanqibajiao_de_daima = Qiwu("乱七八槽的代码", 999, 999,  4, use_luanqibajiao_de_daima)
    youdian_xiqiqiao_de_daima = Qiwu("有点蹊跷的代码", 999, 999,  4, use_youdian_xiqiqiao_de_daima)
    zhongguizhongju_de_daima = Qiwu("中规中矩的代码", 999, 999,  4, use_zhongguizhongju_de_daima)
    jingque_youya_de_daima = Qiwu("精确优雅的代码", 999, 999,  4, use_jingque_youya_de_daima)
    wuxian_digui_de_daima = Qiwu("无限递归的代码", 999, 999,  4, use_wuxian_digui_de_daima)
    suixing_fangyv = Qiwu("碎星芳饵", 999, 999,  4, use_suixing_fangyv)
    yanmie_zhujian = Qiwu("湮灭烛剪", 999, 999,  0, use_yanmie_zhujian)
    chongwang = Qiwu("虫网", 999, 999,  4, use_chongwang)
    tianshi_xingxie_zhai_faxingji = Qiwu("天使型谢债发行机", 5, 999,  1, use_tianshi_xingxie_zhai_faxingji)
    huanjing_guiguan = Qiwu("换境桂冠", 999, 999,  0, use_huanjing_guiguan)
    shikong_lengjing = Qiwu("时空棱镜", 999, 999,  0, use_shikong_lengjing)
    wanshi_nang = Qiwu("万识囊", 999, 1, 0,  use_wanshi_nang)
    bushi_gugu_zhong = Qiwu("卜筮咕咕钟", 999, 999,  1, use_bushi_gugu_zhong)
    heisenlin_gugu_zhong = Qiwu("黑森林咕咕钟", 999, 999,  2, use_heisenlin_gugu_zhong)
    yongdong_gugu_zhong = Qiwu("永动咕咕钟", 999, 999,  3, use_yongdong_gugu_zhong)
    pengke_luode_jingshen = Qiwu("朋克洛德精神", 999, 999,  4, use_pengke_luode_jingshen)
    xinbiao_zhaoseji = Qiwu("信标着色剂", 999, 999,  0, use_xinbiao_zhaoseji)
    gongsigu_gugu_zhong = Qiwu("公司咕咕钟", 999, 999,  2, use_gongsigu_gugu_zhong)
    jixie_gugu_zhong = Qiwu("机械咕咕钟", 999, 999,  4, use_jixie_gugu_zhong)
    meiyou_zhushi_de_daima = Qiwu("没有注释的代码", 999, 999,  4, use_meiyou_zhushi_de_daima)
    qiwu_list.append(yinhedaletou)
    qiwu_list.append(jiangwei_touzi)
    qiwu_list.append(hundun_yunzhi)
    qiwu_list.append(yueqian_fuyan)
    qiwu_list.append(yimu_guoshi)
    qiwu_list.append(cebuzhun_xia)
    qiwu_list.append(xiangxian_ganlao)
    qiwu_list.append(fuling_jiao)
    qiwu_list.append(yongbutingzui_de_yangpijuan)
    qiwu_list.append(boshi_zhipao)
    qiwu_list.append(julebu_quan)
    qiwu_list.append(xinyang_zhaiquan)
    qiwu_list.append(chunmei_zhipao)
    qiwu_list.append(fenlie_jinbi)
    qiwu_list.append(kongwu_zhujian)
    qiwu_list.append(tianwai_chongsheng_dadie)
    qiwu_list.append(wanxiang_wuchang_tou)
    qiwu_list.append(shanyao_de_pianfang_sanbamian_tou)
    qiwu_list.append(cunhu_huoqi)
    qiwu_list.append(huanyu_huoqi)
    qiwu_list.append(xunlie_huoqi)
    qiwu_list.append(huimie_huoqi)
    qiwu_list.append(jiyi_huoqi)
    qiwu_list.append(xuwu_huoqi)
    qiwu_list.append(fengrao_huoqi)
    qiwu_list.append(luanqibajiao_de_daima)
    qiwu_list.append(youdian_xiqiqiao_de_daima)
    qiwu_list.append(zhongguizhongju_de_daima)
    qiwu_list.append(jingque_youya_de_daima)
    qiwu_list.append(wuxian_digui_de_daima)
    qiwu_list.append(suixing_fangyv)
    qiwu_list.append(yanmie_zhujian)
    qiwu_list.append(chongwang)
    qiwu_list.append(tianshi_xingxie_zhai_faxingji)
    qiwu_list.append(huanjing_guiguan)
    qiwu_list.append(shikong_lengjing)
    qiwu_list.append(wanshi_nang)
    qiwu_list.append(bushi_gugu_zhong)
    qiwu_list.append(heisenlin_gugu_zhong)
    qiwu_list.append(yongdong_gugu_zhong)
    qiwu_list.append(pengke_luode_jingshen)
    qiwu_list.append(xinbiao_zhaoseji)
    qiwu_list.append(gongsigu_gugu_zhong)
    qiwu_list.append(jixie_gugu_zhong)
    qiwu_list.append(meiyou_zhushi_de_daima)
    return qiwu_list



