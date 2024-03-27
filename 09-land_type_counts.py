import numpy as np

# 读取文件
file_1 = np.loadtxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\2020.txt')
file_2 = np.loadtxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\result.txt')

# 初始化计数器
count_farmland = 0
count_forest = 0
count_grassland = 0

# 遍历所有满足条件的坐标
for i in range(file_1.shape[0]):
    for j in range(file_1.shape[1]):
        if 11 <= file_1[i, j] <= 18:  # 耕地
            if file_2[i, j] in [1, 2, 3]:
                count_farmland += 1
        elif 19 <= file_1[i, j] <= 30:  # 林地
            if file_2[i, j] in [1, 2, 3]:
                count_forest += 1
        elif 31 <= file_1[i, j] <= 33:  # 草地
            if file_2[i, j] in [1, 2, 3]:
                count_grassland += 1

print(f'耕地的个数：{count_farmland}')
print(f'林地的个数：{count_forest}')
print(f'草地的个数：{count_grassland}')