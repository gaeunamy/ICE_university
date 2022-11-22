print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다")
print("변환하고 싶은 섭씨온도를 입력하세요.")
celsius = input() # 섭씨온도를 입력받아(문자열) 변수에 저장
fahrenheit = (float(celsius) * 1.8) + 32 # 실수형으로 변환
print("섭씨온도: ", celsius)
print("화씨온도: ", fahrenheit)