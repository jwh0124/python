import urllib.request
import urllib.error

import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}

url = "https://news.naver.com/"
req = urllib.request.Request(url,headers=headers)
try:
    html = urllib.request.urlopen(req)
    main = bs4.BeautifulSoup(html, "html.parser")
    
    hdline_article_list = main.find("ul", {"class": "hdline_article_list"}).findAll("li")

    for hdline in hdline_article_list:
        print(hdline.find("a").text.strip())

except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.code)


