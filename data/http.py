# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import json

def http_post_data(header=None,url="http://api.waditu.com"):
    if header == None:
        header={'api_name':'stock_basic',
                'token':'f054de446f8cbcd1375f1a372f88bb130137e2c8659ad7ea37b32fd9',
                    'params':{
                        'list_stauts':'L',
                        'fields':'ts_code,name,area,industry,list_date',
                    }
                }
    else:
        header = header
    print header
    req = urllib2.Request(url, header)
    response = urllib2.urlopen(req)
    return json.loads(response.read())['data']

'''
resp = http_post_data()
print resp
print type(resp)
print json.loads(resp)['data']['items'][0][2]'''




'''JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。易于人阅读和编写。同时也易于机器解析和生成。
它基于JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999的一个子集。
JSON采用完全独立于语言的文本格式，但是也使用了类似于C语言家族的习惯（包括C, C++, C#, Java, JavaScript, Perl, Python等）。
这些特性使JSON成为理想的数据交换语言。
二、HTTP的请求方法
HTTP/1.1协议中共定义了八种方法（有时也叫“动作”）来表明Request-URI指定的资源的不同操作方式：
. OPTIONS - 返回服务器针对特定资源所支持的HTTP请求方法。
                   也可以利用向Web服务器发送'*'的请求来测试服务器的功能性。
. HEAD    - 向服务器索要与GET请求相一致的响应，只不过响应体将不会被返回。
                这一方法可以在不必传输整个响应内容的情况下，就可以获取包含在响应消息头中的元信息。
. GET     - 向特定的资源发出请求。
                注意：GET方法不应当被用于产生“副作用”的操作中，例如在web app.中。
                其中一个原因是GET可能会被网络蜘蛛等随意访问。
. POST    - 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。
                数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
. PUT     - 向指定资源位置上传其最新内容。
. DELETE  - 请求服务器删除Request-URI所标识的资源。
. TRACE   - 回显服务器收到的请求，主要用于测试或诊断。
. CONNECT - HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。
. PATCH   - 用来将局部修改应用于某一资源，添加于规范RFC5789。

其中，GET，POST, PUT, DELETE常用于RESTful API的实现，所以下面做的代码实现
三、Python实现的json数据以HTTP GET,POST,PUT,DELETE方式进行页面请求
闲言少述，直接上代码.
1. GET方法
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: http_get.py

import urllib2

def http_get():
    url='http://192.168.1.13:9999/test'   #页面的地址
    response = urllib2.urlopen(url)         #调用urllib2向服务器发送get请求
    return response.read()                     #获取服务器返回的页面信息
    
ret = http_get()
print("RET %r" % (ret))
2. POST方法
#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py

import urllib
import urllib2
import json
    
def http_post():
    url='http://192.168.1.13:9999/test'
    values ={'user':'Smith','passwd':'123456}

    jdata = json.dumps(values)             # 对数据进行JSON格式化编码
    req = urllib2.Request(url, jdata)       # 生成页面请求的完整数据
    response = urllib2.urlopen(req)       # 发送页面请求
    return response.read()                    # 获取服务器返回的页面信息

resp = http_post()
print resp
3. PUT方法
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: http_put.py

import urllib2
import json

def http_put():
    url='http://192.168.1.13:9999/test'
    values={'':''}

    jdata = json.dumps(values)                  # 对数据进行JSON格式化编码
    request = urllib2.Request(url, jdata)
    request.add_header('Content-Type', 'your/conntenttype')
    request.get_method = lambda:'PUT'           # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_put()
print resp
4. DELETE方法
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# File: http_delete.py

import urllib2
import json

def http_delete():
    url='http://192.168.1.13:9999/test'
    values={'user':'Smith'}

    jdata = json.dumps(values)
    request = urllib2.Request(url, jdata)
    request.add_header('Content-Type', 'your/conntenttype')
    request.get_method = lambda:'DELETE'        # 设置HTTP的访问方式
    request = urllib2.urlopen(request)
    return request.read()

resp = http_delete()
print resp'''
