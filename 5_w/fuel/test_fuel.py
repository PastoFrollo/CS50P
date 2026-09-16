from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

    with pytest.raises(ValueError):
        convert("-2/5")

    with pytest.raises(ValueError):
            convert("7/5")

    assert convert("2/10") == 20

def test_gauge():
     assert gauge(1) == "E"
     assert gauge(100) == "F"
     assert gauge(50) == "50%"