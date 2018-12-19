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

parser = MyHTMLParser()
s = requests.Session()

for i in range(1,157911):
    print(i, file=sys.stderr)
    data = s.get('http://archillect.com/'+str(i)).text
    #print(data.split('='))
    parser.feed(data)
    vid = parser.get_vid()
    if vid is not None:
        print(vid)
