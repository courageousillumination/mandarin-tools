from os import path

from convertors import character_to_pinyin
from download_samples import download_samples
from export_anki import create_deck


class VocabTriad(object):
    def __init__(self, english, pinyin, character):
        self.english = english
        self.pinyin = pinyin
        self.character = character

        self.audio = self.load_audio()

    def load_audio(self):
        print(self.character, self.english)
        pinyin2 = character_to_pinyin(self.character)
        return download_samples(pinyin2, "data/")


def create_triad_from_string(data):
    split_data = data.split(":")
    return VocabTriad(split_data[0].strip(), split_data[1].strip(), split_data[2].strip())


vocab = """I : wǒ : 我
you : nǐ : 你
he : tā : 他
she : tā : 她
we : wǒmen : 我们
you (plural) : nǐmen : 你们
they : tāmen : 他们
to be : shì : 是
not : bù : 不
China : Zhōngguó : 中国
United States : Měiguó : 美国
teacher : lǎoshī : 老师
student : xuésheng : 学生
understand : dǒng : 懂
thank you : xièxie : 谢谢
you’re welcome : bú kèqi : 不客气
good : hǎo :好
goodbye : zàijiàn : 再见
possesive: de : 的
study : xué : 学
speak :  shuō : 说
read/see : kàn : 看
write : xiě : 写
know (a skill) : huì : 会
know (about something) : zhīdao : 知道
like : xǐhuan : 喜欢
want  : yào : 要
teach : jiāo : 教
listen / hear  : tīng : 听
a little : yìdiǎn : 一点
only : zhǐ : 只
also : yě : 也
and : hè : 和
big : dà : 大
small : xiǎo : 小
tall : gāo : 高
short : ǎi : 矮
beautiful : měi : 美
ugly : chǒu : 丑
good looking : hǎokàn : 好看
unattractive : nánkàn : 难看
happy : kuàilè : 快乐
sad : nánguò : 难过
fat : pàng : 胖
thin : shòu: 瘦
difficult : nán : 难
easy : róngyì :容易
intelligent : cōngmíng : 聪明
stupid : bèn : 笨
comparison : bǐ : 比
superlative : zuì : 最
music : yīnyuè : 音乐
to be in, at, or on : zài : 在
to live in : zhù zài : 住在
who : shéi : 谁
what : shénme : 什么
which : nǎ : 哪
where: nǎli : 哪里
there : nàli : 那里
here : zhèli : 这里
New York : Niǔyuē : 纽约
Chicago : Zhījiāgē : 芝加哥
San Francisco : Jiùjīnshān : 旧金山
correct : duì : 对
sorry : duìbuqǐ : 对不起
that’s ok : méi guānxi : 没关系
excuse me / may I ask : qǐngwèn : 请问
but : kěshì : 可是
family : jiā : 家
mother : māma : 妈妈
father : bàba : 爸爸
male : nán : 男
female : nǚ : 女
child : háizi : 孩子
older brother : gēge : 哥哥
younger brother : dìdi : 弟弟
older sister : jiějie : 姐姐
younger sister : mèimei : 妹妹
friend : péngyou : 朋友
boyfriend : nánpéngyou : 男朋友
girlfriend : nǚpéngyou : 女朋友
one : yī : 一
two : èr : 二
three : sān : 三
four : sì :四
five : wǔ : 五
six : liù : 六
seven : qī : 七
eight : bā : 八
nine : jiǔ : 九
ten : shì : 十
hundred : bǎi : 百
how many : jǐ : 几
years old : suì : 岁
all : dōu :都
relations / to matter : guānxi : 关系
meaning : yìsi :意思
interesting : yǒu yìsi : 有意思
measure word : ge : 个
Have : yǒu : 有
year : nián : 年
month : yuè : 月
number / date : hào : 号
week : xīngqī : 星期
sunday : Xīngqītiān : 星期天
morning : zǎoshang : 早上
middday : zhōngwǔ : 中午
afternoon : xiàwǔ : 下午
evening : wǎnshang : 晚上
o’clock : diǎn : 点
minutes : fēn : 分
now : xiànzài : 现在
today : jīntiān :今天
tomorrow : míngtiān : 明天
yesterday : zuótiān : 昨天
birthday : shēngrì : 生日
really : zhēn de : 真的
up : shàng : 上
down : xià : 下
go : qù : 去
movie : diànyǐng : 电影
TV : diànshì : 电视
eat : chī : 吃
rice / meal : fàn : 饭
make / do : zuò :做
drink : hē :喝
breakfast : zǎofàn : 早饭
lunch : wǔfàn :午饭
dinner : wǎnfàn : 晚饭
and : hái yǒu :还有
cat : māo : 猫
dog : gǒu : 狗
love : ài :爱
pig : zhū : 猪
this : zhè : 这
that : nà : 那
cow : niú : 牛
sheep : yáng : 羊
fish : yú : 鱼
chicken : jī : 鸡
bird : niǎo :鸟
pork : zhūròu : 猪肉
beef : niúròu :牛肉
bread : miànbāo : 面包
vegetable : shūcài : 蔬菜
tea : chá : 茶
coffee : kāfēi : 咖啡
alcohol : jiǔ : 酒
soda : kělè : 可乐
cup of (measure word ) : bēi :杯
plate of (measure word) : pán : 盘
milk : niúnǎi : 牛奶
cake : dàngāo : 蛋糕
egg : jīdàn :鸡蛋
how much : duōshǎo : 多少
money : qián : 钱
Yuan (colloquial) : kuài : 快
waiter : fúwùyuán :服务员 
dumplings : jiǎozi : 饺子
water : shuǐ : 水
bowl (measure word) : wǎn :碗
noodle : miàntiáo : 面条
soup : tāng : 汤
beer : píjiǔ : 啤酒
pair (measure word) : shuāng : 双
chopsticks : kuàizi : 筷子
fork : chāzi : 叉子
spoon : sháozi : 勺子
give : gěi : 给
please : qǐng : 请
restaurant : fànguǎn : 饭馆
supermarket : chāoshì : 超市
school : xuéxiào : 学校
office : bàngōngshì : 办公室
park : gōngyuán : 公园
bank : yínháng : 银行
airport : jīchǎng : 机场
shop : shāngdiàn : 商店
zero : líng : 零
this one / current one : zhègè : 这个
last : shànggè : 上个
next : xiàgè : 下个
hospital : yīyuàn : 医院
table : zhuōzi : 桌子
bed : chuáng : 床
on / above : shàngbiān : 上边
under / below : xiàbiān : 下边
inside : lǐbiān : 里边
east / east side : dōngbiān : 东边
west / west side : xībiān : 西边
south / south side : nánbiān : 南边
north / north side : běibiān : 北边
together : yīqǐ : 一起
sleep : shuìjiào : 睡觉
wake up : qǐchuáng : 起床
when : shénmeshíhòu : 什么时候
go to / start work : shàngbān : 上班
finish work : xiàbān : 下班
every day : měitiān : 每天
do what : gànshénme : 干什么
before : yǐqián : 以前
after : yǐhòu : 以后
often : chángcháng : 常常
brush teeth : shuāyá : 刷牙
wash : xǐ : 洗
face : liǎn : 脸
right away : mǎshàng :马上
hot : rè : 热
cold : lěng : 冷
hungry : è : 饿
thirsty : kě : 渴
bad : chà : 差
extremely : fēicháng : 非常
tasty (food) : hǎochī : 好吃
tasty (drinks) : hǎohē : 好喝
too much : tài ... le :太了
coat : wàitào : 外套
clothes : yīfu : 衣服
measure word for clothes (upper body) : jiàn : 件
pants : kùzi : 裤子
dress : qúnzi : 裙子
long : cháng : 长
short : duǎn : 短
measure word for long things : tiáo : 条
shoe : xiézi : 鞋子
shirt : chènshān : 衬衫
expensive : guì : 贵
cheap : piányì : 便宜
tired : lèi :累
full : bǎo : 饱
busy : máng : 忙
bored : wúliáo :无聊
nervous : jǐnzhāng : 紧张
comfortable : shūfu : 舒服
embarrassed : bù hǎoyìsi : 不好意思
excited : xīngfèn : 兴奋
happy : gāoxìng : 高兴
stomach : dùzi : 肚子
think / want : xiǎng : 想
bathe (shower or bath) : xǐzǎo : 洗澡
use internet : shàngwǎng : 上网
rest : xiūxi : 休息
computer : diànnǎo : 电脑
go home : huíjiā : 回家
drive a car : kāichē : 开车
time : shíjiān : 时间
early : zǎo : 早
late : wǎn : 晚 
problem : wèntí : 问题
I don’t care : wúsuǒwèi : 无所谓
there is no need : búyòng : 不用
let’s go : zǒu ba : 走吧
guest / customer : kèrén : 客人
to open : kāi :开
to close : guān : 关
dish / food : cài : 菜
menu : càidān : 菜单
bill (restaurants) : mǎidān : 买单
duck : yā : 鸭
tofu : dòfu :豆腐
cheers : gānbēi : 干杯
enjoy your meal : mànman chī : 慢慢吃
spicy : là : 辣
again, once more, another : zài : 再
white : báisè : 白色
black : hēisè : 黑色
red : hóngsè : 红色
green : lǜsè :绿色
yellow : huángsè : 黄色
toilet : xǐ shǒu jiān : 洗手间 
to shower : xǐzǎo : 洗澡
class : kè : 课
page : yè : 页
cell phone : shǒujī : 手机
phone number : diànhuà hàomǎ : 电话号码
far : yuǎn : 远
to wear : dài : 戴
shoes : xiézi : 鞋子
buy : mǎi : 买 
sell : mài : 卖
to stroll : guàng :逛
to wait : děng : 等
possible / can work : xíng : 行
borrow / lend money : jièqián : 借钱
train : hǔochē : 火车
bus : gōnggòng qìchē : 公共汽车
taxi : chūzūchē : 出租车
boat : chuán : 船
to walk : zǒu : 走
airplane : fēijī : 飞机
boring : wúliáo : 无聊
peaceful / quiet : ānjìng : 安静
left : zuǒ :左
right : yòu : 右
Kiss : wěn : 吻
Two (of something) : liǎng : 两
Can / Possible : kěyǐ : 可以
Thing : dōngxi : 东西
Book bag / Backpack : shūbāo : 书包
Book : shū : 书"""

triads = [create_triad_from_string(line) for line in vocab.split("\n")]
create_deck(triads)
