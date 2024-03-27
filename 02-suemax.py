import numpy as np
import os

# 文件夹路径
folder_path = 'E:\\DeskTop\\桌面\\科目\\大创\\大创\\SUEASCLL'

# 获取文件夹中的所有文件
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 初始化结果矩阵
result = np.full((720, 1230), -9999.0)  # 将结果矩阵初始化为-9999

# 遍历所有文件
for file in files:
    # 读取文件
    data = np.loadtxt(os.path.join(folder_path, file))

    # 将大于-9999的数据写入结果矩阵
    result[data > -9999] = np.maximum(result[data > -9999], data[data > -9999])

# 将值为0的数据写入结果矩阵
result[result == 0] = 0

# 保存结果
np.savetxt('E:\\DeskTop\\桌面\\科目\\大创\\大创\\new\\suemax.txt', result, fmt='%.4f')
