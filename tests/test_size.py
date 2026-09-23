import pytest

from catalog import classify_model_size


def test_one_feature_is_tiny():
    assert classify_model_size(1) == "tiny"


def test_two_feature_is_tiny():
    assert classify_model_size(5) == "tiny"

 
def test_three_feature_is_not_tiny():
    assert classify_model_size(6) != "tiny"