import urllib.request
import urllib.error
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}

def get_product_info(box):
    prod_box_list = box.find("p", {"class":"name"})
    prod_list = prod_box_list.find("span")
    price = box.find("ul").findAll("span")
    link = box.find("a")["href"]

    return {"name": prod_list.text, "price": price[1].text, "link": link}

def get_page_product(url):
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req)
    main = bs4.BeautifulSoup(html, "html.parser")
    ul = main.find("ul", {"class":"prdList"})
    boxes = ul.findAll("div",{"class":"box"})

    return [get_product_info(box) for box in boxes]


urls = [
    "https://jolse.com/category/toners-mists/1019/?page=1",
    "https://jolse.com/category/toners-mists/1019/?page=2",
    "https://jolse.com/category/toners-mists/1019/?page=3",
    "https://jolse.com/category/toners-mists/1019/?page=4",
    "https://jolse.com/category/toners-mists/1019/?page=5"
]

try :
    
    for url in urls:
        get_page_product(url)

except urllib.error.HTTPError as e :
    print(e.code)
