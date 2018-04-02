import urllib.request
import re
import os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)
  
  
    try:
        os.mkdir("mm")
    except FileExistsErro:
        pass

    os.chdir('mm')

    for each in imglist:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each,filename,None)
   

    

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3563409202'
    get_img(open_url(url))
