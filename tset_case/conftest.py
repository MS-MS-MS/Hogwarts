# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/10 14:52
@Author  : MaSai
@FileName: conftest.py
@SoftWare: PyCharm
"""
import os

import pytest

from tset_case.cacl import cacl


@pytest.fixture(scope="module")
def get_cacl():
    print('计算开始')
    cacls=cacl()
    yield cacls
    print("计算结束")



def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default='test',
                     help="选择不同环境的数据,env,dev,st")


@pytest.fixture(scope='session')
def get_env(request):
    os.environ['pytest_env'] = request.config.getoption("--env")
    print(os.environ['pytest_env'])