
import requests
from bs4 import BeautifulSoup
import os
import time
def get_one_page(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'Referer':'https://www.meitulu.com/t/youhuo/'+ str(page)+'.html'}
    response = requests.get(url=url,headers=headers)
    return response.text


def paser_page(html):
    soup = BeautifulSoup(html,'lxml')
    all_a = soup.find('ul',class_='img').find_all('a')
    l_a = list(set(all_a))
    for a in l_a:
        randoms = time.time()
        os.makedirs(os.path.join("D:\mzitu1",str(randoms)))
        os.chdir("D:\mzitu1\\"+str(randoms))
        href = a['href']
        suffix = 'html'
        if href.endswith(suffix) is True:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                'Referer': 'https://www.meitulu.com/t/youhuo/' + str(page) + '.html'
                }

            img_url = requests.get(href, headers)
            biaoqian = str(href)[29:34]

            img_url_soup = BeautifulSoup(img_url.content, 'lxml')
            print(href)
            max_span = img_url_soup.find('div', class_='c_l').find_all('p')[2]
            spans = str(max_span)[9:11]
            for span in range(1,int(spans)+1):
                img = 'https://mtl.ttsqgs.com/images/img/' + biaoqian + '/' + str(span) + '.jpg'

                print('正在写入'+href+img)
                image = requests.get(img,headers=headers)
                f = open(str(biaoqian)+str(span)+str(randoms)+'.jpg', 'ab')
                f.write(image.content)
                f.close()



if __name__ == '__main__':
    for page in range(2,3):
        url = 'https://www.meitulu.com/t/youhuo/'+ str(page)+'.html'
        html = get_one_page(url)
        item = paser_page(html)





