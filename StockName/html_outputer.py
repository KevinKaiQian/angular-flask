# coding:utf8


class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]
        
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def outoupt_html_header(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<head>')
        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
        fout.write('</head>')
        fout.write('<boady>')
        fout.write('<table>') 
        fout.flush()
    
    
    def outoupt_html(self,count = 1):

        
        fout = open('output.html','a')
        for i in range (0,1,count):
            data = self.datas.pop()
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        fout.flush()
            #print data['summary'].encode('utf-8')


    
    def outoupt_html_ender(self):
        fout = open('output.html','a')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.flush()
    
    



