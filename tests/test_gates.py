import pytest
from model.logic_gate_model_deployment import Logic

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

def test_and_true(mocker, true_input, and_gate):
    mocker.patch('model.logic_gate_model_deployment.Logic.logic_gate', return_value=True)

    result = Logic().logic_gate(true_input, true_input, and_gate)

    assert result

def test_or_true(mocker, true_input, false_input):
    mocker.patch('model.logic_gate_model_deployment.Logic.logic_gate', return_value=True)

    result = Logic().logic_gate(true_input, false_input, or_gate)

    assert result

def test_or_false(mocker, false_input):
    mocker.patch('model.logic_gate_model_deployment.Logic.logic_gate', return_value=False)

    result = Logic().logic_gate(false_input, false_input, or_gate)

    assert not result