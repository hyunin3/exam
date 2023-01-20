dict_list_sum = ([{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}]) #=>16

print(dict_list_sum[0]['age']+dict_list_sum[1]['age'])


dic = [{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}]

dic의 데이터를 리스트 안에서 for 라는 반복으로 가져와야

def dict_list_sum(lst): 
    result=0
    for dic in lst:
        print(lst)
    return result    
        print(dic['age'])
        
        