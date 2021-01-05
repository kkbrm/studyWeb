# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print("yes")

# 예2
if False:
    print("No")

# 예3
if False:
    print("No")
else:
    print("yes2")

# 관계연산자
# >,>=,<,<=,==<!=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# 참 거짓 종류(True, False)
# 참 : "내용",[내용], (내용),{내용}, 1
# 거짓 : "",[], (),{}, 0

city = ""

if city:
    print(">>true")
else:
    print(">>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print("and :", a > b and b > c)
print("or :", a > b or c > b)
print("not:", not a > b)
print(not False)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용

print("ex1:", 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = "A"
if score1 >= 90 and score2 == "A":
    print("합격")
else:
    print("불합격")

# 다중조건문
num = 90

if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("등급 B")
elif num >= 70:
    print("등급 C")
else:
    print("꽝")

# 중첩조건문
age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A")
    elif height >= 160:
        print("B")
    else:
        print("c")
else:
    print("c")
