import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import json
import os
import http.server
import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
datetoday=date.today()
d1=datetoday.strftime("%Y-%m-%d")
print(d1)
date3months=datetoday+relativedelta(months=+3)
print (date3months)
url = f'https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=off&year=now&month=x&start={d1}&end={date3months}&ss=off&mf=off&c=on&'
resp = requests.get(url=url,verify=False)
data = resp.json()
data = json.dumps(data, indent = 4)
print(type(data))
result={'items':[]}
if os.path.exists("output.txt"):
  os.remove("output.txt")
else:
  print("The file does not exist")
data=eval(data)
for item in data['items']:
    result['items'].append({'title':item['title'],'date':item['date']})
fl=open('output.txt', 'w')
json.dump(result,fl,indent=4)
fl.close()
print(result)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'output.txt'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("/home/vagrant/cert.pem") # PUT YOUR cert.pem HERE
server_address = ("", 8082)
with socketserver.TCPServer(server_address, handler_object) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
