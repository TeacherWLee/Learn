"""
# 明确目的
# 找到数据对应的网页
# 分析网页的结构找到数据所在的标签位置

# Step1：模拟HTTP请求，向服务器发送请求，获取服务器返回的HTML数据
# Step2：用正则表达式提取我们要的数据（名字，人气）
"""
import re
from urllib import request


url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.5ddadrilvua'

# url = 'https://www.panda.tv/cate/dota1?pdt=1.c_lol.psbar-ca0.5.2hso37lm6hk'


def fetch_content():
    r = request.urlopen(url)
    html_str = r.read()
    html_str = str(html_str, encoding='utf-8')
    return html_str


def analyse_html_ele(analysis_str):
    pattern = '<div class="video-info">([\\s\\S]*?)</div>'
    return re.findall(pattern, analysis_str)


def analyse_nickname_ele(analysis_str):
    pattern = '<span class="video-nickname"([\\s\\S]*?)</span>'
    rst = re.findall(pattern, analysis_str)[0]
    pattern = '</i>([\\S\\s]*)'
    rst = re.findall(pattern, rst)[0]
    rst = rst.strip()
    # pattern = '[ \n]'
    # rst = re.sub(pattern, '', rst)
    return rst


def analyse_number_ele(analysis_str):
    pattern = '<span class="video-number">([\\s\\S]*?)</span>'
    rst = re.findall(pattern, analysis_str)[0]
    pattern = '</i>([\S\s]*)'
    rst = re.findall(pattern, rst)[0]
    return rst


def anchors_number_sort_seed(anchor):
    # return anchor['number']     # 错误示例1
    r = re.findall('\d*', anchor['number'])
    number = float(r[0])
    if '万' in anchor['number']:
        number *= 10000
    return number


def anchors_number_sort(anchors):
    anchors = anchors.sort(key=anchors_number_sort_seed, reverse=True)
    return anchors


def show_data(anchors):
    for i in range(0, len(anchors)):
        print('NO.' + str(i+1) + ': '
              + anchors[i]['name'] + '--'
              + anchors[i]['number']
              )
    # for anchor in anchors:
    #     print(anchor['name'] + ' ----> ' + anchor['number'])

    # map(lambda anchor: {
    #     print(anchor['name'] + ' ----> ' + anchor['number'])
    # }, anchors)


def go():
    # 爬虫 1.获取HTML数据 -> 2.提取关键数据
    html_str = fetch_content()
    all_video_info_ele = analyse_html_ele(html_str)
    anchors = []
    for video_info_ele_str in all_video_info_ele:
        name = analyse_nickname_ele(video_info_ele_str)
        number = analyse_number_ele(video_info_ele_str)
        anchors.append({'name': name, 'number': number})

    # 业务处理 1.排序 -> 2.可视化
    anchors_number_sort(anchors)
    show_data(anchors)


if __name__ == '__main__':
    go()


'''
第三方爬虫：BeautifulSoap、Scrapy
爬虫、反爬虫、反反爬虫
IP被封，代理IP库
'''
