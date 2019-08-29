"""
This file handles scraping and parsing Mandarin characters from https://hanzicraft.com.

Each character is downloaded into a cache if necessary, and then processed via beautiful
soup.
"""

import requests
import os
from bs4 import BeautifulSoup

DATA_DIRECTORY = 'data/'


def fetch_character_page(character):
    """Takes in a single chinese character and attempts to fetch the data from HanziCraft."""
    url = f"https://hanzicraft.com/character/{character}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")
    return response.text


def load_character(character):
    """Loads a character, checking the cache first."""
    character_file = f"{DATA_DIRECTORY}{character}.html"
    if not os.path.exists(character_file):
        content = fetch_character_page(character)
        with open(character_file, "w") as fout:
            fout.write(content)

    with open(character_file, "r") as fin:
        return fin.read()


def parse_character_data(character):
    soup = BeautifulSoup(load_character(character), 'html.parser')
    phonetic_clues = [
        x.text for x in soup.find(class_="phoneticinfo").findAll("li")
    ]
    radicals = [x.text for x in soup.find(text="Radical :").next.findAll("a")]
    return (phonetic_clues, radicals)


# Testing
ALL_CHARACTERS = "阿姨啊矮爱爱好安静八把爸爸吧白百班搬半办法办公室帮忙帮助包饱报纸杯子北方北京被本鼻子比比较比赛必须变化表示表演别别人宾馆冰箱不客气不才菜菜单参加草层茶差长唱歌超市衬衫成绩城市吃迟到出出现出租车厨房除了穿船春词语次聪明从错打电话打篮球打扫打算大大家带担心蛋糕但是当然到地的得灯等低弟弟地方地铁地图第一点电脑电视电梯电影电子邮件东东西冬懂动物都读短段锻炼对对不起多多么多少饿而且儿子耳朵二发烧发现饭馆方便房间放放心非常飞机分分钟服务员附近复习干净敢感冒刚才高高兴告诉哥哥个给跟根据更公共汽车公斤公司公园工作狗故事刮风关关系关心关于贵国家果汁过去过还还是孩子害怕汉语好好吃号喝和河黑黑板很红后面护照花动花园画坏欢迎还环境换黄回回答会会议火车站或者机场鸡蛋几乎机会极几记得季节家检查简单件健康见面讲教角脚叫教室接街道结婚结束节目节日姐姐解决借介绍今天进近经常经过经理九久旧就举行句子觉得决定咖啡开开始看看见考试渴可爱可能可以刻课客人空调口哭裤子块快快乐筷子来蓝老老师了累冷离离开里礼物历史脸练习两辆了解邻居零六楼路旅游绿妈妈马马上吗买卖满意慢忙猫帽子没没关系每妹妹门米米饭面包面条明白明天名字拿哪哪儿那那儿奶奶南男人难难过呢能你年年级年轻鸟您牛奶努力女儿女人爬山盘子旁边胖跑步朋友啤酒便宜票漂亮苹果葡萄普通话七妻子其实其他骑奇怪起床千铅笔钱前面清楚晴请秋去去年裙子然后让热热情人认识认为认真日容易如果三伞商店上上班上网上午少谁身体什么生病生气生日声音十时候时间使是世界事情手表手机瘦书舒服叔叔树数学刷牙双水水果水平睡觉说话司机四送虽然岁所以他她它太太阳糖特别疼踢足球题提高体育天气甜条跳舞听同事同学同意头发突然图书馆腿外完完成玩碗晚上万忘记喂为为了为什么位文化问问题我我们五西西瓜希望习惯洗洗手间洗澡喜欢下下午下雨夏先先生现在香蕉相同相信想向像小小姐小时小心笑校长些鞋写谢谢新新闻新鲜信星期行李箱姓兴趣熊猫休息需要选择学生学习学校雪颜色眼镜眼睛羊肉要求药要爷爷也一衣服医生医院一定一共一会儿一样以后以前以为已经椅子一般一边一起一直意思阴因为音乐银行应该影响用游戏游泳有有名又右边鱼遇到元远愿意月月亮越云运动在再再见早上怎么怎么样站张长丈夫着急找照顾照片照相机这这儿着真正在知道只中国中间中午终于种重要周末主要住祝注意准备桌子字字典自己自行车总是走最最近昨天左边坐做作业作用"
radical_count = {}
for char in ALL_CHARACTERS:
    (_, radicals) = parse_character_data(char)
    for radical in radicals:
        if radical not in radical_count:
            radical_count[radical] = 0
        radical_count[radical] += 1

print(sorted(list(radical_count.items()), key=lambda x: x[1]))