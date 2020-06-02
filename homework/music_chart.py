import requests #requests 라이브러리 가져오기
from bs4 import BeautifulSoup #크롤링을 쉽게 해주는 라이브러리
from pprint import pprint
from pymongo import MongoClient           # pymongo를 임포트 하기
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 url 가져오기
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

#변수에 parsing된 데이터 담기
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, 원하는 것 가져오기
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# pprint(musics)


# musics (tr들) 의 반복문을 돌리기
for music in musics:
    # music 안에 rank 가 있으면,
    music_rank = music.select_one('td.number')
    music_name = music.select_one('td.info > a')
    music_artist = music.select_one('td.info > a.artist.ellipsis')
    music_album = music.select_one('td.info > a.albumtitle.ellipsis') #class="albumtitle ellipsis"

    rank = music_rank.text.split(" ")[0].strip()
    name = music_name.text.strip()
    artist = music_artist.text.strip()
    album = music_album.text.strip()
    print(rank+"  "+name+' -'+artist+'      "'+album+'"')
    # doc = {
    #         'rank' : rank,
    #         'name' : name,
    #         'artist' : artist
    #     }
    # db.musics.insert_one(doc)


# target_artist = db.musics.find_one({"artist":"아이유 (IU)"})
# target_rank = target_artist["rank"]

# iu_musics = list(db.musics.find({'rank':target_rank}))

# pprint(iu_musics)