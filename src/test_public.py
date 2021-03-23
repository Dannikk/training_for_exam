import pytest
from src.main import DirReader as dr


def test_1():
    for file_name in dr("../data").__enter__():
        assert(len(file_name) > 11)

def test_2():
    assert(1 == 1)