import numpy as np
import os
from scipy import stats

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\output_2001-2018\\{year}.txt') for year in
          range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\SMASCLL\\{year}.txt') for year in
          range(2001, 2019)}
data_3 = {year: np.loadtxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\SUEASCLL\\{year}.txt') for year in
          range(2001, 2019)}

# 读取temp.txt文件
temp = np.loadtxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\new\\temp.txt')

# 找到值为15，16，17的值，记录该坐标
indices = np.where(np.isin(temp, [15, 16, 17]))

# 初始化结果矩阵
result = np.full(temp.shape, -1)
years_txt = {year: np.full(temp.shape, -1) for year in range(2001, 2019)}

# 遍历所有满足条件的坐标
for x, y in zip(*indices):
    years_1 = []
    years_0 = []
    values_2 = []
    values_3 = []

    # 在文件夹1中，找到所有文件该坐标位置对应的数据
    for year in range(2001, 2019):
        if data_1[year][x, y] == 1:
            years_1.append(year)
        else:
            years_0.append(year)

    # 值为1时，在文件夹2和文件夹3中，对应的相同年份相同坐标对应的值在文件夹2和文件夹3中记录下来
    for year in years_1:
        value_2 = data_2[year][x, y]
        value_3 = data_3[year][x, y]
        if value_3 != -9999:  # 如果纵坐标中出现-9999则取消该点的画图
            values_2.append(value_2)
            values_3.append(value_3)

    if len(values_2) < 2 or len(set(values_2)) == 1:  # 如果没有足够的点进行线性回归，或者所有的x值都相同，则跳过这个坐标
        result[x, y] = -1
        continue

    try:
        # 构造线性拟合函数，构造回归方程，进而构造置信区间
        slope, intercept, r_value, p_value, std_err = stats.linregress(values_2, values_3)
        ci = 1.96 * np.std(values_3) / np.mean(values_3)
    except ValueError:
        result[x, y] = -1
        continue

    # 判断之前记录为0的年份对应的文件夹2和文件夹3中的文件的值是否在该置信区间外
    SUM = 0
    for year in years_0:
        value_2 = data_2[year][x, y]
        value_3 = data_3[year][x, y]
        if value_3 != -9999:  # 如果纵坐标中出现-9999则不统计SUM的值
            if value_3 < intercept + slope * value_2 - ci or value_3 > intercept + slope * value_2 + ci:
                SUM += 1
                years_txt[year][x, y] = 1
        else:
            SUM = -1  # 如果纵坐标中出现-9999，则该点略去，不统计SUM的值，直接写入-1

    # 记录结果
    result[x, y] = SUM
    if SUM < 3:
        if SUM < 2:
            for year in range(2001, 2019):
                if years_txt[year][x, y] != 1:
                    years_txt[year][x, y] = 0

# 保存结果
np.savetxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\new\\result\\result.txt', result, fmt='%d')
for year in range(2001, 2019):
    np.savetxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\new\\18-handled\\{year}.txt', years_txt[year], fmt='%d')