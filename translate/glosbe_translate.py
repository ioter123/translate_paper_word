import urllib.request
import urllib.parse
import json
import requests
from bs4 import BeautifulSoup

# glosbe api (개인키 필요 - 계약해야 됨)
phrase = "정책"
glosbe_url = 'http://api.ezmeta.co.kr/v1/search.php?'
query_params = {
  'k'   : phrase
  }
query_url = urllib.parse.urlencode(query_params)
print(query_url)
#response = urllib.request.urlopen(glosbe_url+query_url)
response = requests.get(glosbe_url+query_url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
trans_en = soup.find_all('')
#print(trans_en)
words = set()
for item in trans_en:
    words.add(item.get_text())
print(words)