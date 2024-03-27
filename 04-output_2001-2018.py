import numpy as np
import os


def read_txt_to_array(filepath):
    return np.loadtxt(filepath, dtype=float)


folder_path = r"E:\DeskTop\桌面\科目\大创\大创\SMASCLL"
handled_file_path = r"E:\DeskTop\桌面\科目\大创\大创\sm-handled.txt"
output_folder = r"E:\DeskTop\桌面\科目\大创\大创\output2001-2018"

handled_data = read_txt_to_array(handled_file_path)
count_matrix = np.zeros(handled_data.shape, dtype=int)

# 对每个年份文件进行遍历和比较
for year in range(2001, 2019):
    file_path = f"{folder_path}\\{year}.txt"
    year_data = read_txt_to_array(file_path)
    count_matrix += (year_data >= handled_data)

# 对每个年份处理和写入新文件
for year in range(2001, 2019):
    file_path = f"{folder_path}\\{year}.txt"
    year_data = read_txt_to_array(file_path)
    output_file_path = os.path.join(output_folder, f"{year}.txt")

    with open(output_file_path, 'w') as output_file:
        for i in range(year_data.shape[0]):
            for j in range(year_data.shape[1]):
                if count_matrix[i, j] < 15 or count_matrix[i, j] == 18:
                    output_file.write("-1 ")
                else:
                    value = 1 if year_data[i, j] >= handled_data[i, j] else 0
                    output_file.write(f"{value} ")
            output_file.write("\n")

    print(f"文件已写入: {output_file_path}")