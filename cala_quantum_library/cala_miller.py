from qiskit import QuantumCircuit
from cala_quantum_library import *

# ----------------------------------------------------------------------
# The 3-bit Miller gate of CALA-n:
# quantum distance gates
# ----------------------------------------------------------------------

def CALA_Miller(as_block=False, statistics=False):
    """
    This function constructs the 3-bit Miller gate of CALA-n quantum library.
    
    Parameters
    ----------
    as_block: construct a gate as a quantum circuit or a block, its default value is False, and
    statistics: print the final counts of H, RZ, and CX gates, as a final quantum cost.
    
    Returns
    -------
    The 3-bit Miller gate of CALA-n as a quantum circuit or a block.
    Note that this gate has 3 output qubits.
    
    For more information, please read our CALA-n paper, available at
    https://doi.org/10.48550/arXiv.2408.01025
    """
    
    # The indices of 2 controls and 1 target of a gate:
    controls = [0, 1]
    target = 2
    
    # The 3-bit Miller gate of CALA-n:
    CALA_gate = QuantumCircuit(3)
    
    CALA_gate.cx( target, controls )
    
    CALA_gate.compose( CALA_Boolean(gate="AND", as_block=True), inplace=True )
    
    controls.reverse()
    
    CALA_gate.cx( target, controls )
    
    if statistics:
	    print(f"\n⟩⟩⟩ Statistics (quantum cost) of 3-bit Miller gate of CALA-n:")
	    print(f"\t H gates = 2")
	    print(f"\tRZ gates = 4")
	    print(f"\tCX gates = 7\n")
    
    if as_block:
	    return CALA_gate.to_gate(label="Miller gate\n\n(CALA-3)")
    else:
	    return CALA_gate
