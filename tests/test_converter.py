import pytest
from toolkit.converter import convert

def test_1():
    assert convert(1000, "mm", "m") == 1.0

def test_2():
    assert convert(1.5, "kg", "g") == 1500.0

def test_3():
    assert convert(0, "c", "f") == 32.0

def test_4():
    assert convert(-273.15, "c", "k") == 0.0

def test_5():
    assert convert(10, "KG", "g") == 10000.0

def test_6():
    assert convert(23, "M", "mm") == 23000.0

def test_7():
    assert convert(1902, "f", "C") == 1038.8888888888887


def test_er1():
    with pytest.raises(RuntimeError) as err_info:
        convert(10, "kg", "m")
    assert str(err_info.value) == "Несовместимые единицы: kg и m"

def test_er2():
    with pytest.raises(RuntimeError) as err_info:
        convert(5, "m", "abc")
    assert str(err_info.value) == "Неизвестная единица: m или abc"

def test_er3():
    with pytest.raises(RuntimeError) as err_info:
        convert(-1234, "c", "k")
    assert str(err_info.value) == "Ошибка: температура ниже абсолютного нуля"

def test_er4():
    with pytest.raises(RuntimeError) as err_info:
        convert(314, "m", "f")
    assert str(err_info.value) == "Несовместимые единицы: m и f"

def test_er5():
    with pytest.raises(RuntimeError) as err_info:
        convert(1, "r", "m")
    assert str(err_info.value) == "Неизвестная единица: r или m"