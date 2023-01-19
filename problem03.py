#입력정보인 user_data가 dict형태로 들어온다
#아이디와 비밀번호가 하나라도 빈 문자열이면 False 그렇지 않으면 True가 반환되도록.
#(True, False는 bool자료형)
def is_user_data_valid(user_data):
    for value in user_data.values():
        if value == '':
            return False
        
        else:
             return True    

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True