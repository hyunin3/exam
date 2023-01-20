num=int(input())
for i in range(1,num+1):
    
    if num % i ==0:
        print(i)
    else: 
        pass



# n=input
# print(n) 
# print(type(n))-> str이니 정수로 바꿔줘야됨
# n=int(n) 

# 약수? n % i=0
# 모든 경우 다 돌아봐야되서 1~n까지 다 돌아봐야됨 
# for i in range(1,n+1):
#      if num % i ==0:
#         print(i)
# i는 1이 들어가고 실행, 2가 들어가고 실행 ....      
# ㅔ갸ㅜㅅ(i, end = '')으로 가로 출력가능