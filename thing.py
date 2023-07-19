from .thing_use import *

class Thing:
    def __init__(self, name, func):
        self.name = name
        self.func = func
    def use(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def get_all_thing_list() -> list:
    thing_list = []
    thing_list.append(Thing("筑城者", zhuchengzhe))
    thing_list.append(Thing("牛仔", niuzai))
    thing_list.append(Thing("杰姆·哈克与杰姆·哈尔", jiemuhakeyujiemuhaer))
    thing_list.append(Thing("虚构史学家", xugoushixuejia))
    thing_list.append(Thing("游牧矿工", youmukuanggong))
    thing_list.append(Thing("阮.梅", ruanmei))
    thing_list.append(Thing("互动芝术", hudongzhishu))
    thing_list.append(Thing("电视购物频道", dianshigouwupindao))
    thing_list.append(Thing("赏金猎人", shangjinlieren))
    thing_list.append(Thing("无尽黑暗", wujinheian))
    thing_list.append(Thing("焚化工", fenhuagong))
    thing_list.append(Thing("虫巢", chongchao))
    thing_list.append(Thing("雕像", diaoxiang))
    thing_list.append(Thing("三只小猪", sanzhixiaozhu))
    thing_list.append(Thing("社会性梦境", shehuixingmengjing))
    thing_list.append(Thing("阿哈玩偶", ahawanou))
    thing_list.append(Thing("自灭者的火种", zimiezhedehuozhong))
    thing_list.append(Thing("萨里奥", saliao))
    thing_list.append(Thing("错误道具", cuowudaoju))
    thing_list.append(Thing("萨里", sali))
    thing_list.append(Thing("尼尔迪斯牌", nierdisipai))
    thing_list.append(Thing("里奥", liao))
    thing_list.append(Thing("谢债发行机", xiezhaifaxingji))
    thing_list.append(Thing("银河商人", yinheshangren))
    thing_list.append(Thing("猜拳游戏", caiquanyouxi))
    thing_list.append(Thing("银河忽悠", yinhehuyou))
    thing_list.append(Thing("像素世界", xiangsusijie))
    thing_list.append(Thing("银河好人", yinhehaoren))
    thing_list.append(Thing("来交换礼物吧", laijiaohuanliwuba))
    thing_list.append(Thing("许个愿吧", xugeyuanba))
    thing_list.append(Thing("机器人销售终端", jiqirenxiaoshouzhongduan))
    thing_list.append(Thing("酒馆", jiuguan))
    thing_list.append(Thing("周期性大魔王", zhouqixingdamowang))
    return thing_list
