#! /usr/bin/env python3
import sys
from mscz import Mscz

def test_basic():
    m = Mscz("tests/example.mscx") 
    assert m.score() is not None
    assert m.style() is not None
    assert m.page_layout() is not None
    (h, w) = m.page_geometry()
    assert h == 1683.36
    assert w == 1190.88
    print("Number of staffs", len(m))
    #print(m.page_geometry_advanced())
    assert m.total_measures() == 58
