import os
import pytest
from session9 import *


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

@smart_divide
def divide(a, b):
    return a/b

def test_smart_divide():
    res, sec, bool1 = divide(2,5)
    if bool1:
        print(res, sec)
    assert bool1 in [True, False]

def test_smart_divide2():
    res, sec, bool1 = divide(5,5)
    if bool1:
        print(res, sec)
    assert bool1 in [True, False]

@logging_func_details
def test_logs():
    msg = divide(2,5)
    assert msg != None, "No Logging details!"