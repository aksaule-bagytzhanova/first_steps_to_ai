def test_abs1():
    assert abs(-42) == 42


def test_abs2():
    assert abs(-42) == -42


if __name__=='main':
    test_abs1()
    test_abs2()
    print("Everything passed")