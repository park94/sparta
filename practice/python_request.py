import requests # requests 라이브러리 설치 필요
from pprint import pprint

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json() # 제이슨화 시켜주기

#print(rjson['RealtimeCityAir']['row'][0]['NO2'])

# 모든 구의 IDEX_MVL 값을 찍어주자(미세먼지 수치)
gus = rjson['RealtimeCityAir']['row']
#pprint(gus)

for gu in gus:
    if gu["IDEX_MVL"]<100:
        print(gu["MSRSTE_NM"],gu["IDEX_MVL"])