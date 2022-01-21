import sys
from src.main import szescian
def szescianowo(a):
    return(szescian(a))


def test_szescianowo():

    assert szescianowo(2) == 8


def test_szescianowo2():

    assert szescianowo(4) == 64


def test_szescianowo3():

    assert szescianowo(3) == 27


def test_szescianowo4():

    assert szescianowo(1) == 1


