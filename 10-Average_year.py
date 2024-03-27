import numpy as np

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\new\\18-handled\\{year}.txt') for year in range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:\\DeskTop\\桌面\\科目\\大创\\大创\\gpp\\gpp{year}.txt') for year in range(2001, 2019)}

# 遍历所有满足条件的坐标
for year in range(2001, 2019):
    SUM = 0.0
    temp = 0
    indices = np.where(np.isin(data_1[year], [0, 1]))
    for x, y in zip(*indices):
        if data_1[year][x, y] == 0:
            S0 = data_2[year][x, y]
            if S0 == -9999:
                continue
            values = [data_2[i][x, y] for i in range(2001, 2019) if data_2[i][x, y] != -9999]
            if not values:
                continue
            S1 = np.mean(values)
            SUM += abs(S1 - S0)
            temp += 1
        elif data_1[year][x, y] == 1:
            years_0 = [i for i in range(2001, 2019) if data_1[i][x, y] == 0 and data_2[i][x, y] != -9999]
            if not years_0:
                continue
            S_0 = np.mean([data_2[i][x, y] for i in years_0])
            values = [data_2[i][x, y] for i in range(2001, 2019) if data_2[i][x, y] != -9999]
            if not values:
                continue
            S_1 = np.mean(values)
            SUM += abs(S_1 - S_0)
            temp += 1
    if temp > 0:
        Average = round(SUM / temp, 6)
        print(f'Average_{year} = {Average}')