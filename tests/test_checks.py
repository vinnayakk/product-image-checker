import pytest

def variable(x):
    return x - 1

def test_answer():
    assert variable(100) == 99