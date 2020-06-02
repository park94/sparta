from pymongo import MongoClient            # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from pprint import pprint                  # pprint 사용
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'young','age':27})
# db.users.insert_one({'name':'wok','age':29})
# db.users.insert_one({'name':'min','age':27})

all_users = list(db.users.find())    # 모든 사람 찾기
# pprint(all_users)
pprint(list(db.users.find({'name':'young'})))

key = db.users.find_one({"name":"wok"},{"_id": False})
pprint(key)

db.users.update_one({"name":"wok"},{"$set":{"name":"wokki","age":"27"}})
db.users.update_many({"age":27},{"$set":{"occupation":"student"}})
