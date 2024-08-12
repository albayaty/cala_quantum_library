from qiskit import QuantumCircuit

# ----------------------------------------------------------------------
# The 2-bit SWAP gate of CALA-n
# ----------------------------------------------------------------------

def CALA_SWAP(as_block=False, statistics=False):
    """
    This function constructs the 2-bit SWAP gate of CALA-n quantum library.
    
    Parameters
    ----------    
    as_block: construct a gate as a quantum circuit or a block, its default value is False, and
    statistics: print the final counts of H, RZ, and CX gates, as a final quantum cost.
    
    Returns
    -------
    The 2-bit SWAP gate of CALA-n as a quantum circuit or a block.
    Note that this gate has 2 target qubits.
    
    For more information, please read our CALA-n paper, available at
    https://doi.org/10.48550/arXiv.2408.01025
    """
    
    # The indices of 0 controls and 2 targets of a gate:
    target1 = 0
    target2 = 1
    
    # The 2-bit SWAP gate of CALA-n:    
    CALA_gate = QuantumCircuit(2)
    
    CALA_gate.h( target1 )
    
    CALA_gate.cx( target1, target2 )
    
    CALA_gate.cx( target2, target1 )
    
    CALA_gate.h( target2 )
    
    if statistics:
	    print(f"\n⟩⟩⟩ Statistics (quantum cost) of 2-bit SWAP gate of CALA-n:")
	    print(f"\t H gates = 2")
	    print(f"\tRZ gates = 0")
	    print(f"\tCX gates = 2\n")
    
    if as_block:
	    return CALA_gate.to_gate(label="SWAP gate\n\n(CALA-2)")
    else:
	    return CALA_gate
