# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_file(file_name):
    # 打开URL文件
    for line in open(file_name):
        print(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    print_file("./url_almost_full.txt")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
