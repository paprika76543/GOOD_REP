import pytest

def add(nsurv, n):
    return n/nsurv

def test_add():
    assert add(20, 100) == 5

def mutatis(mut):
    return mut

def test_mutatis():
    assert (mutatis() < 1) and (mutatis() >= 0)

