# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from data.daily import daily_data
from db import model


res=daily_data().collect_data(end_date="20190524")
stod = model.StockDaily('000001')
stod.collect_data(data=res)





