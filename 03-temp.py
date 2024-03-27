import numpy as np

def read_txt_to_array(filepath):
    return np.loadtxt(filepath, dtype=float)

folder_path = r"E:\DeskTop\桌面\科目\大创\大创\SMASCLL"
handled_file_path = r"E:\DeskTop\桌面\科目\大创\大创\sm-handled.txt"
output_file_path = r"E:\DeskTop\桌面\科目\大创\大创\temp.txt"

handled_data = read_txt_to_array(handled_file_path)
count_matrix = np.zeros(handled_data.shape, dtype=int)

# 对每个年份文件进行遍历和比较
for year in range(2001, 2019):
    file_path = f"{folder_path}\\{year}.txt"
    year_data = read_txt_to_array(file_path)
    count_matrix += (year_data >= handled_data)

# 创建输出文件
with open(output_file_path, 'w') as output_file:
    # 遍历每个点位，写入temp值或-1
    for row in count_matrix:
        line = ' '.join(str(temp if temp >= 15 and temp != 18 else -1) for temp in row)
        output_file.write(line + "\n")

print("文件已写入:", output_file_path)