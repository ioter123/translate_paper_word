import urllib.request
import json
import requests
from bs4 import BeautifulSoup

# 우리말샘 api
key = "301875D5A1FEF606AB6AD8B6BD76C6AB" # 개인 인증키
q = "정책"
#print(q)
data = "type_search=search&start=1&num=100&translated=y&trans_lang=1&advanced=y"
url = "https://krdict.korean.go.kr/api/search?key="+key+"&q="+q+"&"+data
#print(url)
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup)
trans_en = soup.find_all('trans_word')
#print(trans_en)
words = set()
for item in trans_en:
    words.add(item.get_text())
print(words)