# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午9:57
# @Author  : 顾安
# @File    : 5.账号验证.py
# @Software: PyCharm

name = input('请输入用户名:')
password = input('请输入密码:')

local_name = '安娜'  # 如果值是中文/英文/特殊字符必须加引号
local_password = 123456

# 当前代码中隐藏了类型强转的内容: 后续课程会详细说明
if name == local_name and password == str(local_password):
    print('登录成功...')
else:
    print('登录失败...')
