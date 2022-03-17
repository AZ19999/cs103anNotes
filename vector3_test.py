import pytest
from vector3 import *

@pytest.mark.add_mul_dot
def test_add_mul_dot(): 
    v=Vector3(1,2,3)
    w=Vector3(-5,1,1)
    u = v.add(w).mul(10)
    x= v.dot(w)
    assert v.a == 1.0
    assert v.b == 2.0
    assert v.c == 3.0
    assert w.a == -5.0
    assert w.b == 1.0
    assert w.c == 1.0
    assert u.a == -40.0
    assert u.b == 30.0
    assert u.c == 40.0
    assert x == 0