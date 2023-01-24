# 전체 점수 중 최고점을 반환하는 함수 max_score을 완성하시오.(내장함수 max사용 불가)
def max_score(lst):
    i = 0
    for score in lst:
        if i < score:
            i = score

    return i


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90

