import pytest


def always_returns_true():
    return 0


def test_always_returns_true():
    assert always_returns_true()
