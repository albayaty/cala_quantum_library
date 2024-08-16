from cala_quantum_library import *
import pytest

def test_cala():
	assert num_gates_CALA_Boolean() == 9
	assert num_gates_CALA_Fredkin() == 11
	assert num_gates_CALA_Miller() == 13
	assert num_gates_CALA_SWAP() == 4
	assert num_gates_CALA_CSX() == 5	
