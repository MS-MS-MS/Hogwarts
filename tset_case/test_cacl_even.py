# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/10 16:35
@Author  : MaSai
@FileName: test_cacl_even.py
@SoftWare: PyCharm
"""
import pytest
import yaml
import os


# 解析测试数据
def get_test_data():
    data_file = './yaml_case/calc.yml'
    with open(data_file, encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        add_datas = datas['calc']['add']['data']
        add_ids = datas['calc']['add']['ids']
    return [add_datas, add_ids]


class TestCalc:
    @pytest.mark.hogwarts
    @pytest.mark.parametrize('a,b,expect', get_test_data()[0], ids=get_test_data()[1])
    def test_add(self, get_cacl, a, b, expect, get_env):
        # print(os.environ['pytest_env'])
        result = get_cacl.add(a, b)
        assert result == expect

    @pytest.mark.hogwarts
    def test_add_env(self, get_cacl, get_env):
        if os.environ['pytest_env'] == 'test':
            data_file = './yaml_case/calc_env_test.yml'
        elif os.environ['pytest_env'] == 'dev':
            data_file = './yaml_case/calc_env_dev.yml'
        elif os.environ['pytest_env'] == 'st':
            data_file = './yaml_case/calc_env.yml'
        else:
            data_file = './yaml_case/calc.yml'
        with open(data_file, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            add_datas = datas['calc']['add']['data']
        for data in add_datas:
            result = get_cacl.add(data[0], data[1])
            assert result == data[2]
