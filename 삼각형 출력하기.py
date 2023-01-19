num = int(input())
for i in range(1, num + 1):
    print(' ' * (num - i) + '*' * i)   # ''이 아니라 ' '임


#다른 삼각형 출력
# num = int(input())
# for i in range(1, num+1):
#     print('*' * i)

#            or

# num = int(input())
# for i in range(1, num + 1):
#     for j in range(1, num + 1):
#         if i<j:
#             print('', end='')
#         else:
#             print('*', end='')
#     print()            


#역삼각형 출력
# for i in range(5):
#     for j in range(5):
#         if j<i:
#             print('', end='')
#         else:
#             print('*', end='')    
#     print()        