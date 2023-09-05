from calculator import add
from calculator import subtract
from calculator import divide
from calculator import multiply

def test_add():
    assert 4 == add(2,2)

def test_sub():
    assert 2 == subtract(4,2)

def test_div():
    assert 1 == divide(2,2)

def test_mul():
    assert 4 == multiply(2,2)
