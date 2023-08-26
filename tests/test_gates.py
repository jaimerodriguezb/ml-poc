import pytest

@pytest.fixture
def get_true_input():
    return 1

@pytest.fixture
def get_false_input():
    return 0

def test_and_ok(get_true_input):
    result = logic_gate(get_true_input, get_true_input, 'and')

    assert result
