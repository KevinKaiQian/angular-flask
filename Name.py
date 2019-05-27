# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from StockName import url_manager, html_downloader, html_parser,html_outputer


import os
import exception
from db import model

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)

        #try:
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print 'craw %d : %s' %(count,new_url)
            html_cont = self.downloader.download(new_url)

            new_urls,new_data = self.parser.parse(new_url,html_cont)
            #self.urls.add_new_urls(new_urls)
            print new_data
            try:
                sto=model.StockNameList()
                sto.collect_data(new_data)
            except exception.DataBaseException as e:
                print e.message
            except exception as e:
                print e.message

            count =count +1
            if count == 1:break
        #except Exception as e:
        #    print "craw fail"

if __name__ == "__main__":

    root_url = "http://quote.eastmoney.com/stock_list.html"
    #root_url = "http://data.eastmoney.com/stockcomment/mkt/0.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

'''
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, DECIMAL,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_BASE_DIR = os.path.join(BASE_DIR, "db")
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(DB_BASE_DIR, "app.db")

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

from db import model

class StockNameList():
    def __init__(self):

        self.method_dict = {  

        '__tablename__':'StocKName', 
        'id' : Column(Integer, primary_key=True,autoincrement=True),
        'name' : Column(String(100)), 
        'stockid' : Column(String(100)),
        'link' :  Column(String(100)),
        'selfchoose' : Column(Boolean, default=False),

        }
        self.table_id = 'StocKName'
    @staticmethod
    def collect_data(obj,data):
        try:
            obj.Create(Clean=True)
            obj.Insert(data)
        except exception as e:
            raise exception.DataBaseException(reason='can not insert data to database')
    def Create(self,Clean= False):
        self.table=type(self.table_id, (Base,), self.method_dict)
        Base.metadata.create_all(engine)
        if Clean == True:Base.metadata.clear()
        Base.metadata.create_all(engine)
    def update(self):
        self.session = DBSession()
        # 创建新User对象:
        new_user = self.table(id='2')
        # 添加到session:
        self.session.add(new_user)
        # 提交即保存到数据库:
        self.session.commit()
        # 关闭session:
        self.session.close()
    def Query(self,stockid):
        session = DBSession()
        user = session.query(self.table).filter(self.table.stockid ==stockid).first()
        session.close()
        return user
    def Insert(self,Params):
        self.session = DBSession()
        # 创建新User对象:
        for Param in Params:
            if self.Query(Param[0]):continue
            new_user = self.table(name=Param[1].decode('utf-8'),stockid=Param[0],link=Param[2])
            # 添加到session:
            self.session.add(new_user)
            # 提交即保存到数据库:
        self.session.commit()
        # 关闭session:
        self.session.close()
'''