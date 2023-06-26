from .qiwu import get_all_qiwu_list
from .thing import get_all_thing_list
import random
import sys
from .msg_utils import *
class Process:
    leg_count = 1
    negative_qiwu_list = ["机械咕咕钟", "公司咕咕钟", "永动咕咕钟", "黑森林咕咕钟", "卜筮咕咕钟"]
    code_qiwu_list = ["无限递归的代码", "有点蹊跷的代码",
                      "乱七八槽的代码", "没有注释的代码", "精确优雅的代码", "中规中矩的代码"]
    normal_thing_list = [
        "筑城者",
        "牛仔",
        "杰姆·哈克与杰姆·哈尔",
        "虚构史学家",
        "游牧矿工",
        "互动芝术",
        "电视购物频道",
        "赏金猎人",
        "无尽黑暗",
        "焚化工",
        "虫巢",
        "雕像",
        "三只小猪",
        "社会性梦境",
        "阿哈玩偶",
        "自灭者的火种",
        "萨里奥",
        "错误道具",
        "萨里",
        "尼尔迪斯牌",
        "里奥",
        "谢债发行机",
        "银河商人",
        "猜拳游戏",
        "银河忽悠",
        "像素世界",
        "银河好人",
    ]
    trade_thing_list = ["来交换礼物吧","许个愿吧","机器人销售终端"]
    come_across_ting_list = ["酒馆","周期性大魔王"]
    have_qiwu_list = []
    all_instance_qiwu_list = []
    have_instance_qiwu_list = []
    all_instance_thing_list = []
    multi = 1
    gold = 0
    mingtu = 0
    yanmie_zhujian = 0
    have_bless = []
    bless_count = 3
    weights = [1,1,1,1,1,1,1]
    get_bless_count = 1
    upgrade_1 = 0
    upgrade_random = 0
    refresh_free = 0
    julebuquan_multi = 1
    xinyangzhaiquan_multi = 1
    have_fulingjiao = 0
    have_tianshi_xingxie_zhai_faxingji = 0
    my_dict = {}
    bot = None
    event = None
    def __init__(self, my_dict,bot, event):
        self.init_qiwu_list()
        self.init_all_instance_qiwu()
        self.init_bless_list()
        self.init_all_instance_thing()
        self.my_dict = my_dict
        self.bot = bot
        self.event = event
    def init_all_instance_thing(self):
        self.all_instance_thing_list = get_all_thing_list()
        
    def init_all_status(self):
        self.multi = 1
        self.yanmie_zhujian = 0
        self.bless_count = 3
        self.weights = [1,1,1,1,1,1,1]
        self.weights[self.mingtu] = 3
        self.get_bless_count = 1
        self.upgrade_1 = 0
        self.upgrade_random = 0
        self.refresh_free = 0
        self.julebuquan_multi = 1
        self.xinyangzhaiquan_multi = 1
        self.have_fulingjiao = 0
        self.have_tianshi_xingxie_zhai_faxingji = 0
    def init_qiwu_list(self):
        self.normal_qiwu_list = [
            "降维骰子",
            "混沌云芝",
            "跃迁复眼",
            "异木果实",
            "测不准匣",
            "香涎干酪",
            "福灵胶",
            "永不停嘴的羊皮卷",
            "博士之袍",
            "俱乐部券",
            "信仰债券",
            "纯美之袍",
            "分裂金币",
            "空无烛剪",
            "天外重声大碟",
            "万象无常骰",
            "闪耀的偏方三八面骰",
            "存护火漆",
            "欢愉火漆",
            "巡猎火漆",
            "毁灭火漆",
            "记忆火漆",
            "虚无火漆",
            "丰饶火漆",
            "碎星芳饵",
            "湮灭烛剪",
            "换境桂冠",
            "时空棱镜",
            "银河大乐透",
            "万识囊",
            "朋克洛德精神",
            "信标着色剂",
        ]
        self.have_qiwu_list = []
    
    def init_bless_list(self):
        self.all_bless = ["普通_一星_巡猎_电射牛斗","普通_一星_巡猎_背生击死","普通_一星_巡猎_乌号綦箭","普通_一星_巡猎_桑弧蓬矢","普通_一星_巡猎_天棓步危",
                          "普通_一星_巡猎_彤弓素矰","普通_一星_巡猎_雷车动地","普通_一星_巡猎_背孤击虚","特殊_二星_巡猎_天舟缴夙敌","普通_二星_巡猎_飞虹诛凿齿",
                          "普通_二星_巡猎_景星助狩月","普通_二星_巡猎_云镝逐步离","普通_二星_巡猎_流岚追孽物","普通_二星_巡猎_背生击死","特殊_二星_巡猎_白矢决射御",
                          "特殊_二星_巡猎_序师执迟彝","特殊_三星_巡猎_帝星君临制穹桑","特殊_三星_巡猎_帝星君临制穹桑","特殊_三星_巡猎_帝车超光所向捷",
                          "普通_三星_巡猎_帝弓断空彻太清",
                          "普通_一星_存护_构筑·哨戒","普通_一星_存护_构筑·坚定","普通_一星_存护_构筑·哨戒","普通_一星_存护_构筑·回转","普通_一星_存护_构筑·弥合",
                          "普通_一星_存护_构筑·专注","普通_一星_存护_构筑·聚塑","普通_一星_存护_构筑·补偿","普通_一星_存护_构筑·迸发",
                          "普通_一星_记忆_体验:难言的羞耻","普通_一星_记忆_体验:决绝的痛恨","普通_一星_记忆_体验:原初的苦衷","普通_一星_记忆_体验:丢失的记忆",
                          "普通_一星_记忆_体验:病痛的折磨","普通_一星_记忆_体验:攀升的刺激","普通_一星_记忆_体验:回应的兴奋","普通_一星_记忆_体验:疏离的煎熬",
                          "普通_一星_虚无_漠视主义","普通_一星_虚无_悲剧讲座","普通_一星_虚无_知觉迷墙","普通_一星_虚无_意义质询","普通_一星_虚无_虚妄供品",
                          "普通_一星_虚无_虚妄供品","普通_一星_虚无_日出之前","普通_一星_虚无_盲目视界","普通_一星_虚无_情绪舍锅",
                          "普通_一星_丰饶_加持","普通_一星_丰饶_加持","普通_一星_丰饶_延寿","普通_一星_丰饶_禳灾","普通_一星_丰饶_甘露","普通_一星_丰饶_愿印",
                          "普通_一星_丰饶_回生","普通_一星_丰饶_胜军","普通_一星_丰饶_法雨",
                          "普通_一星_毁灭_永坍缩体","普通_一星_毁灭_偏振受体","普通_一星_毁灭_回光效应","普通_一星_毁灭_不稳定带","普通_一星_毁灭_原生黑洞",
                          "普通_一星_毁灭_轨道红移","普通_一星_毁灭_储备度规","普通_一星_毁灭_哨戒卫星",
                          "普通_一星_欢愉_《基本有害》","普通_一星_欢愉_《阴风阵阵》","普通_一星_欢愉_《回灯塔去》","普通_一星_欢愉_《奇爱医生》",
                          "普通_一星_欢愉_《铂金时代》","普通_一星_欢愉_《操行满分》","普通_一星_欢愉_《发条苹果》","普通_一星_欢愉_《灰暗的火》",
                          "特殊_二星_存护_星间构筑·迸裂晶格","普通_二星_存护_星间构筑·回馈庇护","普通_二星_存护_星间构筑·安全载荷","普通_二星_存护_星间构筑·四棱锥体",
                          "普通_二星_存护_星间构筑·亚共晶体","特殊_二星_存护_星间构筑·切变结构","特殊_二星_存护_星间构筑·固溶强化",
                          "特殊_二星_记忆_极端体验:头晕目眩","普通_二星_记忆_极端体验:特立独行","普通_二星_记忆_极端体验:多愁善感","普通_二星_记忆_极端体验:沦浃肌髓",
                          "普通_二星_记忆_极端体验:不寒而栗","特殊_二星_记忆_极端体验:麻木不仁","特殊_二星_记忆_极端体验:怅然若失",
                          "特殊_二星_虚无_开端与终结","普通_二星_虚无_火堆外的夜","特殊_二星_虚无_旷野的呼告","普通_二星_虚无_他人即地狱",
                          "普通_二星_虚无_无根据颂歌","普通_二星_虚无_存在的黄昏","特殊_二星_虚无_自欺咖啡馆",
                          "普通_二星_丰饶_大愿般若船","特殊_二星_丰饶_灭罪累生善","普通_二星_丰饶_大愿般若船","特殊_二星_丰饶_慧海度慈航","普通_二星_丰饶_明澈琉璃身",
                          "普通_二星_丰饶_宝光烛日月","普通_二星_丰饶_厌离邪秽苦","特殊_二星_丰饶_天人不动众",
                          "普通_二星_毁灭_戒律性闪变","特殊_二星_毁灭_灾难性共振","普通_二星_毁灭_破坏性耀发","特殊_二星_毁灭_预兆性景深","普通_二星_毁灭_毁灭性吸积",
                          "普通_二星_毁灭_危害性余光","特殊_二星_毁灭_递增性末日",
                          "特殊_二星_欢愉_《流吧,你的眼泪》","特殊_二星_欢愉_《燃烧男子的肖像》","特殊_二星_欢愉_《砂时镜下的幼园》","普通_二星_欢愉_《十二猴子与怒汉》",
                          "普通_二星_欢愉_《第二十一条军规》","普通_二星_欢愉_《被涂污的信天翁》","普通_二星_欢愉_《利尔他引力之虹》",
                          "特殊_三星_存护_神性构筑·谐振传递","普通_三星_存护_神性构筑·宏观偏析","特殊_三星_存护_神性构筑·超静定场",
                          "特殊_三星_记忆_完美体验:纯真","特殊_三星_记忆_完美体验:浮黎","普通_三星_记忆_完美体验:缄默",
                          "普通_三星_虚无_为何一切尚未消失","特殊_三星_虚无_被装在套子里的人","特殊_三星_虚无_感官追奉者的葬礼",
                          "普通_三星_丰饶_丰饶众生,一法界心","特殊_三星_丰饶_葳蕤繁祉,延彼遐龄","特殊_三星_丰饶_若罪若福,施诸愿印",
                          "普通_三星_毁灭_湮灭回归不等式","特殊_三星_毁灭_寰宇热寂特征数","特殊_三星_毁灭_反物质非逆方程",
                          "特殊_三星_欢愉_《四号屠场·众生安眠》","特殊_三星_欢愉_《自动口琴·茫茫白夜》","特殊_三星_欢愉_《冠军晚餐·猫的摇篮》"
                          ]
        
    def init_all_instance_qiwu(self):
        self.all_instance_qiwu_list = get_all_qiwu_list()
        
    def name_into_obj(self):
        self.have_instance_qiwu_list = []
        for i in self.have_qiwu_list:
            for j in self.all_instance_qiwu_list:
                if i == j.name:
                    self.have_instance_qiwu_list.append(j)
        self.have_instance_qiwu_list = list(set(self.have_instance_qiwu_list))
        return self.have_instance_qiwu_list
    
    def repair_qiwu(self):
        new_instance_qiwu = get_all_qiwu_list()
        repaired_qiwu_list = []
        for i in range(len(self.have_instance_qiwu_list)):
            if self.have_instance_qiwu_list[i].broke_count < 1:
                for j in new_instance_qiwu:
                    if self.have_instance_qiwu_list[i].name == j.name:
                        self.have_instance_qiwu_list[i] = j
                        repaired_qiwu_list.append(j.name)
        return repaired_qiwu_list
    
    def get_kind_bless(self):
        all_kind_bless = []
        kind_0 = []
        kind_1 = []
        kind_2 = []
        kind_3 = []
        kind_4 = []
        kind_5 = []
        kind_6 = []
        for i in self.all_bless:
            if "巡猎" in i:
                kind_0.append(i)
            if "存护" in i:
                kind_1.append(i)
            if "丰饶" in i:
                kind_2.append(i)                             
            if "毁灭" in i:
                kind_3.append(i)
            if "虚无" in i:
                kind_4.append(i)
            if "记忆" in i:
                kind_5.append(i)
            if "欢愉" in i:
                kind_6.append(i)
        all_kind_bless.append(kind_0)
        all_kind_bless.append(kind_1)                                       
        all_kind_bless.append(kind_2) 
        all_kind_bless.append(kind_3) 
        all_kind_bless.append(kind_4) 
        all_kind_bless.append(kind_5) 
        all_kind_bless.append(kind_6)
        return all_kind_bless
    
    #0为战斗胜利后获得祝福  #1为商店获得祝福 #2为事件获得祝福 #3为奇物获得祝福
    def get_bless(self, name, star,type = 0, two_prob=30, three_prob=0):
        all_kind_bless = self.get_kind_bless()
        weights = self.weights[:]
        if type != 0:
            weights = [1,1,1,1,1,1,1]
            weights[self.mingtu] = 3
        total_weight = sum(weights)
        normalized_weights = [weight / total_weight for weight in weights]
        unaverage_bless_unlock = []
        name_list = []
        star_list = []
        choose_list = []
        upgrade_list = []
        return_list = []
        for i in self.have_bless:
            if "特殊" in i:
                temp = i.split("_")
                unaverage_bless_unlock.append(temp[2])

        for i in self.all_bless:
            if name == "随机":
                name_list.append(i)
            if name in i:
                name_list.append(i)
        
        for i in name_list:
            if star == "随机":
                if "三星" in i and random.randint(1,100) <= three_prob:
                    star_list.append(i)
                elif "二星" in i and random.randint(1,100) <= two_prob:
                    star_list.append(i)
                elif "一星" in i:
                    star_list.append(i)
            if star in i:
                star_list.append(i)
        for i in star_list:
            if "特殊" in i:
                temp = i.split("_")
                if temp[1] == "二星":
                    if temp[2] not in unaverage_bless_unlock:
                        star_list.remove(i)
        for i in star_list:
            if "特殊" in i:
                temp = i.split("_")
                if temp[1] == "二星":
                    if temp[2] not in unaverage_bless_unlock:
                        star_list.remove(i)
        
        choose_list = []
        bless_count = self.bless_count
        if type != 0:
            bless_count = 3
        condition = True
        while condition:
            condition_count = 0
            choose_list = random.choices(
                [immsg_merge for category in all_kind_bless for immsg_merge in category],  # 平铺刻印列表
                weights=[weight for weight, category in zip(normalized_weights, all_kind_bless) for _ in range(len(category))],  # 平铺权重列表
                k=bless_count  # 选择数量
            )
            for i in choose_list:
                if i in star_list:
                    condition_count += 1
            if condition_count == bless_count and len(set(choose_list)) == bless_count:
                condition = False
                    
        if self.upgrade_1 == 1 and type == 0:
            for i in choose_list:
                temp = i.split("_")
                if temp[1] == "一星":
                    upgrade_list.append(i + "_2")
                else:
                    upgrade_list.append(i)
        else:
            upgrade_list = choose_list
        
        if self.upgrade_random == 1 and type == 0:
            need_upgrade_list = []
            for i in upgrade_list:
                temp = i.split("_")
                if len(temp) == 4:
                    need_upgrade_list.append(i)
                else:
                    return_list.append(i)
            if len(need_upgrade_list) > 0:
                upgrade_bless = random.choice(need_upgrade_list)
                return_list.append(upgrade_bless)
                need_upgrade_list.remove(upgrade_bless)
                for j in need_upgrade_list:
                    return_list.append(i)
        else:
            return_list = upgrade_list
        return return_list    
     
    def choose_bless(self, name):
        for i in self.all_bless:
            temp = i.split("_")
            compare = name.split("_")
            if temp[3] == compare[3]:
                self.have_bless.append(name)
                self.all_bless.remove(i)
                
    def get_need_upgrade_list(self, star="随机"):
        need_upgrade_list = []
        for i in self.have_bless:
            temp = i.split("_")
            if star == "随机":
                star_ = True
            else:
                if star in i:
                    star_ = True
                else:
                    star_ = False
            if len(temp) == 4 and star_:
                need_upgrade_list.append(i)
        return need_upgrade_list
    def upgrade_bless(self, name, star="随机"):
        
        gold_multi = 1
        need_upgrade_list = self.get_need_upgrade_list(star)
        if len(need_upgrade_list) != 0:   
            _upgrade_bless = ""
            if name == "随机":
                _upgrade_bless = random.choice(need_upgrade_list)
                gold_multi = 0
            else:
                _upgrade_bless = name
            if "一星" in _upgrade_bless:
                gold_need = 100
            if "二星" in _upgrade_bless:
                gold_need = 130
            if "三星" in _upgrade_bless:
                gold_need = 160
            
            self.have_bless.remove(_upgrade_bless)
            self.have_bless.append(_upgrade_bless + "_2")
            if name == "随机":
                msg_merge(self.my_dict,"强化结果", _upgrade_bless)
            self.gold -= gold_need * gold_multi * self.xinyangzhaiquan_multi
        else:
            msg_merge(self.my_dict,"没有可用强化的祝福")
    async def throw_bless(self, one, two, three):
        one_list = []
        two_list = []
        three_list = []
        unite_list = []
        for i in self.have_bless:
            if "一星" in i:
                one_list.append(i)
            elif "二星" in i:
                two_list.append(i)
            else:
                three_list.append(i)
        if one == 1:
            unite_list.extend(one_list)
        if two == 1:
            unite_list.extend(two_list)
        if three == 1:
            unite_list.extend(three_list)
        result = random.sample(unite_list, 3)
        msg_merge(self.my_dict,"请丢弃(012)", result)
        sel = await get_answer(self.my_dict,self.bot,self.event,3)
        result = result[int(sel)]
        self.have_bless.remove(result)
        self.all_bless.append(result.replace("_2", ""))
    async def dir_end(self, prob):
        rand = random.randint(1, 100)
        if rand < prob:
            msg_merge(self.my_dict,"模拟结束,开始结算------------")
            msg_merge(self.my_dict,"奇物列表", self.have_qiwu_list)
            msg_merge(self.my_dict,"祝福列表", self.have_bless)
            msg_merge(self.my_dict,"宇宙碎片", self.gold)
            msg_merge(self.my_dict,"湮灭烛剪层数", self.yanmie_zhujian)
            await push_msg(self.bot, self.event, self.my_dict["log"])
            return "1" + 1
            

    
    async def get_thing_bless(self, name, star, type=2, three_prob=0):
        gold_spend = 30 * self.xinyangzhaiquan_multi
        result = self.get_bless(name,star, type, three_prob=three_prob)
        msg_merge(self.my_dict,"请选择",result)
        if self.gold >= gold_spend:
            msg_merge(self.my_dict,f"3刷新,消耗{gold_spend}碎片,当前碎片{self.gold}, 012选择, 请选择")
            sel = await get_answer(self.my_dict,self.bot,self.event,4)
            if "3" in sel:
                result = self.get_bless(name,star, type,three_prob=three_prob)
                msg_merge(self.my_dict,"请选择(012)",result)
                sel_1 = await get_answer(self.my_dict,self.bot,self.event,3)
                result = result[int(sel_1)]
                self.choose_bless(result)
                self.gold -= gold_spend
            else:
                result = result[int(sel)]
                self.choose_bless(result)
        else:
            msg_merge(self.my_dict,"输入(012)")
            sel = await get_answer(self.my_dict,self.bot,self.event,3)
            result = result[int(sel)]
            self.choose_bless(result)            
    async def get_thing_qiwu(self, is_neg=0):
        if is_neg == 0:
            result = random.sample(self.normal_qiwu_list, 3)
            msg_merge(self.my_dict,"请选择(012)",result)
            sel = await get_answer(self.my_dict,self.bot,self.event,3)
            self.have_qiwu_list.append(result[int(sel)])
            self.normal_qiwu_list.remove(result[int(sel)])
        else:
            result = random.choice(self.negative_qiwu_list)
            msg_merge(self.my_dict,"获得",result)
            self.have_qiwu_list.append(result)
            self.negative_qiwu_list.remove(result)      
    async def trigger_thing(self, name=None, type = 0):
        _thing_list = []
        if type == 0:
            _thing_list = self.normal_thing_list
        elif type == 1:
            _thing_list = self.come_across_ting_list
        else:
            _thing_list = self.trade_thing_list    
        if name == None:           
            sel = random.choice(_thing_list)
            for i in self.all_instance_thing_list:
                if i.name == sel:
                    await i.use(self)
        else:
            for i in self.all_instance_thing_list:
                if i.name == name:
                    await i.use(self)            
                   
            
            
            
            
        
      