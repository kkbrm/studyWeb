# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로
# .. : 부모 디렉토리
# . : 현재 디렉토

# 사용1 (클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("exw :", Fibonacci.fib2(400))
print("ex2: ", Fibonacci().title)

# 사용2(클래스)
# from pkg.fibonacci import *

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

# 사용(함수)
import pkg.calculations as c

print("ex:", c.add(10, 100))
print("dd", c.mul(10, 100))

# 사용5
from pkg.calculations import dev as d

print("ex5:", int(d(100, 10)))

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()

print(dir(builtins))
