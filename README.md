# Undergraduate-Innovation-and-Entrepreneurship-Training-Program



## 源码项目地址

https://github.com/SSE-DZH/Undergraduate-Innovation-and-Entrepreneurship-Training-Program

## sm-handled.txt

### 输入

> SMASCLL文件，SUEASCLL文件

### 输出

> sm-handled.txt

### 输出描述

该代码求出18年中某栅格sue最大值对应的坐标，记录该坐标对应的该年sm的值。以此类推，最后求出720*1230个sm的栅格，并记录在文件中。

### 源码

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {
        // 指定文件路径
        String smascllFolder = "E:\\SMASCLL";
        String sueascllFolder = "E:\\SUEASCLL";
        String outputFilePath = "E:\\sm-handled.txt";

        try {
            // 创建输出文件的写入器
            BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilePath));

            // 遍历每一行
            for (int count = 0; count < 720; count++) {
                // 遍历每一列
                for (int i = 0; i < 1230; i++) {
                    float[][] f1 = readDataFromFile(sueascllFolder, count);
                    float[][] f2 = readDataFromFile(smascllFolder, count);

                    float max = 0;
                    float set = 0;
                    max = f1[0][i];
                    set = f2[0][i];
                    // 比较每个文件夹中的数据
                    for (int j = 0; j < 17; j++) {
                        if (f1[j + 1][i] > max) {
                            max = f1[j + 1][i];
                            set = f2[j + 1][i];
                        }
                    }

                    // 将 set 写入输出文件
                    if (set == -9999) {
                        // 如果 set 为 -9999，则直接写入整数 -9999
                        writer.write("-9999 ");
                    } else {
                        // 否则，保留4位有效数字写入
                        writer.write(String.format("%.4f", set) + " ");
                    }
                }

                // 写入换行符
                writer.newLine();
            }

            // 关闭写入器
            writer.close();

            System.out.println("处理完成，结果保存在：" + outputFilePath);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // 读取文件并返回二维数组的逻辑，包括指定行的处理
    private static float[][] readDataFromFile(String folderPath, int row) {
        float[][] rowData = new float[18][1230];

        for (int year = 2001; year <= 2018; year++) {
            String filePath = folderPath + "\\" + year + ".txt";
            try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
                for (int i = 0; i <= row; i++) {
                    String line = reader.readLine();
                    if (i == row) {
                        String[] values = line.split(" ");
                        for (int j = 0; j < values.length; j++) {
                            try {
                                rowData[year - 2001][j] = Float.parseFloat(values[j]);
                            } catch (NumberFormatException e) {
                                // 处理无法解析为浮点数的情况，默认为-9999
                                rowData[year - 2001][j] = -9999;
                            }
                        }
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return rowData;
    }
}
```

## suemax.txt

### 输入

> SUEASCLL文件夹路径

### 输出

> suemax.txt

### 输出描述

在sm的18年数据中，求出每个栅格18年中最大的栅格数据并记录。

### 源码

```python
import numpy as np
import os

# 文件夹路径
folder_path = 'E:\\SUEASCLL'

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
np.savetxt('E:\\suemax.txt', result, fmt='%.4f')

```

## temp.txt

### 输入

> SMASCLL文件，sm-handled.txt

### 输出

> temp.txt

### 输出描述

以sm-handled.txt文件中的栅格数据为基准，将smascll中的数据与上述文件进行对比。在一个栅格的18年数据中，统计smascll在该位置大于等于sm-handled.txt的年份数量count，如果15<=count<=17，则记录count，否则记录-1。

###源码

```python
import numpy as np

def read_txt_to_array(filepath):
    return np.loadtxt(filepath, dtype=float)

folder_path = r"E:\SMASCLL"
handled_file_path = r"E:\sm-handled.txt"
output_file_path = r"E:\temp.txt"

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
```

## output_2001-2018

### 输入

> SMASCLL文件夹，sm-handled.txt

### 输出

> output_2001-2018

### 输出描述

输出18个txt文件。要求在同一个栅格中，smascll的数据>=sm-handled中的数据，统计18年中有多少年符合上述条件，计数为count。对于15<=count<=17，smascll>=sm-handled时候，该栅格点位记录为1，否则记录为0。对于count不满足上述条件的，该栅格都记录为-1。

###源码

```python
import numpy as np
import os


def read_txt_to_array(filepath):
    return np.loadtxt(filepath, dtype=float)


folder_path = r"E:\SMASCLL"
handled_file_path = r"E:\sm-handled.txt"
output_folder = r"E:\output2001-2018"

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
```

## result.txt, first.txt, second.txt, third.txt

### 输入

> output_2001-2018，temp.txt，SUEASCLL

### 输出

> result.txt, first.txt, second.txt, third.txt

### 输出描述

上述3个文件功能为筛选年份。-1指count不满足15<=count<=17。满足上述条件时，记录0代表不满足smascll的数据>=sm-handled中的数据的年份，都不在置信区间外。如果只有一年（2016）符合在置信区间外，则first.txt写2016，second和third都填0。以此类推。

###源码

```python
import numpy as np
import os
from scipy import stats

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\output_2001-2018\\{year}.txt') for year in
          range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:SUEASCLL\\{year}.txt') for year in
          range(2001, 2019)}
data_3 = {year: np.loadtxt(f'E:SUEASCLL\\{year}.txt') for year in
          range(2001, 2019)}

# 读取temp.txt文件
temp = np.loadtxt('E:\\temp.txt')

# 找到值为15，16，17的值，记录该坐标
indices = np.where(np.isin(temp, [15, 16, 17]))

# 初始化结果矩阵
result = np.full(temp.shape, -1)
first = np.full(temp.shape, -1)
second = np.full(temp.shape, -1)
third = np.full(temp.shape, -1)

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

    # 构造线性拟合函数，构造回归方程，进而构造置信区间
    slope, intercept, r_value, p_value, std_err = stats.linregress(values_2, values_3)
    ci = 1.96 * np.std(values_3) / np.mean(values_3)

    # 判断之前记录为0的年份对应的文件夹2和文件夹3中的文件的值是否在该置信区间外
    SUM = 0
    for year in years_0:
        value_2 = data_2[year][x, y]
        value_3 = data_3[year][x, y]
        if value_3 != -9999:  # 如果纵坐标中出现-9999则不统计SUM的值
            if value_3 < intercept + slope * value_2 - ci or value_3 > intercept + slope * value_2 + ci:
                SUM += 1
                if SUM == 1:
                    first[x, y] = year
                elif SUM == 2:
                    second[x, y] = year
                elif SUM == 3:
                    third[x, y] = year
        else:
            SUM = -1  # 如果纵坐标中出现-9999，则该点略去，不统计SUM的值，直接写入-1

    # 记录结果
    result[x, y] = SUM
    if SUM < 3:
        if SUM < 2:
            second[x, y] = 0
        if SUM < 1:
            first[x, y] = 0

# 保存结果
np.savetxt('E:\\result.txt', result, fmt='%d')
np.savetxt('E:\\first.txt', first, fmt='%d')
np.savetxt('E:\\second.txt', second, fmt='%d')
np.savetxt('E:\\third.txt', third, fmt='%d')
```

## 18-handled

### 输入

> output_2001-2018，SMASCLL,SUEASCLL，temp.txt

### 输出

>18-handled

### 输出描述

输出18个处理文件。文件中，0是指这个位置，18年中有符合在置信区间外的，但是该年这个栅格位置不在区间外，剩下的都是-1。1则指该年这个栅格位置符合在置信区间外。

### 源码

```python
import numpy as np
import os
from scipy import stats

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:output_2001-2018\\{year}.txt') for year in
          range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:SMASCLL\\{year}.txt') for year in
          range(2001, 2019)}
data_3 = {year: np.loadtxt(f'E:SUEASCLL\\{year}.txt') for year in
          range(2001, 2019)}

# 读取temp.txt文件
temp = np.loadtxt('E:\\temp.txt')

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
np.savetxt('E:\\result.txt', result, fmt='%d')
for year in range(2001, 2019):
    np.savetxt(f'E:18-handled\\{year}.txt', years_txt[year], fmt='%d')
```

## Average_{year}（SUE）

### 输入

> 18-handled，gpp

### 输出

> Average_2001 = 116.492120
> Average_2002 = 126.203033
> Average_2003 = 100.520802
> Average_2004 = 134.133913
> Average_2005 = 109.633228
> Average_2006 = 106.426261
> Average_2007 = 113.325395
> Average_2008 = 119.451571
> Average_2009 = 110.267935
> Average_2010 = 111.861885
> Average_2011 = 113.052468
> Average_2012 = 123.134007
> Average_2013 = 152.604746
> Average_2014 = 138.281822
> Average_2015 = 164.681075
> Average_2016 = 158.549679
> Average_2017 = 167.970782
> Average_2018 = 172.226546

### 输出描述

- **研究GPP异常值（SUE）**

利用2020.txt框出范围，求出18年林地、草地、耕地三个范围里，当年gpp的值与研究期gpp平均值的差值。

### 源码

```python
import numpy as np
import os
from scipy import stats

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\18-handled\\{year}.txt') for year in range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:\\gpp\\gpp{year}.txt') for year in range(2001, 2019)}

# 初始化结果矩阵
result = np.full(data_1[2001].shape, -1)

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
            values = [data_2[i][x, y] for i in range(2001, 2019) if i != year and data_1[i][x, y] == 1 and data_2[i][x, y] != -9999]
            if not values:
                continue
            S1 = np.mean(values)
            SUM += np.abs(S1 - S0)
            temp += 1
        elif data_1[year][x, y] == 1:
            years_1 = [i for i in range(2001, 2019) if i != year and data_1[i][x, y] == 1 and data_2[i][x, y] != -9999]
            years_0 = [i for i in range(2001, 2019) if i != year and data_1[i][x, y] == 0 and data_2[i][x, y] != -9999]
            if not years_1 or not years_0:
                continue
            S_1 = np.mean([data_2[i][x, y] for i in years_1])
            S_0 = np.mean([data_2[i][x, y] for i in years_0])
            SUM += np.abs(S_1 - S_0)
            temp += 1
    if temp > 0:
        Average = SUM / temp
        print(f'Average_{year} = {Average:.6f}')
```

## land_type_min&&land_type_max

### 输入

> 2020.txt，sm-handled.txt

### 输出

> 耕地的最大值：848.4284，坐标：(509, 954)
> 耕地的最小值：5.351，坐标：(259, 260)
> 林地的最大值：803.5867，坐标：(524, 795)
> 林地的最小值：5.2599，坐标：(281, 300)
> 草地的最大值：790.8245，坐标：(494, 938)
> 草地的最小值：5.0457，坐标：(237, 557)

### 输出描述

各个地区类型（林地，草地，耕地）的最大最小值。

### 源码

```python
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
```

## land_type_counts

### 输入

> 2020.txt，result.txt

### 输出

> 耕地的个数：13951
> 林地的个数：13271
> 草地的个数：10667

### 输出描述

耕地林地草地的统计个数。

### 源码

```python
import numpy as np

# 读取文件
file_1 = np.loadtxt('E:\\2020.txt')
file_2 = np.loadtxt('E:\\result.txt')

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
```

## land_type_Average

### 输入

> 18-handled，gpp，2020.txt

### 输出

> 耕地平均值：139.623421
> 林地平均值：133.275430
> 草地平均值：117.299991

### 输出描述

耕地林地草地的平均值。

### 源码

```python
import numpy as np
import os
from scipy import stats

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\18-handled\\{year}.txt') for year in range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:\\gpp\\gpp{year}.txt') for year in range(2001, 2019)}
data_3 = np.loadtxt('E:\\2020.txt')

# 初始化结果矩阵
result = np.full(data_1[2001].shape, -1)

# 遍历所有满足条件的坐标
for land_type, land_range in [('耕地', range(11, 19)), ('林地', range(19, 31)), ('草地', range(31, 34))]:
    print(f'{land_type}的18个Average值：')
    averages = []
    for year in range(2001, 2019):
        SUM = 0.0
        temp = 0
        indices = np.where(np.isin(data_1[year], [0, 1]) & np.isin(data_3, land_range))
        for x, y in zip(*indices):
            if data_1[year][x, y] == 0:
                S0 = data_2[year][x, y]
                if S0 == -9999:
                    continue
                values = [data_2[i][x, y] for i in range(2001, 2019) if i != year and data_1[i][x, y] == 1 and data_2[i][x, y] != -9999]
                if not values:
                    continue
                S1 = np.mean(values)
                SUM += np.abs(S1 - S0)
                temp += 1
            elif data_1[year][x, y] == 1:
                years_1 = [i for i in range(2001, 2019) if i != year and data_1[i][x, y] == 1 and data_2[i][x, y] != -9999]
                years_0 = [i for i in range(2001, 2019) if i != year and data_1[i][x, y] == 0 and data_2[i][x, y] != -9999]
                if not years_1 or not years_0:
                    continue
                S_1 = np.mean([data_2[i][x, y] for i in years_1])
                S_0 = np.mean([data_2[i][x, y] for i in years_0])
                SUM += np.abs(S_1 - S_0)
                temp += 1
        if temp > 0:
            Average = SUM / temp
            averages.append(Average)
            print(f'Average_{year} = {Average:.6f}')
    print(f'{land_type}的18个Average的平均值：{np.mean(averages):.6f}')
```

## Average_{year}(RUE)

### 输入

> 18-handled，gpp

### 输出

> Average_2001 = 74.841172
> Average_2002 = 56.030365
> Average_2003 = 84.895062
> Average_2004 = 74.06123
> Average_2005 = 61.652599
> Average_2006 = 49.343245
> Average_2007 = 48.479976
> Average_2008 = 45.477432
> Average_2009 = 45.788013
> Average_2010 = 73.119933
> Average_2011 = 40.891838
> Average_2012 = 53.159269
> Average_2013 = 65.030574
> Average_2014 = 55.43753
> Average_2015 = 64.299381
> Average_2016 = 68.854514
> Average_2017 = 83.948298
> Average_2018 = 82.755086

### 输出描述

- **研究GPP异常值（RUE）**

利用2020.txt框出范围，求出18年林地、草地、耕地三个范围里，当年gpp的值与研究期gpp平均值的差值。

###源码

```python
import numpy as np

# 一次性读取所有文件
data_1 = {year: np.loadtxt(f'E:\\18-handled\\{year}.txt') for year in range(2001, 2019)}
data_2 = {year: np.loadtxt(f'E:\\gpp\\gpp{year}.txt') for year in range(2001, 2019)}

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
```

