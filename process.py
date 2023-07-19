from .qiwu import get_all_qiwu_list
from .thing import get_all_thing_list
import random
import sys
from .msg_utils import *
from .pic_utils import *
from .json_util import *

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
        for i in range(len(self.all_instance_qiwu_list)):
            if self.all_instance_qiwu_list[i].broke_count < 1:
                for j in new_instance_qiwu:
                    if self.all_instance_qiwu_list[i].name == j.name and "火漆" not in j.name and "测不准" not in j.name:
                        self.all_instance_qiwu_list[i] = j
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
            if "存护" in i:
                kind_0.append(i)
            if "记忆" in i:
                kind_1.append(i)
            if "虚无" in i:
                kind_2.append(i)                             
            if "丰饶" in i:
                kind_3.append(i)
            if "巡猎" in i:
                kind_4.append(i)
            if "毁灭" in i:
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
        for i in star_list[:]:
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
                [im for category in all_kind_bless for im in category],  # 平铺刻印列表
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
                return_list.append(upgrade_bless + "_2")
                need_upgrade_list.remove(upgrade_bless)
                for j in need_upgrade_list:
                    return_list.append(j)
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
    async def upgrade_bless(self, name="随机", star="随机"):
        
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
            if self.gold >= gold_need * gold_multi * self.xinyangzhaiquan_multi:     
                self.have_bless.remove(_upgrade_bless)
                self.have_bless.append(_upgrade_bless + "_2")
                self.gold -= gold_need * gold_multi * self.xinyangzhaiquan_multi
            if name == "随机":
                msg_merge(self.my_dict,"强化结果", _upgrade_bless)
                await push_image(self.my_dict, self.bot, self.event, pic2b64(make_choose_bless_card([_upgrade_bless, _upgrade_bless + "_2"], self.gold)))
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
            harm_0 = self.cal_harm(0)
            harm_1 = self.cal_harm(0)
            if harm_0[0] > harm_1[0]:
                msg_merge(self.my_dict, harm_0[1])
                record_harm(self.event, harm_0[0])
            else:
                msg_merge(self.my_dict, harm_1[1])
                record_harm(self.event, harm_1[0])               
            msg_merge(self.my_dict,"湮灭烛剪层数", self.yanmie_zhujian)
         
            log = self.my_dict["log"]
            msg = self.my_dict["msg"]
            log += msg
            self.my_dict["log"] = log

            await push_msg(self.bot, self.event, self.my_dict["log"])
            
            return "1" + 1
            

    
    async def get_thing_bless(self, name, star, type=2, three_prob=0):
        gold_spend = 30 * self.xinyangzhaiquan_multi
        result = self.get_bless(name,star, type, three_prob=three_prob)
        msg_merge(self.my_dict,"请选择",result)
        await push_image(self.my_dict, self.bot, self.event, pic2b64(make_choose_bless_card(result, self.gold)))
        if self.gold >= gold_spend:
            msg_merge(self.my_dict,f"3刷新,消耗{gold_spend}碎片,当前碎片{self.gold}, 012选择, 请选择")
            sel = await get_answer(self.my_dict,self.bot,self.event,4)
            if "3" in sel:
                result = self.get_bless(name,star, type,three_prob=three_prob)
                msg_merge(self.my_dict,"请选择(012)",result)
                await push_image(self.my_dict, self.bot, self.event, pic2b64(make_choose_bless_card(result, self.gold)))
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
                    _thing_list.remove(sel)
        else:
            for i in self.all_instance_thing_list:
                if i.name == name:
                    await i.use(self)            
                    self.all_instance_thing_list.remove(i)
    def cal_harm(self, life_sel):
        with open(info_dir, "r", encoding= "utf-8") as f:
            info = json.load(f)        
        life_recover_role = 0#角色回血量
        addition_harm = 0#附加伤害
        attack = 2500#
        attack_basis = 2500
        attack_enemy = 5000
        attack_beilv = 1#攻击力倍率
        attack_enemy_dec_beilv = 1

        zhuijia_beilv = 5
        continue_harm_beilv = 1#持续伤害倍率
        crit_harm = 2
        continue_harm = 0#持续伤害
        crit_rate = 0.5
        crit_rate_zhuijia = 0
        defense = 3000#防御力
        defense_basis = 3000
        easy_hurt = 1
        easy_hurt_continue = 1
        end_beilv = 5
        end_zhuijia_beilv = 0
        fanzhen = 0#反震伤害
        harm_beilv = 0#追加 终结共同倍率
        huiwei = 0#回味伤害
        huiwei_beilv = 1
        huiwei_count = 0
        huixin_limit = 0#会心上限
        jipo = 0#击破特攻, 50%加成瞬间击破伤害， 50%加成持续伤害
        lieshang_beilv = 0
        life_basis = 5000#基础生命
        life_enemy = 150000

        life_now = 0#当前生命
        life_recover = 0#回血量
        life = 8000#生命上限
        lishen_beilv = 1#离神伤害的倍率
        lishen_multi = 1#离神伤害额外x区
        lishen_multi_1 = 1#额外x区
        shield = 0
        shield_add = 0
        shield_all = 0
        shield_role = 0#角色提供的护盾量
        shield_role_beilv = 1
        
        suspect_count = 0
        xiaolv_continue = 1#持续伤害加成
        xiaolv_huixin = 1#会心效果加成
        xiaolv_life = 0#回血效果加成
        xiaolv_shield = 1#护盾增加加成
        xiaolv_zhanyi = 1#战意效果加成
        xiaolv_zhulu = 1#zhulu回复量加成
        zhanyi_limit = 0#战意上限
        zhuijia_addition = 0#追加伤害附加伤害
        zhuijia_harm_beilv = 1
        zhulu = 0#zhulu存储量&伤害
        zhulu_beilv = 1#zhulu伤害倍率
        lishen_have = 0
        msg = ""
        qiwi_num = len(self.have_qiwu_list)
        harm_beilv += 0.05 * qiwi_num
        if "纯美之袍" in self.have_qiwu_list:
            harm_beilv += self.gold // 100 * 0.16
        if "没有注释的代码" in self.have_qiwu_list:
            harm_beilv += 0.35
        if "虫网" in self.have_qiwu_list:
            attack += attack_basis * 0.5
        harm_beilv += self.yanmie_zhujian * 0.03
        #--------------------------------------
        #--------------------------------------

        #生命上限优先加 其次是防御力，然后是护盾，然后是攻击力，然后是治疗量
        for j in range(6):
            locals_dict = locals()
            locals_dict["info"] = {}
            for i in self.have_bless:
                temp = i.split("_")
                type = temp[2]
                name = temp[3]

                if info[type][name]["4"] == j:
                    if len(temp) == 4:
                        sel = "2"
                    else:
                        sel = "3"
                    exec(info[type][name][sel], globals(),locals_dict)
                    
                try:
                    exec(func_result, globals(), locals_dict)
                    
                except Exception as e:
                    pass
# region
                zhulu = locals_dict["zhulu"]
                life_recover_role = locals_dict["life_recover_role"]
                addition_harm = locals_dict["addition_harm"]
                attack = locals_dict["attack"]
                attack_basis = locals_dict["attack_basis"]
                attack_enemy = locals_dict["attack_enemy"]
                attack_beilv = locals_dict["attack_beilv"]
                attack_enemy_dec_beilv = locals_dict["attack_enemy_dec_beilv"]
                zhuijia_beilv = locals_dict["zhuijia_beilv"]
                continue_harm_beilv = locals_dict["continue_harm_beilv"]
                crit_harm = locals_dict["crit_harm"]
                continue_harm = locals_dict["continue_harm"]
                crit_rate = locals_dict["crit_rate"]
                crit_rate_zhuijia = locals_dict["crit_rate_zhuijia"]
                defense = locals_dict["defense"]
                defense_basis = locals_dict["defense_basis"]
                easy_hurt = locals_dict["easy_hurt"]
                easy_hurt_continue = locals_dict["easy_hurt_continue"]
                end_beilv = locals_dict["end_beilv"]
                end_zhuijia_beilv = locals_dict["end_zhuijia_beilv"]
                fanzhen = locals_dict["fanzhen"]
                harm_beilv = locals_dict["harm_beilv"]
                huiwei = locals_dict["huiwei"]
                huiwei_beilv = locals_dict["huiwei_beilv"]
                huiwei_count = locals_dict["huiwei_count"]
                huixin_limit = locals_dict["huixin_limit"]
                jipo = locals_dict["jipo"]
                lieshang_beilv = locals_dict["lieshang_beilv"]
                life_basis = locals_dict["life_basis"]
                life_enemy = locals_dict["life_enemy"]
                life_now = locals_dict["life_now"]
                life_recover = locals_dict["life_recover"]
                life = locals_dict["life"]
                lishen_beilv = locals_dict["lishen_beilv"]
                lishen_multi = locals_dict["lishen_multi"]
                lishen_multi_1 = locals_dict["lishen_multi_1"]
                shield = locals_dict["shield"]
                shield_add = locals_dict["shield_add"]
                shield_all = locals_dict["shield_all"]
                shield_role = locals_dict["shield_role"]
                shield_role_beilv = locals_dict["shield_role_beilv"]
                suspect_count = locals_dict["suspect_count"]
                xiaolv_continue = locals_dict["xiaolv_continue"]
                xiaolv_huixin = locals_dict["xiaolv_huixin"]
                xiaolv_life = locals_dict["xiaolv_life"]
                xiaolv_shield = locals_dict["xiaolv_shield"]
                xiaolv_zhanyi = locals_dict["xiaolv_zhanyi"]
                xiaolv_zhulu = locals_dict["xiaolv_zhulu"]
                zhanyi_limit = locals_dict["zhanyi_limit"]
                zhuijia_addition = locals_dict["zhuijia_addition"]
                zhuijia_harm_beilv = locals_dict["zhuijia_harm_beilv"]
                lishen_have = locals_dict["lishen_have"] 
# endregion         
            if j == 0:#战意,会心
                # 战意
                defense += defense_basis * 0.03 * zhanyi_limit * xiaolv_zhanyi
                
                attack += attack_basis * 0.03 * zhanyi_limit * xiaolv_zhanyi
                #会心
                crit_rate += huixin_limit * 0.06 * xiaolv_huixin
                crit_harm += huixin_limit * 0.12 * xiaolv_huixin
                #持续伤害
                continue_harm = (20000 + life_enemy * 0.07 * lieshang_beilv) * xiaolv_continue
                
                
            if j == 1:#防御力,会心,当前血量
                shield_role = defense * 0.5
                shield_role *= shield_role_beilv
                shield_add += shield_role
                shield_all = shield_add * 4
                shield = shield_add * (1 + xiaolv_shield)
                if life_sel == 0:
                    life_now = life
                else:
                    life_now = life * 0.01
                easy_hurt += suspect_count * 0.01 
            if j == 2:#攻击力,治疗量(血量100% 攻击力100%)
                attack *= attack_beilv
                life_recover_role += life + attack
                life_recover += life_recover_role * 4
            
            if j == 4:
                attack_enemy *= attack_enemy_dec_beilv

        #必杀期望伤害 = (攻击力 * 必杀倍率 * 暴伤 * 暴击率 + 攻击力 * 必杀倍率 * (1 - 暴击率) ) * (通用伤害加成 + 追加必杀技) * 易伤
        end_harm = (attack * end_beilv + addition_harm + zhulu* zhulu_beilv + fanzhen) * (crit_harm * crit_rate + (1 - crit_rate)) * (1 + harm_beilv + end_zhuijia_beilv)  * easy_hurt
        msg += f" 必杀期望伤害 {int(end_harm)}"
        #追加期望伤害 =  (攻击力 * 必杀倍率 + 追加附加 + 回味) * (爆伤 * (暴击率 + 追加暴击率) + (1 - 暴击率 - 追加暴击率)) * (通用伤害加成 + 追加伤害加成) * 易伤
        zhuijia_harm = (attack * zhuijia_beilv + zhuijia_addition + huiwei * huiwei_beilv) * (crit_harm * (crit_rate_zhuijia + crit_rate) + (1 - crit_rate - crit_rate_zhuijia)) * (1 + zhuijia_harm_beilv + harm_beilv) * easy_hurt
        msg += f" 追加期望伤害 {int(zhuijia_harm)}"
        #击破伤害 = 10000 * 击破特攻 * 易伤
        jipo_harm = 10000 * (1 + jipo) * easy_hurt
        msg += f" 击破伤害 {int(jipo_harm)}"
        #持续伤害 = 持续伤害 * 持续伤害易伤 * 持续伤害加成 * 易伤
        continue_harm = continue_harm * easy_hurt_continue * (continue_harm_beilv + jipo) * easy_hurt
        msg += f" 持续伤害 {int(continue_harm)}"
        #离神伤害 = 离神 * 易伤 * 其他
        lishen_harm = lishen_have * life_enemy * 0.3 * lishen_beilv * lishen_multi * lishen_multi_1 * easy_hurt
        msg += f" 离神伤害 {int(lishen_harm)}"
        msg += f" 总伤害 {int(end_harm + zhuijia_harm + jipo_harm + continue_harm + lishen_harm)}"
        
        return int(end_harm + zhuijia_harm + jipo_harm + continue_harm + lishen_harm), msg
        
    
    

def count_bless_num(type, level, bless_list: list):
    num = 0
    for i in bless_list:
        if type in i:
            num += 1
    data = {
        "存护": {
            "1": f"defense += defense_basis * 0.6 * 6 if {num} > 6 else defense_basis * 0.6 * {num}",
            "2": f"defense += defense_basis * 0.8 * 9 if {num} > 9 else defense_basis * 0.8 * {num}"
        },
        "记忆": {
            "1": f"lishen_beilv += 0.08 * 6 if {num} > 6 else 0.08 * {num}",
            "2": f"lishen_beilv += 0.08 * 9 if {num} > 9 else 0.10 * {num}"
        }, 
        "虚无": {
            "1": f"continue_beilv += 0.06 * 6 if {num} > 6 else 0.06 * {num}",
            "2": f"continue_beilv += 0.08 * 9 if {num} > 9 else 0.08 * {num}"
        },  
        "丰饶": {
            "1": f"life += (life_basis * 0.05 * 6) if {num} > 6 else (life_basis * 0.05 * {num})",
            "2": f"life += (life_basis * 0.07 * 9) if {num} > 9 else (life_basis * 0.07 * {num})"
        }, 
        "巡猎": {
            "1": f"crit_harm += 0.04 * 6 if {num} > 6 else 0.04 * {num}",
            "2": f"crit_harm += 0.06 * 9 if {num} > 9 else 0.06 * {num}"
        },            
        "毁灭": {
            "1": f"attack += 0.05 * 6 if {num} > 6 else 0.05 * {num}",
            "2": f"attack += 0.07 * 9 if {num} > 9 else 0.07 * {num}"
        },    
        "欢愉": {
            "1": f"zhuijia_harm_beilv += 0.10 * 6 if {num} > 6 else 0.10 * {num}",
            "2": f"zhuijia_harm_beilv += 0.13 * 9 if {num} > 9 else 0.13 * {num}"
        },    
    }
    return data[type][level]            



      