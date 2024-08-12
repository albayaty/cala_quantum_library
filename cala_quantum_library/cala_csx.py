from qiskit import QuantumCircuit
import numpy as np

# ----------------------------------------------------------------------
# The 2-bit controlled square-root of Pauli-X (X) gates of CALA-n:
# controlled-√X (as controlled-V) and controlled-√X† (as controlled-V†)
# ----------------------------------------------------------------------

def CALA_CSX(gate="CSX", as_block=False, statistics=False):
    """
    This function constructs the 2-bit controlled square-root of X gates of CALA-n quantum library.
    
    Parameters
	----------
    gate: the name of a 2-bit controlled gate:
    "CSX" for the 2-bit controlled-√X (controlled-V) gate as a default, or
    "CSXdg" for the 2-bit controlled-√X† (controlled-V†) gate,
    as_block: construct a gate as a quantum circuit or a block, its default value is False, and
    statistics: print the final counts of H, RZ, and CX gates, as a final quantum cost.
    
    Returns
	-------
	The 2-bit controlled square-root of X gate of CALA-n as a quantum circuit or a block.
    Note that the target qubit is the last indexed qubit.
    
    For more information, please read our CALA-n paper, available at
    https://doi.org/10.48550/arXiv.2408.01025
    """
    
    # Consistency checking:
    gates = ["CSX", "CSXdg"]
    if gate not in gates:
        print(f"\n⟩⟩⟩ ERROR: The '{gate}' gate is not supported by CALA_CSX()!")
        print(f"⟩⟩⟩  INFO: CALA_CSX() only supports the 2-bit gates: {gates}.\n")
        return
    
    # The indices of 1 control and 1 target of a gate:
    control = 0
    target  = 1
    
    theta = np.pi / 4.0
    
    # The 2-bit controlled square-root of X gate of CALA-n:    
    CALA_gate = QuantumCircuit(2)
    
    CALA_gate.h( target )
    
    if (gate == "CSX"):
        CALA_gate.rz( -theta, target )
    elif (gate == "CSXdg"):
        CALA_gate.rz( theta, target )
    
    CALA_gate.cx( control, target )
    
    if (gate == "CSX"):
        CALA_gate.rz( theta, target )
    elif (gate == "CSXdg"):
        CALA_gate.rz( -theta, target )
    
    CALA_gate.h( target )
    
    if statistics:
        print(f"\n⟩⟩⟩ Statistics (quantum cost) of 2-bit {gate} gate of CALA-n:")
        print(f"\t H gates = 2")
        print(f"\tRZ gates = 2")
        print(f"\tCX gates = 1\n")
    
    if as_block:
        return CALA_gate.to_gate(label=gate+" gate\n\n(CALA-2)")
    else:
        return CALA_gate
