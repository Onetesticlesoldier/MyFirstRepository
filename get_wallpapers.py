#导入第三方库
import requests #爬虫
import re #正则表达式
import os #文件操作

#壁纸主站(英文)：https://wallhaven.cc/
#网站页面基于ajax协议动态刷新

#获取网站整页url模板
def get_url(base_url):
    keyword=input("请输入搜索的英文关键词:(爬取排行榜请输入toplist)") #输入关键词
    if keyword=='toplist': #获取排行榜的url
        base_url=base_url+keyword+'?page='
    else: #获取搜索的url
        base_url=base_url+'search?q='+keyword+'&page='
    return base_url

#获取图片初步的url并存在一个列表中
def get_img_url(base_url):
    header={ 
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    } #模拟浏览器头部
    img_url_list=[] #创建一个空列表
    page_num=input("请输入下载页数:(一页24张)") #输入下载页数
    for num in range(1,int(page_num)+1):
        new_url=base_url+str(num) #page=1,page=2,······
        page_text=requests.get(url=new_url,headers=header).text #获取url源代码
        ex='<a class="preview" href="(.*?)"' 
        img_url_list+=re.findall(ex,page_text,re.S) #利用正则表达式从源代码中截取图片url(初步)并存放在一个列表中 https://wallhaven.cc/w/q26x6q
    return img_url_list

#完善图片url并下载图片，存放在一个文件夹中
def download_img(img_url_list):
    header={ 
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    } #模拟浏览器头部
    keyword=input("请再次输入关键词以方便创建文件夹:")
    if not os.path.exists('./wallpapers'):     #在当前目录下创建一个文件夹保存所有图片
        os.mkdir('./wallpapers')
    path='./wallpapers/'+keyword
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(len(img_url_list)): #完善图片url https://w.wallhaven.cc/full/q2/wallhaven-q26x6q.jpg 注：jpg或png结尾
        x=img_url_list[i].split('/')[-1]  #获取图片的初步url结尾的数据
        a=x[0]+x[1] #获取x的前两位
        img_url='https://w.wallhaven.cc/full/'+a+'/wallhaven-'+x+'.jpg' #拼接图片的完整url,先默认jpg结尾
        code=requests.get(url=img_url,headers=header).status_code 
        if code==404: #若网页返回值为404，则为png结尾
            img_url='https://w.wallhaven.cc/full/'+a+'/wallhaven-'+x+'.png'
        img_data=requests.get(url=img_url,headers=header,timeout=20).content #获取图片二进制数据,加入timeout限制请求时间
        img_name=img_url.split('-')[-1] #生成图片名字
        img_path=path+'/'+img_name #生成图片存储路径
        with open(img_path,'wb') as fp: #('w':写入,'b':二进制格式)
            fp.write(img_data)
            print(img_name,'下载成功')

#主函数
def main(url):
    base_url=get_url(url) #获取网站整页url模板
    img_url_list=get_img_url(base_url) #获取图片初步的url并存在一个列表中
    #print(img_url_list)
    download_img(img_url_list) #完善图片url并下载图片，存放在一个文件夹中

#调用主函数
main('https://wallhaven.cc/')

#网站本身加载就慢，所以爬取壁纸时也很慢，需要耐心等待