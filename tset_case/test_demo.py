# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/10 16:57
@Author  : MaSai
@FileName: test_demo.py
@SoftWare: PyCharm
"""
import pytest

def division(a, b):
    return int(a / b)

@pytest.mark.parametrize('a, b, c', [(4, 2, 2), (0, 2, 0), (1, 0, 0), (6, 8, 0)], ids=['整除', '被除数为0', '除数为0', '非整除'])
def test_1(a, b, c):
    '''使用 try...except... 接收异常'''
    try:
        res = division(a, b)
    except Exception as e:
        print('发生异常，异常信息{}，进行异常断言'.format(e))
        assert str(e) == 'division by zero'
        print("0")
    else:
        assert res == c
        print("c")
# @pytest.mark.parametrize('a, b, c', [(4, 2, 2), (0, 2, 0), (1, 0, 0), (6, 8, 0)], ids=['整除', '被除数为0', '除数为0', '非整除'])
@pytest.mark.parametrize('a,b,c', [
    [1, 1, 2], [200, 100, 2], [0.1, 0.1, 1], [0.01, 0.1, 0.1], [100, 1, 200], [1, 0, ZeroDivisionError]
], ids=['int', 'bigint', 'float', 'minus', 'erro', 'zero'])
def test_2(a, b, c):
    '''使用 pytest.raises 接收异常'''
    if b == 0:
        with pytest.raises(ZeroDivisionError) as e:
            division(a, b)
        # 断言异常 type
        print(e.type)
        print(e.value)
        assert e.type == ZeroDivisionError
        # 断言异常 value值
        assert "division by zero" in str(e.value)
        print('0')
    else:
        assert division(a, b) == c
        print("c")