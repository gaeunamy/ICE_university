kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score) # 리스트 안에 세 개의 리스트가 들어있음

# 이차원 리스트에 인덱싱하여 값에 접근하기
print(midterm_score[0][2]) # 첫 번째 리스트 내의 세 번째 원소에 접근

# 리스트의 메모리 저장
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)

math_score[0] = 1000 # midterm_score 두 번째 행의 첫 번째 값이 변경됨
print(midterm_score)