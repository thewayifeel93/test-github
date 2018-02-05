def summation(a,b):
    return a+b
def minus(a,b):
    return a-b

a=[0,0]
op=""
a[0]=int(input("숫자를 입력하세요 :"))
a[1]=int(input("숫자를 입력하세요 :"))
op=input("무엇을 하시겠습니까?(더하기/빼기):")

if op=="더하기":
    print("합은 %d 입니다."%summation(a[0],a[1]))
if op=="빼기":
    print("차는 %d 입니다."%minus(a[0],a[1]))
