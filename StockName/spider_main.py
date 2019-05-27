# coding:utf8
import url_manager, html_downloader, html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        #self.outputer.outoupt_html_header()
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' %(count,new_url)
                html_cont = self.downloader.download(new_url)
                #print html_cont
                new_data = self.parser.parse(new_url,html_cont)
                #self.urls.add_new_urls(new_urls)
                #self.outputer.collect_data(new_data)
                print new_data
                count =count +1
                if count == 1:
                    break
                #self.outputer.outoupt_html(1)
        except Exception as e:
            print e.message
            print "craw fail"
            
            
        self.outputer.outoupt_html_ender()
    

if __name__ == "__main__":
    root_url =  "http://quote.eastmoney.com/stocklist.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)