# 동의어 검색(크롤링)
import requests
from bs4 import BeautifulSoup


def synonyms(word):

    synonym = []

    url = "https://www.collinsdictionary.com/dictionary/english-thesaurus/"+word
    #print(url)
    response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0"})
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    trans_en = soup.find_all("span", "orth")
    #print(trans_en)
    words = set()
    for item in trans_en:
        words.add(item.get_text())

    return list(words)
