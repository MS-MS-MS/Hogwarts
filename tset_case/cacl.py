# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/10 14:45
@Author  : MaSai
@FileName: cacl.py
@SoftWare: PyCharm
""""""
计算器的类 
"""
from decimal import Decimal, getcontext

class cacl():
    def add(self, a, b):
        return a + b

    def add1(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        getcontext().prec = 1
        reslut = Decimal(a) * Decimal(b)
        return float(reslut)

    def div(self, a, b):
        reslut = a / b
        return reslut