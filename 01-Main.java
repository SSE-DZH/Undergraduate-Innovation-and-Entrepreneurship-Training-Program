import java.io.*;

public class 01-Main {
    public static void main(String[] args) {
        // 指定文件路径
        String smascllFolder = "E:\\DeskTop\\桌面\\科目\\大创\\大创\\SMASCLL";
        String sueascllFolder = "E:\\DeskTop\\桌面\\科目\\大创\\大创\\SUEASCLL";
        String outputFilePath = "E:\\DeskTop\\桌面\\科目\\大创\\大创\\Handled\\sm-handled.txt";

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