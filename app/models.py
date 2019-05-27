'''
Models used in Remember
'''
from flask_sqlalchemy import SQLAlchemy

from app import app


db = SQLAlchemy(app)    

class StockName(db.Model):
    '''
    this is StockName model
    '''
    __tablename__ = "StockName"
    id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(100))
    link = db.Column(db.String(100))
    stockid =db.Column(db.String(100))
    selfchoose = db.Column(db.Boolean, default=False)

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __repr__(self):
        return "<StockName %r>" % self.name
		
class StockDaily(db.Model):
    '''
    this is StockDaily model
    '''
    __tablename__ = "StockDaily"
    id = db.Column(db.Integer, primary_key=True)    
    ts_code = db.Column(db.String(10))
    trade_date = db.Column(db.String(10))
    open =db.Column(db.Float(100))
    high = db.Column(db.Float(100))
    low = db.Column(db.Float(100))
    close =db.Column(db.Float(100))
    pre_close = db.Column(db.Float(100))
    change = db.Column(db.Float(100))
    pct_chg =db.Column(db.Float(100))
    vol = db.Column(db.Float(100))
    amount = db.Column(db.Float(100))

 

    def __init__(self):
        pass


    def __repr__(self):
        return "<StockDaily>"
