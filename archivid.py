import requests
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    vid_url = None
    def handle_starttag(self, tag, attrs):
        src = None
        found = False
        if tag == 'img':
            for n,k in attrs:
                if n == 'src':
                    src = k
                if n == 'id' and k == 'ii':
                    found = True
        self.vid_url = src if found and '.gif' in src else self.vid_url
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):
        pass

    def get_vid(self):
        v = self.vid_url
        self.vid_url = None
        return v

class MainPageParser(HTMLParser):
    max_id = None
    found = False
    found_found = False
    def handle_starttag(self, tag, attrs):
        if self.found_found:
            return
        if tag == 'div' or tag == 'a':
            for n,k in attrs:
                if n == 'href':
                    if self.found and not self.found_found:
                        self.max_id = int(k[1:])
                        self.found_found = True
                if n == 'id' and k == 'container':
                    self.found = True
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):
        pass


parser = MyHTMLParser()
max_id_p = MainPageParser()
s = requests.Session()
data = s.get('http://archillect.com/').text
max_id_p.feed(data)
for i in range(1,max_id_p.max_id):
    print(i, file=sys.stderr)
    data = s.get('http://archillect.com/'+str(i)).text
    #print(data.split('='))
    parser.feed(data)
    vid = parser.get_vid()
    if vid is not None:
        print(vid)
