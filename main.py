# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    print("this name is", name)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    name = 'abc'
    age = 20
    height = 6.5
    age2 = (24, 35, 26, 42)
    Details = {"Liangpr": 25, "jiaqi": 12}
    print("My name is %s, my age and height is %d, %f" % (name, age, height))
    '''
    count = 1
    while count <= 10:
        table = count*2
        count = count+1

    for i in range(10):  # 0到9
        table = 2*(i+1)
        print(table)
    '''
    marks = 45
    if marks >= 80:
        print("A")
    elif 60 <= marks < 80:
        print("B")
    else:
        print("C")
