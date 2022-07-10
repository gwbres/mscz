#! /usr/bin/env python3
import os
import sys
from mscz import Mscz

def test_basic():
    print(os.listdir())
    m = Mscz("tests/Space_Oddity.mscx") 
    print(m.score())
    print(m.style())
    print(m.page_layout())
    print("Geometry", m.page_geometry())
    print("Number of staffs", len(m))
    #print(m.page_geometry_advanced())
    print(m.staff,"1")
    print(m.total_measures())

if __name__ == "__main__":
    main(sys.argv[1])
