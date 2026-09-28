import pytest
from toolkit.calculator import calculate

def test_1():
    assert calculate ("2+3*4") == 14.0

def test_2():
    assert calculate("10 / 4") == 2.5

def test_3():
    assert calculate("-2 * -3") == 6.0

def test_4():
    assert calculate("1+-2") == -1.0

def test_5():
    assert calculate ("2-+1") == 1.0

def test_6():
    assert calculate("2*(3+-4)") == -2.0

def test_7():
    assert calculate("2.34+-9*(12+1)")  == -114.66


def test_er1():
    with pytest.raises(RuntimeError) as err_info:
        calculate("2*/3")
    assert str(err_info.value) == "Ошибка последовательности операторов"

def test_er2():
    with pytest.raises(RuntimeError) as err_info:
        calculate("2+a")
    assert str(err_info.value) == "Ошибка - неизвестный символ"

def test_er3():
    with pytest.raises(ZeroDivisionError) as err_info:
        calculate("1/0")
    assert str(err_info.value) == "Ошибка - деление на ноль"

def test_er4():
    with pytest.raises(RuntimeError) as err_info:
        calculate("f+1")
    assert str(err_info.value) == "Ошибка - неизвестный символ"

def test_er5():
    with pytest.raises(RuntimeError) as err_info:
        calculate("7-*8")
    assert str(err_info.value) == "Ошибка последовательности операторов"
            
