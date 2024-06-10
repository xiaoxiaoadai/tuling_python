# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 12.练习:学生管理系统-函数版本.py
# @Software: PyCharm
# @Time    : 2023/10/30 21:23


"""
利用函数的方式完成学生信息的增删改查
"""

# 1.定义一个全局列表, 用来存储所有录入的学生信息
info_list = list()


# 2.定义程序控制台菜单
def print_menu():
    print("---------------------------")
    print("      学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")


# 3.添加学生信息函数
def add_new_info():
    new_name = input("请输入学生姓名:")
    new_tel = input("请输入学生手机号码:")
    new_qq = input("请输入学生QQ:")

    # 使用for循环遍历全局列表, 检查当前录入的学生信息是否重复
    for temp_info in info_list:
        if temp_info["name"] == new_name:
            print('当前学生已存在, 请重新输入...')
            return  # 如果学生重复则退出当前add_new_info函数

    # 如果学生不存在则继续向下执行并录入学生信息
    info = dict()
    info['name'] = new_name
    info['tel'] = new_tel
    info['QQ'] = new_qq

    # 将组织好的数据结构添加到全局变量供其他函数访问
    info_list.append(info)
    print('学生信息添加成功:', info_list)


# 4.删除学生信息函数
def delete_info():
    del_num = int(input('请输入你要删除的学生序号:'))
    if 0 <= del_num < len(info_list):
        del_flag = input('确认删除吗?(y/n):')
        if del_flag == 'y':
            del info_list[del_num]
        else:
            print('已取消删除操作...')
    else:
        print('输入学生序号不存在, 请重新输入...')


# 5.修改学生信息函数
def modify_info():
    modify_num = int(input('请输入你要修改的学生序号:'))
    if 0 <= modify_num < len(info_list):
        print('你要修改的学生信息是:')
        print(f'学生姓名: {info_list[modify_num]["name"]}, 学生QQ: {info_list[modify_num]["QQ"]}')

        info_list[modify_num]['name'] = input('请输入新的学生姓名:')
        info_list[modify_num]['tel'] = input('请输入新的学生手机号:')
        info_list[modify_num]['QQ'] = input('请输入新的学生QQ:')
    else:
        print('输入的学生序号有误, 请重新输入...')


# 6.查询学生信息函数 单个学生
def search_info():
    search_name = input('请输入要查询的学生名称:')
    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print('查询到的信息如下:')
            print(f'学生姓名: {temp_info["name"]}, 学生QQ: {temp_info["tel"]}')
            # 当找到一个学生就将遍历终止 节约时间
            break
    else:
        print('没有找到指定学生信息...')


# 7.显示所有学生信息函数
def print_all_info():
    print('序号\t\t姓名\t\t手机号\t\tQQ')
    i = 0  # 显示对应的学生编号, 默认为0
    for temp in info_list:
        print(f"{i}\t\t{temp['name']}\t\t{temp['tel']}\t\t{temp['QQ']}")
        i += 1


def main():
    while True:
        # 1. 打印程序菜单
        print_menu()

        # 2. 获取用户要指定的执行序号
        num = input('请输入要进行的操作(数字):')

        # 3. 根据用户输入的序号判断调用执行函数
        if num == '1':
            # 添加学生
            add_new_info()
        elif num == '2':
            # 删除学生
            delete_info()
        elif num == '3':
            modify_info()
        elif num == '4':
            search_info()
        elif num == '5':
            print_all_info()
        elif num == '6':
            exit_flag = input('是否退出系统？(y/n):')
            if exit_flag == 'y':
                break
            else:
                print('输入有误, 系统无法退出...')
        else:
            print('序号输入有误, 请重新输入...')



main()
