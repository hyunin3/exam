# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    sum = 0
    for i in scores:
        sum = sum + i  #scores 리스트 안의 값을 모두 더합니다.
    return sum / len(scores) #평균을 구하기 위해 더한 값들을 리스트의 길이로 나누어줍니다.
        
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5