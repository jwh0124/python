import urllib.request
import urllib.error
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
}

from_date = "2010-01-01"
to_date = "2018-04-28"

url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/"+ from_date +"/edate/" + to_date
req = urllib.request.Request(url,headers=headers)

html = urllib.request.urlopen(req)
json_data = json.load(html)

for data in json_data:
    print(data["date"] + "@" + data["settlement"])