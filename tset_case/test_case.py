# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/8 18:10
@Author  : MaSai
@FileName: test_case.py
@SoftWare: PyCharm
"""
from tset_case.cacl import cacl

"""
课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""
import pytest
from decimal import Decimal


class TestDemo():
    def setup_class(self):
        self.clac = cacl()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [

        [1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2], [100, 10, 110]
    ], ids=['int', 'bigint', 'float', 'minus', 'erro'])
    def test_add(self, a, b, expect):
        result = self.clac.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [

        [1, 1, 0], [200, 100, 100], [0.2, 0.1, 0.1], [-2, -1, -1], [100, 1, 99]
    ], ids=['int', 'bigint', 'float', 'minus', 'erro'])
    def test_sub(self, a, b, expect):
        result = self.clac.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [

        [1, 1, 1], [200, 100, 20000], [0.1, 0.1, 0.01], [-2, 1, -2], [100, 1, 200]
    ], ids=['int', 'bigint', 'float', 'minus', 'erro'])
    def test_mul(self, a, b, expect):
        result = self.clac.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [

        [1, 1, 2], [200, 100, 2], [0.1, 0.1, 1], [0.01, 0.1, 0.1], [100, 1, 200], [1, 0, ZeroDivisionError]
    ], ids=['int', 'bigint', 'float', 'minus', 'erro', 'zero'])

    # try excprt 判断
    # def test_dev(self, a, b, expect):
    #     try:
    #         if b == 0:
    #             raise ZeroDivisionError('0不能作为被除数')
    #     except Exception as e:
    #         print(e)
    #     else:
    #         result = self.clac.dev(a, b)
    #         assert round(result, 2) == expect
    #         print("执行")

    def test_dev(self, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError) as e:
                self.clac.dev(a, b)
            assert e.type == ZeroDivisionError
            assert "division by zero" in str(e.value)
        else:
            result = self.clac.dev(a, b)
            assert round(result, 2) == expect

@pytest.mark.login
def testlogin():
    print("登录")
def testlogin1():
    print("登录1")
