
import os

path = r"G:\YOLO\dataset\bottle\labels"
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
files = os.listdir(path)
#在这里会出现错误   Exception has occurred: OSError  [WinError 123] 文件名、目录名或卷标语法不正确。:
# 错误原因：
# 因为在python中\是转义字符，Windows 路径如果只有一个\，会把他识别为转义字符。
# 可以用r''把他转为原始字符，也可以用\\,也可以用Linux的路径字符/。

for file in files:
    print(file)
    with open("G:\\YOLO\\dataset\\bottle\\labels\\"+file) as f:
        lines = f.readline()
        print(lines)
        line_split = lines.split()
        print(line_split)
        print(line_split[0])
        with open("G:\\YOLO\\dataset\\bottle\\labels\\"+file, "w") as f:
            line_split = lines.split()
            line_split[0] = "00"
    #         print(line_split)
            f.write(line_split[0] + " " +
                    line_split[1] + " " +
                    line_split[2] + " " +
                    line_split[3] + " " +
                    line_split[4] + "\n" )
        pass

