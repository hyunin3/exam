# #신규 아이디 생성 마지막 글자는 0부터 9까지의 숫자임을 만족하면 True, 아니면 False
def is_id_valid(user_data):
    for i in range(10):

        if user_data['id'][-1] == str(i):
            return True
    else:
        return False        



# # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
