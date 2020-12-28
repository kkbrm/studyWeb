# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print("Hello Python!")  # ''
print("Hello Python!")
print("""Hello Python!""")
print("""Hello Python!""")  # '''

print()

# Separator 옵션 사용
print("T", "E", "S", "T", sep="")
print("2019", "02", "19", sep="-")
print("niceman", "googl.com", sep="@")

# end 옵션 사용 : 다음 라인과 연결
print("Welcom To", end=" ")
print("the black parade", end=" ")
print("piono notes")

print()

# format 사용 [], {}, ()
print("{} and {}".format("you", "me"))
print("{0} and {1} and {0}".format("you", "me"))
print("{a} are {b}".format(a="you", b="me"))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ("kk", 7))
print("Test1: %5d, Price : %4.2f" % (665, 7643.123))
print("Test1: {0:5d}, Price: {1:4.2f}".format(6423, 543.1234))
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=6423, b=543.1234))

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print("'you'")
print("'you'")  # "\'you\'"
print('"you"')
print("""'you'""")
print("\\you\\\n")
print("\t\t\ttest")
