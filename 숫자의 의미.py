#get_secret_word([83, 115, 65, 102, 89]) #SsAfY
#chr() 숫자를 문자열로 반환

words_a = [83, 115, 65, 102, 89]
def get_secret_word(words):
    result = ''  #숫자 나올때 0에서 시작하듯이 문자열은 빈 문자열로 시작.
    for word in words:
        
        result = result + chr(word)
        # words.append(chr(word)) 이거 의미는 [83, 115, 65, 102, 89, S, s..]
        
    return result

#print(words)
print(get_secret_word(words_a))
