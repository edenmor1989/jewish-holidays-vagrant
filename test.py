import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import json
import os
import http.server
import socketserver
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
def init_date_url():
    datetoday=date.today()
    d1=datetoday.strftime("%Y-%m-%d")
    print(d1)
    date3months=datetoday+relativedelta(months=+3)
    print (date3months)
    url = f'https://www.hebcal.com/hebcal?v=1&cfg=json&maj=on&min=on&mod=on&nx=off&year=now&month=x&start={d1}&end={date3months}&ss=off&mf=off&c=on&'
    return url
def api_request(url):
    resp = requests.get(url=url,verify=False)
    data = resp.json()
    data = json.dumps(data, indent = 4)
    return(data)
def remove_file_if_exists():
    if os.path.exists("output.txt"):
        os.remove("output.txt")
def convert_data(retrive_data):
    for item in retrive_data['items']:
        result['items'].append({'title':item['title'],'date':item['date']})
    fl=open('output.txt', 'w')
    json.dump(result,fl,indent=4)
    fl.close()
    return(result)
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'output.txt'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
def start_server(handler_object):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("/home/vagrant/cert.pem") # PUT YOUR cert.pem HERE
    server_address = ("", 8082)
    with socketserver.TCPServer(server_address, handler_object) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()
if __name__ == "__main__":
    url=init_date_url()
    result={'items':[]}
    retrive_data=api_request(url)
    remove_file_if_exists()
    retrive_data=eval(retrive_data)
    converted_data=convert_data(retrive_data)
    handler_object = MyHttpRequestHandler
    start_server(handler_object)
