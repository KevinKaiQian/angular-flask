# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, DECIMAL ,Boolean,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import exception



BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#DB_BASE_DIR = os.path.join(BASE_DIR, "db")
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

class StockNameList():
    def __init__(self):
        self.method_dict = {
            '__tablename__' :'StocKName',
            'id' : Column(Integer, primary_key=True ,autoincrement=True),
            'name' : Column(String(100)),
            'stockid' : Column(String(100)),
            'link' :  Column(String(100)),
            'selfchoose' : Column(Boolean, default=False),
        }
        self.table_id = 'StocKName'
        self.__Create()
    def collect_data(self ,data):
        try:
            self.Insert(data)
        except exception as e:
            raise exception.DataBaseException(reason='can not insert data to database')
    def __Create(self ):
        Base.metadata.clear()
        self.table=type(self.table_id, (Base,), self.method_dict)
        Base.metadata.create_all(engine)
        self.session = DBSession()

    def update(self):
        new_user = self.table(id='2')
        self.session.add(new_user)
        self.session.commit()
    def Query(self ,stockid):
        user = self.session.query(self.table).filter(self.table.stockid==stockid).first()
        return user
    def Insert(self ,Params):
        for Param in Params:
            if self.Query(Param[0]) :continue
            new_user = self.table(name=Param[1].decode('utf-8') ,stockid=Param[0] ,link=Param[2])
            self.session.add(new_user)
        self.session.commit()
    def __del__(self):
        self.session.close()



class StockDaily():
    def __init__(self, table_id):
        self.method_dict = {
            '__tablename__': 'default',
            'id': Column(Integer, primary_key=True, autoincrement=True),
            'ts_code':  Column(String(10)),
            'trade_date': Column(String(10)),
            'open': Column(Float(10)),
            'high': Column(Float(10)),
            'low': Column(Float(10)),
            'close': Column(Float(10)),
            'pre_close': Column(Float(10)),
            'change': Column(Float(10)),
            'pct_chg': Column(Float(10)),
            'vol': Column(Float(10)),
            'amount': Column(Float(10)),

        }
        self.method_dict['__tablename__'] = "Stock"+str(table_id)
        self.table_id = str(table_id)
        self.__Create()

    def collect_data(self,data):
        try:
            self.Insert(names=data['fields'],values=data['items'])
        except exception as e:
            raise exception.DataBaseException(reason='can not insert data to database')
    def query_kdj_data(self):
        data = self.session.query(self.table.trade_date,self.table.open,self.table.close,self.table.low,self.table.high).all()
        if data :
            return  data
        else:
            return None
    def __Create(self):
        Base.metadata.clear()
        self.table = type(self.table_id, (Base,), self.method_dict)
        Base.metadata.create_all(engine)
        self.session = DBSession()

    def update(self):
        new_user = self.table(id='2')
        self.session.add(new_user)
        self.session.commit()

    def Query(self, trade_date=''):

        user = self.session.query(self.table).filter(self.table.trade_date == trade_date).first()
        return user

    def Insert(self, names, values):
        for value in values:
            if self.Query(trade_date= value[1]):
                continue
            ref = self.table()
            for num in range(len(names)):
                setattr(ref,names[num],value[num])
            self.session.add(ref)
        self.session.commit()


    def __del__(self):
        self.session.close()
        #print "close"