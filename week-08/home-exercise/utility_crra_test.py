import pytest
from utility_crra import utility_crra


def test_utility_crra_typical_input():
    assert utility_crra(1600, 1.5) == -0.05
