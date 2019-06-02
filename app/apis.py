'''
all the REST api implementations
'''

# -*- coding: utf-8 -*
import os
import uuid
import json

from data.daily import daily_data
from db import model
import werkzeug
from flask import abort, make_response, send_from_directory
from flask_restful import Api, Resource, reqparse, fields, marshal


from app import app, models
from app.models import db

import time

api = Api(app)  # pylint: disable=C0103

@api.representation("application/json")
def output_json(data, code, headers=None):
    '''
    convert the response data to json
    '''
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

@api.representation("application/xml")
def output_xml(data, code, headers=None):
    '''
    convert the response data to xml
    TODO: place holder to implement xml response
    '''
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

STOCK_FIELDS = {
    "id": fields.String,
    "name":fields.String,
    "link": fields.String,
    "stockid": fields.String,
    "selfchoose": fields.Boolean

}

STOCK_DETAIL_FIELDS = {
    "open": fields.Float,
    "close":fields.Float,
    "low": fields.Float,
    "high": fields.Float,
    "trade_date":fields.String,

}
class StockName(Resource):
    '''
    this is StockName resource
    '''
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type=unicode,
                                   required=True, help="No StockName name provided", location="json")
        self.reqparse.add_argument("link", type=unicode, default="", location="json")
        self.reqparse.add_argument("stockid", type=unicode, default="", location="json")
        self.reqparse.add_argument("selfchoose", type=bool, required=True, location="json")
        self.reqparse.add_argument("id", type=int, required=True, location="json")
        super(StockName, self).__init__()



    def put(self, stock_id):
        '''
        method to update task by task id
        '''
        stock = models.StockName.query.filter_by(id=stock_id).first()
        args = self.reqparse.parse_args()

        if not stock:
            abort(404)
        if args.has_key("stockid"):
            if args['stockid'][0]=="0" or args['stockid'][0]=="3":ts_code=args['stockid']+".SZ"
            else:ts_code=args['stockid']+".SH"
            res = daily_data().collect_data(end_date=str(time.strftime("%Y%m%d", time.localtime())),ts_code=ts_code)
            print res
            stod = model.StockDaily(args['stockid'])
            stod.collect_data(data=res)
            for arg_name, arg_value in args.items():
                if arg_value is not None:
                    setattr(stock, arg_name, arg_value)
            db.session.commit()

        return {"StockList": marshal(stock, STOCK_FIELDS)}

class StockNames(Resource):
    '''
    this is Task list resource
    '''
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("name", type=unicode,
                                   required=True, help="No StockName name provided", location="json")
        self.reqparse.add_argument("link", type=unicode, default="", location="json")
        self.reqparse.add_argument("stockid", type=unicode, default="", location="json")
        self.reqparse.add_argument("selfchoose", type=bool, required=True, location="json")
        self.reqparse.add_argument("id", type=int, required=True, location="json")
        super(StockNames, self).__init__()

        self.representations = {
            "application/xml": output_xml,
            "application/json": output_json,
        }
    def get(self):

        StockDatas = models.StockName.query.all()
        return  {"StockList": [marshal(StockData, STOCK_FIELDS) for StockData in StockDatas] }
    
    def put(self, stock_id):
        StockDatas = models.StockName.query.all()
        return {"StockList": [marshal(StockData, STOCK_FIELDS) for StockData in StockDatas] }


class StockDetail(Resource):
    '''
    this is StockName resource
    '''
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("ts_code", type=unicode,
                                   required=True, help="No ts_code name provided", location="json")
        self.reqparse.add_argument("trade_date", type=unicode, default="", location="json")
        self.reqparse.add_argument("open", type=float, default="", location="json")
        self.reqparse.add_argument("high", type=float, default="", location="json")
        self.reqparse.add_argument("low", type=float, default="", location="json")
        self.reqparse.add_argument("close", type=float, default="", location="json")
        self.reqparse.add_argument("pre_close", type=float, default="", location="json")
        self.reqparse.add_argument("change", type=float, default="", location="json")
        self.reqparse.add_argument("pct_chg", type=float, default="", location="json")
        self.reqparse.add_argument("vol", type=float, default="", location="json")
        self.reqparse.add_argument("amount", type=float, default="", location="json")


        super(StockDetail, self).__init__()
    def get(self,stock_id):
        stock = models.StockName.query.filter_by(id=stock_id).first()
        if not stock:
            abort(404)
        else:
            stod = model.StockDaily(stock.stockid)
            datas= stod.query_kdj_data()
            if datas == None : abort(404)


            #print sorted(datas, key=lambda d: int(d[0]), reverse=False)

            return  {"StockDaily":sorted(datas, key=lambda d: int(d[0]), reverse=False)}

'''
    def put(self, stock_id):
 
        stock = models.StockName.query.filter_by(id=stock_id).first()
        args = self.reqparse.parse_args()

        if not stock:
            abort(404)
        if args.has_key("stockid"):
            if args['stockid'][0]=="0" or args['stockid'][0]=="3":ts_code=args['stockid']+".SZ"
            else:ts_code=args['stockid']+".SH"
            res = daily_data().collect_data(end_date=str(time.strftime("%Y%m%d", time.localtime())),ts_code=ts_code)

            stod = model.StockDaily(args['stockid'])
            stod.collect_data(data=res)
            for arg_name, arg_value in args.items():
                if arg_value is not None:
                    setattr(stock, arg_name, arg_value)
            db.session.commit()

        return {"StockDaily": marshal(stock, STOCK_FIELDS)}
'''

class StockDetails(Resource):
    '''
    this is Task list resource
    '''
    #decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("ts_code", type=unicode,
                                   required=True, help="No ts_code name provided", location="json")
        self.reqparse.add_argument("trade_date", type=unicode, default="", location="json")
        self.reqparse.add_argument("open", type=float, default="", location="json")
        self.reqparse.add_argument("high", type=float, default="", location="json")
        self.reqparse.add_argument("low", type=float, default="", location="json")
        self.reqparse.add_argument("close", type=float, default="", location="json")
        self.reqparse.add_argument("pre_close", type=float, default="", location="json")
        self.reqparse.add_argument("change", type=float, default="", location="json")
        self.reqparse.add_argument("pct_chg", type=float, default="", location="json")
        self.reqparse.add_argument("vol", type=float, default="", location="json")
        self.reqparse.add_argument("amount", type=float, default="", location="json")
        super(StockDetails, self).__init__()

        self.representations = {
            "application/xml": output_xml,
            "application/json": output_json,
        }
    def get(self):

        StockDatas = models.StockName.query.filter_by(selfchoose=True).all()

        return  {"StockDailys": [marshal(StockData, STOCK_FIELDS) for StockData in StockDatas] }


class Macroeconomics(Resource):
    '''
    this is Task list resource
    '''

    # decorators = [auth.login_required]

    def __init__(self):
        #self.reqparse = reqparse.RequestParser()

        super(Macroeconomics, self).__init__()

        self.representations = {
            "application/xml": output_xml,
            "application/json": output_json,
        }

    def get(self):
        StockDatas = models.StockName.query.filter_by(selfchoose=True).all()

        return {"Macroeconomics": []}


api.add_resource(StockNames,
                 "/stock/api/v1.0/StockNames",
                 endpoint="ep_stocks")

api.add_resource(StockName,
                 "/stock/api/v1.0/StockNames/<int:stock_id>",
                 endpoint="ep_stock")
api.add_resource(StockDetails,
                 "/stock/api/v1.0/StockDetails",
                 endpoint="ep_stockdetails")

api.add_resource(StockDetail,
                 "/stock/api/v1.0/StockDetails/<int:stock_id>",
                 endpoint="ep_stockdetail")

api.add_resource(Macroeconomics,
                 "/stock/api/v1.0/EconomicData",
                 endpoint="ep_Macroeconomics")