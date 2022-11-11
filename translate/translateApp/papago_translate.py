# 파파고 api
import urllib.request
import json


def papago_translate(word):
    client_id = "Nn_DSXGvKuCp3WAVnUSX" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "ZtAlB3mxTr" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(word)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        result_trans = json.loads(response_body.decode('utf-8'))
        return result_trans['message']['result']['translatedText']
    else:
        return False


