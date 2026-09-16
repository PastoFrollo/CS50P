from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("Good Morning") == 100