# append()
color = ['red', 'blue', 'green']
color.append('white') # 리스트에 원소 추가
print(color)

# extend()
color = ['red', 'blue', 'green']
color.extend(['black', 'purple']) # 새로운 리스트 추가
print(color) # 합쳐져서 하나의 리스트로 출력됨

# insert()
color = ['red', 'blue', 'green']
color.insert(0, 'orange') # 첫 번째 자리에 새로운 원소 추가, 기존 원소들은 한 칸씩 밀림
print(color)

# remove()
color. remove('red') # 특정 원소 삭제
print(color)

# 인덱스의 재할당과 삭제
color = ['red', 'blue', 'green']
color[0] = 'orange' # 첫 번째 인덱스에 새로운 값 재할당
print(color) # red가 orange로 바뀜