scores_a = [30,60,90,70]

def over(lst):
    cnt = 0
    for i in lst:
        if i >= 60:
            cnt = cnt +1
    return cnt

print(over(scores_a))            