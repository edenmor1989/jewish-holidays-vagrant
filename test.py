import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import json
import os
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
resultlist=[]
import os
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
#json_load = json.loads(data)
import os
if os.path.exists("output.json"):
  os.remove("output.json")
else:
  print("The file does not exist")

#json2html.convert(json=result)
#print(result)
#exit()
import http.server
import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'output.txt'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8082
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()

print(result)
