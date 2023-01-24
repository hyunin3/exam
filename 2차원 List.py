lst=[[1],[2,3],[4,5,6],[7,8,9,10]]

def list_sum(list_a):
    sum = 0
    for sub_lst in list_a:
        #print(sub_lst)
        for i in sub_lst:
            sum = sum + i
        
    return sum

print(list_sum(lst))

#lst[0]=[1], lst[1]=[2,3], lst[2]=[4,5,6]   
#리스트 안에 리스트 
