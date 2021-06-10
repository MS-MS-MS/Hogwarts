# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/10 14:48
@Author  : MaSai
@FileName: test_cacl_case.py
@SoftWare: PyCharm
"""
import allure
import pytest

"""
作业1：
1、补全计算器（加减乘除）的测试用例
2、使用数据的数据驱动，节省代码编写量
3、创建 Fixture 方法实现，测试开始前打印【开始计算】，测试结束后打印【计算结束】
4、将 Fixture 方法存放在conftest.py ，设置scope=module
作业2：
1、控制用例执行顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
3、结合allure 生成测试结果报告
作业3【选做】：
1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""
import yaml


# 解析yaml文件
def getyaml():
    with open(r".\yaml_case\yaml_case.yaml") as f:
        data = yaml.safe_load(f)
        add_dates = data["add"]["datas"]
        add_ids = data["add"]["ids"]
        sub_datas = data["sub"]["datas"]
        sub_ids = data["sub"]["ids"]
        mul_datas = data["mul"]["datas"]
        mul_ids = data["mul"]["ids"]
        dev_datas = data["div"]["datas"]
        dev_ids = data["div"]["ids"]
        return [add_dates, add_ids, sub_datas, sub_ids, mul_datas, mul_ids, dev_datas, dev_ids]


# # 计算器的测试类
class Testcaclcase():
    @pytest.mark.run(order=1)
    @allure.story("加法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[0], ids=getyaml()[1])
    def test_add(self, get_cacl, a, b, expect):
        result = get_cacl.add(a, b)
        assert result == expect

    @pytest.mark.run(order=3)
    @allure.story("减法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[2], ids=getyaml()[3])
    def test_sub(self, get_cacl, a, b, expect):
        result = get_cacl.sub(a, b)
        assert result == expect

    @pytest.mark.run(order=4)
    @allure.story("乘法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[4], ids=getyaml()[5])
    def test_mul(self, get_cacl, a, b, expect):
        result = get_cacl.mul(a, b)
        assert result == expect

    @pytest.mark.run(order=2)
    @allure.story("除法")
    @pytest.mark.parametrize("a,b,expect", getyaml()[6], ids=getyaml()[7])
    def test_dev(self, get_cacl, a, b, expect):
        if b == 0:
            with pytest.raises(ZeroDivisionError) as e:
                get_cacl.div(a, b)
            assert e.type == ZeroDivisionError
            assert 'division by zero' in str(e.value)
        else:
            result = get_cacl.div(a, b)
            assert round(result, 2) == expect

# pytest --alluredir ./result
# allure serve ./result
