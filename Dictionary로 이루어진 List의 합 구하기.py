#dict_list_sum([{'name': 'kim', 'age': 12},
#              {'name': 'lee', 'age': 4}])   => 16

#dict_list_sum[0]['age']+dict_list_sum[1]['age']

#dic의 데이터를 리스트 안에서 for 라는 반복으로 가져와야
list_a = [{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}]
def dict_list_sum(lst):
    sum = 0
    for dic in lst:
        #print(lst)
        sum = sum + dic['age']
        
    return sum
#print(dic['age'])

print(dict_list_sum(list_a))        

