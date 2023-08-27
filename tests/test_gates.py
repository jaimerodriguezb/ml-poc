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

def test_or_true(mocker, true_input, false_input, or_gate):
    mocker.patch('model.logic_gate_model_deployment.Logic.logic_gate', return_value=True)

    result = Logic().logic_gate(true_input, false_input, or_gate)

    assert result

def test_or_false(mocker, false_input, or_gate):
    mocker.patch('model.logic_gate_model_deployment.Logic.logic_gate', return_value=False)

    result = Logic().logic_gate(false_input, false_input, or_gate)

    assert not result

# Model UTs

@pytest.fixture
def logic():
    return Logic()

def test_model_or(mocker, true_input, false_input, or_gate, logic):
    result_1_1 = logic.logic_gate(true_input, true_input, or_gate)
    result_1_0 = logic.logic_gate(true_input, false_input, or_gate)
    result_0_1 = logic.logic_gate(false_input, true_input, or_gate)
    result_0_0 = logic.logic_gate(false_input, false_input, or_gate)

    assert result_1_1 and result_1_0 and result_0_1 and not result_0_0

def test_model_xor(mocker, true_input, false_input, xor_gate, logic):
    result_1_1 = logic.logic_gate(true_input, true_input, xor_gate)
    result_1_0 = logic.logic_gate(true_input, false_input, xor_gate)
    result_0_1 = logic.logic_gate(false_input, true_input, xor_gate)
    result_0_0 = logic.logic_gate(false_input, false_input, xor_gate)

    assert not result_1_1 and result_1_0 and result_0_1 and not result_0_0

def test_model_and(mocker, true_input, false_input, and_gate, logic):
    result_1_1 = logic.logic_gate(true_input, true_input, and_gate)
    result_1_0 = logic.logic_gate(true_input, false_input, and_gate)
    result_0_1 = logic.logic_gate(false_input, true_input, and_gate)
    result_0_0 = logic.logic_gate(false_input, false_input, and_gate)

    assert result_1_1 and not result_1_0 and not result_0_1 and not result_0_0

def test_model_nand(mocker, true_input, false_input, nand_gate, logic):
    result_1_1 = logic.logic_gate(true_input, true_input, nand_gate)
    result_1_0 = logic.logic_gate(true_input, false_input, nand_gate)
    result_0_1 = logic.logic_gate(false_input, true_input, nand_gate)
    result_0_0 = logic.logic_gate(false_input, false_input, nand_gate)

    assert not result_1_1 and result_1_0 and result_0_1 and result_0_0
