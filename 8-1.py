# 5주차 과제 1번

Str = input("문자열을 입력하세여 : ")   # 사용자로 부터 문자열을 입력받아 Str에 저장
NewStr = ""            # 대소문자 변경 후의 문자열을 저장할 변수

# 2019038040 나광호

for i in range(0,len(Str)):         # 입력받은 문자열의 길이만큼 반복
    if(ord(Str[i])>=ord("A") and ord(Str[i])<=ord("Z")):   # 아스키코드를 이용하여 Str[i]가 대문자이면
        newCh = Str[i].lower()       # 소문자로 변경
    elif(ord(Str[i])>=ord("a") and ord(Str[i])<=ord("z")):  # Str[i]가 소문자이면
        newCh = Str[i].upper()      # 대문자로 변경
    else:                       # 그외에는
        newCh = Str[i]         # 그대로둠

    NewStr += newCh            # NewStr에 저장

print("대소문자 변환 결과 --> %s" % NewStr)  # 변경 후의 문자열 출력
