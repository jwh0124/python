import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

main = bs4.BeautifulSoup(html, "html.parser")

menuListLi = main.find("ul", {"class": "list_nav"}).findAll("li")
menuList = []

for menu in menuListLi:
    menuList.append(menu.find("a").text)

newsListArea = main.find("div", {"class":"thumb_area"})
newsList = []

for newsListDiv in newsListArea:
    newListImg = newsListDiv.find("img")
    if newListImg != -1:
        newsList.append(newListImg["alt"])

print("Menu : ", menuList)
print("News : ", newsList)

urllib.request.urlcleanup()