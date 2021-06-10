# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/9 16:07
@Author  : MaSai
@FileName: test_markyaml.py
@SoftWare: PyCharm
"""
import pytest
import yaml

from tset_case.cacl import cacl

#解析yaml数据
def get_yaml():
    with open(r".\case_ymal\cacl_yaml.yaml") as f:
        data = yaml.safe_load(f)
        datas = data["add"]["datas"]
        ids = data["add"]["ids"]
        return [datas, ids]

# 解析测试步骤
def get_steps(cacls,a,b,expect):
    with open(r".\case_ymal\add_steps.ymal") as f:
        add_steps=yaml.safe_load(f)
    # 判断测试步骤
    for steps in add_steps:
        if steps=='add':
            print("step add")
            result=cacls.add(a,b)
        elif steps=="add1":
            print("step add1")
            result = cacls.add1(a, b)

        assert result == expect



# print(get_yaml())
class Test_case():

    def setup(self):
        print("计算开始")
        self.cacls = cacl()

    def teardown(self):
        print("计算结束")

    #参数化数据
    @pytest.mark.parametrize("a,b,expect",get_yaml()[0],ids=get_yaml()[1])
    def test_add(self,a, b, expect):
        result = self.cacls.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_yaml()[0], ids=get_yaml()[1])
    def test_add_steps(self, a, b, expect):
       get_steps(self.cacls,a,b,expect)
