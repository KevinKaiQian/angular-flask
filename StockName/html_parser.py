# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import re
import urlparse



class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        try:
            
            new_urls = set()
            links =soup.find_all('a',href = re.compile(r"/item/\w+"))
            
            for link in links:
                new_url = link['href']
                new_full_url = urlparse.urljoin(page_url,new_url)
                new_urls.add(new_full_url)
            return new_urls
        
        except Exception as e:
            print e.message
        
    
    
    def _get_new_data(self, page_url, soup):

        res_data = []

        links = soup.find_all('a',href=re.compile(r'http://quote.eastmoney.com/\w\w\d{6}.html'),limit=10000)
        #print len(links)
        for link in links:

            result =re.findall(r'http://quote.eastmoney.com/(s[h,z][0,3,6]0\d{4}).html', link['href'])

            if(result):
                if link.get_text().encode('utf-8')== "": name = "NoName"
                else:name =link.get_text().encode('utf-8').split("(")[0]

                res_data.append([result[0][2:],name,link['href']])

        return res_data
        

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html5lib',from_encoding='gb2312')
        #soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='gb2312')
        #new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        new_urls= None
        return new_urls,new_data






