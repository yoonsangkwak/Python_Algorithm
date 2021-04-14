# 다음 dataset에서 전체 이름 안에 M이 몇번 나왔는지 빈도수 출력

dataset = ["Fynney Mr.Joseph J", "Dwyer, Miss, Ellen, Nellie"]

m_count = 0
for data in dataset:
    for i in range(len(data)):
        if data[i] == "M":
            m_count += 1

print(m_count)