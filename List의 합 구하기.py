list_a=[1,2,3,4,5]

def list_sum(lst):
    sum=0
    for i in lst:
        sum = sum + i
    
    return sum

print(list_sum(list_a))

#print(sum(list_a))
# numbers=[1,2,3,4]
# result=0
# for i in numbers:
#     result=result+i
# print(result)  

# def list_sum():
#     result = 0
#     print(list_a)
#     for num in list_a:
#         result + num 하고 싶은데 이걸 새로 result에 넣어줘야 재활용가능
#         result=result + num
#     return result
