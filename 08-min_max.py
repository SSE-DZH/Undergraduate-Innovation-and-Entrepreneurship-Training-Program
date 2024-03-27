import numpy as np

# 读取文件
file_1 = np.loadtxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\2020.txt')
file_2 = np.loadtxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\sm-handled.txt')

# 初始化最大值和最小值
max_value = {'耕地': -np.inf, '林地': -np.inf, '草地': -np.inf}
min_value = {'耕地': np.inf, '林地': np.inf, '草地': np.inf}
max_coords = {'耕地': (0, 0), '林地': (0, 0), '草地': (0, 0)}
min_coords = {'耕地': (0, 0), '林地': (0, 0), '草地': (0, 0)}

# 遍历所有满足条件的坐标
for i in range(file_1.shape[0]):
    for j in range(file_1.shape[1]):
        if 11 <= file_1[i, j] <= 18:  # 耕地
            land_type = '耕地'
        elif 19 <= file_1[i, j] <= 30:  # 林地
            land_type = '林地'
        elif 31 <= file_1[i, j] <= 33:  # 草地
            land_type = '草地'
        else:
            continue
        if land_type == '林地' and file_2[i, j] == 848.4284:  # 排除特定值
            continue
        if file_2[i, j] > max_value[land_type] and file_2[i, j] != -9999 and file_2[i, j] != -3277.0 and file_2[i, j] != 0.0:
            max_value[land_type] = file_2[i, j]
            max_coords[land_type] = (i, j)
        if file_2[i, j] < min_value[land_type] and file_2[i, j] != -9999 and file_2[i, j] != -3277.0 and file_2[i, j] != 0.0:
            min_value[land_type] = file_2[i, j]
            min_coords[land_type] = (i, j)

for land_type in ['耕地', '林地', '草地']:
    print(f'{land_type}的最大值：{max_value[land_type]}，坐标：{max_coords[land_type]}')
    print(f'{land_type}的最小值：{min_value[land_type]}，坐标：{min_coords[land_type]}')