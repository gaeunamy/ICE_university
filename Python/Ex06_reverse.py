cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[-8:]) # 인덱스가 -8인 서울부터 수원까지 출력

# slicing with over index
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[:]) # 처음~끝 출력
print(cities[-50:50]) # 범위를 넘어갈 경우 자동으로 최대 범위 지정

#step
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[::2])
print(cities[::-1]) # 거꾸로 출력