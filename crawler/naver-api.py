# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
from urllib.parse import urlparse

import requests

client_id = "teFWuvQdG99M7H6ex4fu"
client_secret = "uJD0kJec60"

def get_api_request(keyword, display) :
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display)
    result = requests.get(urlparse(url).geturl(), headers={
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret":client_secret
    })

    return result.json()



keyword="강남역"
requestResult = get_api_request(keyword, 100)

for item in requestResult["items"]:
    print(item["title"].replace("<b>","").replace("</b>",""), item["link"])
