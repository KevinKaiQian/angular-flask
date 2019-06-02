# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from data import http
import json
import time
class daily_data(object):
    header = {'api_name': 'daily',
              'token': 'f054de446f8cbcd1375f1a372f88bb130137e2c8659ad7ea37b32fd9',
              'params': {
                  'ts_code': '000001.SZ',
                  'start_date': '20180701',
                  'end_date': '20180718',
                  'fields': 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount',
                }
              }
    def __init__(self):

        self.header['api_name']="daily"

    def collect_data(self,start_date=None,end_date=None,ts_code=None):
        if ts_code == None:self.header['params']['ts_code']="600000"
        else:self.header['params']['ts_code']=ts_code

        if start_date==None:self.header['params']['start_date']="20020101"
        else:self.header['params']['start_date']=start_date

        if end_date == None:self.header['params']['end_date']=str(time.strftime("%Y%m%d", time.localtime()))
        else:self.header['params']['end_date']=end_date
        self.jdata = json.dumps(self.header)
        return http.http_post_data(header=self.jdata)


