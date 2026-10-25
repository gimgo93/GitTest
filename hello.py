print("hello, python")
print(1+1)
import random
import time
import sys
L = ["건우", "태훈", "현욱", "유석"]
for name in L :
    print(random.choice(name))
print(L)
while True:
    select = random.choice(L)
    if select == "건우":
        print(select)
        break
    else:
        print(select)
command = input("'다음'을 입력하세요")
if command =='다음':
    print("다음 명령어 실행")
    time.sleep(2)
else:
    print("종료")
    sys.exit()
for i in range(5):           
    name = random.choice(L)
    print(name)
time.sleep(2)
print("goodbye, hello.py")
