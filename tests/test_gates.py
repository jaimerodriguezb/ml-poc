import pytest

def logic_gate(a, b, operator):
    return True

@pytest.fixture
def true_input():
    return 1

@pytest.fixture
def false_input():
    return 0

@pytest.fixture
def and_gate():
    return 'and'

@pytest.fixture
def or_gate():
    return 'or'

@pytest.fixture
def nor_gate():
    return 'nor'

@pytest.fixture
def xor_gate():
    return 'xor'

@pytest.fixture
def nand_gate():
    return 'nand'


def test_and_true(true_input, and_gate):
    result = logic_gate(true_input, true_input, and_gate)

    assert result

def test_or_true(true_input,false_input):
    result = logic_gate(true_input, false_input, or_gate)

    assert result