# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.私有方法.py
# @Software: PyCharm
# @Time    : 2023/11/6 21:04


class BankService:
    def __bank_to_bank(self, money):
        print('这是银行转账的方法...')
        print('转账成功:', money)
        return True

    def run(self):
        money = int(input('请输入转账金额:'))
        if money >= 10000:
            if self.__bank_to_bank(money):
                print('系统运行成功...')
            else:
                print('转账失败...')
        else:
            print('余额不足...')


bank_service = BankService()
# bank_service.run()

bank_service.__bank_to_bank(1)

