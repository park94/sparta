# print ("Hello")

# a = 3
# b = a+1
# print (a, b)
# print (a//b, a%b)

# text = "Hello2"
# print(text)

# # 파이썬은 위에서부터 아래로 읽어오는 형식
# # 파이썬은 띄어쓰기가 중요한 함수 (인덴트 삭제 불가, 줄맞춤 중요)
# # 함수 정의

# def sumsum(num1, num2):
#     return num1 + num2

# c = sumsum(1,5)
# print(c)

# a = 3 
# print(a)

# # 조건문 문법
# # else if 대신에 elif 사용 

# if a%2==1:
#     print ("a is odd")
# else:
#     print ("a is even")

# # for문 사용법이 JS와 다름 

# # JS와 동일한 문법을 사용한다면?
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
def count_fruit(fruit_list, fruit_x):
    count = 0
    for fruit in fruit_list:
        if fruit == fruit_x: 
            count = count+1
    return count

#print(count_fruit(fruits, "딸기"))

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

# 모든 사람의 이름과 나이를 출력해봅시다.

for i in people:
    name = i["name"]
    age = i["age"]
   # print(name, age)

# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 이름을 받으면, age를 리턴해주는 함수
def return_age(name_x):
    list_a = []
    for i in people:
        name = i["name"]
        if name == name_x:
            print(i["age"])

return_age("bob")

