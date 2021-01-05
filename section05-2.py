# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is", v2)

for v3 in range(1, 11):
    print("v3 is", v3)

# 1~100합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print(sum1)
print(sum(range(1, 101)))
print(sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "cho", "choi", "yoo"]
for name in names:
    print("you are : ", name)

word = "dreams"
for s in word:
    print("word:", s)

my_info = {"name": "kim", "age": 33, "city": "seoul"}
# 기본값은 키
for v in my_info:
    print("my_info", v)
for v in my_info.values():
    print("my_info", v)
for v in my_info.keys():
    print("my_info", v)
# 둘다
for k, v in my_info.items():
    print(k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 6, 5, 345, 1, 2, 45, 13]
for num in numbers:
    if num == 345:
        print("found")
        break
    else:
        print("not")

# for - else 구문 (반복문이 끝까지 수행된 경우 else 블럭 수행)
for num in numbers:
    if num == 345:
        print("found")
        break
    else:
        print("not")
else:
    print("nono")

# continue
lt = ["1", 3, 4, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print(type(v))
