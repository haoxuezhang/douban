import re
from douban import settings
import random
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from douban.items import DoubanItem ##这是我定义的需要保存的字段，（导入dingdian项目中，items文件中的DingdianItem类）
from douban.mysqlpipelines.sql import Sql


class Myspider(scrapy.Spider):
        

    name = 'douban'
#    allowed_domains = ['https://movie.douban.com']
    bash_url = 'https://movie.douban.com/tag/'
    headers = {
#        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#        "Accept-Language": "zh-CN,zh;q=0.8",
#        "Connection": "keep-alive",
        "Referer": "https://movie.douban.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(settings.USER_AGENTS)#'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'
    }


    def start_requests(self):
        yield Request(
            url = self.bash_url, 
            headers = self.headers,
            meta = {
                'cookiejar': 1
            },
            callback = self.parse)
#        yield Request('http://www.23wx.com/quanben/1', self.parse)
        

    def parse(self, response):
#        print(response.text)
        a_title = BeautifulSoup(response.text, 'lxml').find('table',class_='tagCol').find_all('a')
        for a in a_title:
            category_url = "https://movie.douban.com" + a['href']
            category = a.get_text()
            print(str(category_url))
            yield Request(
                url=category_url,
                headers = self.headers,
                meta = {
                    'cookiejar': response.meta['cookiejar'],
                    'category' : category,
                },
                callback = self.movie_page_url)
            
    def movie_page_url(self,response):
        print(response.url)
        max_num = BeautifulSoup(response.text,'lxml').find('div',class_='paginator').find_all('a')[-2].get_text()
        for i in range(0,int(max_num)):
            page_url = response.url+'?start='+str(i*20)+'&type=T'  #https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=7840&type=T
            yield Request(
                url=page_url,
                headers = self.headers,
                meta = {
                    'cookiejar': response.meta['cookiejar'],
                    'category' : response.meta['category'],
                },
                callback = self.get_movie_url)
    
    def get_movie_url(self,response):
        atitle2 = BeautifulSoup(response.text,'lxml').find_all('a',class_='nbg')
        for a in atitle2:
            movie_url = a['href']
            name=a['title']
            movie_id=movie_url[-9:-1]
            yield Request(
                url=movie_url,
                headers = self.headers,
                meta = {
                    'cookiejar': response.meta['cookiejar'],
                    'name':name,
                    'movie_id' : movie_id,
                    'category' : response.meta['category'],
                },
                callback = self.get_movie_info)
            
    def get_movie_info(self,response):
        item = DoubanItem()
        score = BeautifulSoup(response.text,'lxml').find('strong',class_='ll rating_num').get_text()
        #ulSoup(response.text,'lxml').find('div',id='info')
        item['name'] = response.meta['name']
        item['score'] = score
        item['movie_id']=response.meta['movie_id']
        item['category'] = response.meta['category']
        return item
        
        
        
        
        