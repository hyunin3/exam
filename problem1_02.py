# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# python 내장함수 min, max 사용 금지
def max_score(scores): #전체 점수 중 최고점을 반환하는 함수 max_score(scores)를
    score = -1         #만듭니다. 시험점수는 최저 0점 이므로 -1점에서 시작해 
    for i in scores:   #리스트 내에서 자신보다 큰 점수를 만나면 그 점수를 score값으로
        if score <= i: #가지도록 한후 score값을 반환합니다.
            score = i
    return score                
    
def min_score(scores): #전체 점수 중 최저점을 반환하는 함수 min_score(scores)를   
    score = 101        #만듭니다. 시험점수는 최고 100점 이므로 101점에서 시작해 
    for j in scores:   #리스트 내에서 자신보다 작은 점수를 만나면 그 점수를 score값으로
        if score >= j: #가지도록 한후 score값을 반환합니다.
            score = j
    return score 

def min_max(scores):  #최저점과 최고점이 튜플로 묶여 반환되는 함수 min_max(scores)입니다.
    return (min_score(scores), max_score(scores))#앞에서 정의한 두 함수를 사용합니다.
     # 여기에 코드를 작성하여 함수를 완성합니다.

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(min_max(scores))    # (75, 90)
