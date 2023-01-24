#전체 점수 중 60점 이상인 과목의 개수를 계산하는 함수 over를 완성하시오
def over(lst):
    cnt = 0
    for score in lst:
        if score >= 60:
            cnt = cnt + 1
    
    return cnt        





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
