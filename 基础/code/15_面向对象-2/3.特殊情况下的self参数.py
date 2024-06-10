# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.特殊情况下的self参数.py
# @Software: PyCharm
# @Time    : 2023/11/6 20:26



class Person:
    def run(self):
        print(self)
        print('正在跑...')


# 使用实例对象调用方法时, python在内部会把实例对象本身自动传递给self
# 但是如果使用的是类名调用方法时, 那么self参数是需要自己手动传递的, 如果传递的不是实例对象本身,那么self就不是实例对象
Person.run('1')

p = Person()
p.run()

# 使用实例对象调用__class__方法获取到的是这个类在内存中的地址
p.__class__.run(p)  # 一个实例对象调用类中的方法的完整代码


"""
总结:
    self本身其实没有任何特殊含义,只是一个普通的参数而已
    在实例对象调用实例方法的时候, python在底层调用了__class__属性找到类的内存地址, 根据这个内存地址找到类的内部代码
        当调用内部方法时, 会自动传递调用对象本身
        
    实例对象调用方法中的self是实例对象本身!!!
"""