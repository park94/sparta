from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

# 영화제목 매트릭스 평점 가져오기

# mat = db.users.find_one({"title":"매트릭스"})
# print(mat["star"])
# star_targ = movie_targ["star"]
movies = list(db.movies.find({"star":"9.97"}))
# print(movies)
for movie in movies:
     print(movie["title"])

# 이 영화들의 평점을 0으로 만들기


db.movies.update_many({"star":"9.97"},{"$set":{"star":"0"}})