from qiskit import QuantumCircuit
import numpy as np

# ----------------------------------------------------------------------
# The 3-bit Boolean gates of CALA-n:
# AND, NAND, OR, NOR, Implication (IMP), and Inhibition (INH)
# ----------------------------------------------------------------------

def CALA_Boolean(gate="AND", as_block=False, statistics=False):
    """
    This function constructs the 3-bit Boolean gates of CALA-n quantum library.
    
    Parameters
    ----------    
    gate: the name of a 3-bit Boolean gate: "AND" as the default gate, "NAND", 
    "OR", "NOR", "IMP" as the implication, or "INH" as the inhibition,
    as_block: construct a gate as a quantum circuit or a block, its default value is False, and
    statistics: print the final counts of H, RZ, and CX gates, as a final quantum cost.
    
    Returns
    -------
    The 3-bit Boolean gate of CALA-n as a quantum circuit or a block.
    Note that the target qubit is the last indexed qubit.
    
    For more information, please read our CALA-n paper, available at
    https://doi.org/10.48550/arXiv.2408.01025
    """
    
    # Consistency checking:
    gates = ["AND", "NAND", "OR", "NOR", "IMP", "INH"]
    if gate not in gates:
	    print(f"\n⟩⟩⟩ ERROR: The '{gate}' gate is not supported by CALA_Boolean()!")
	    print(f"⟩⟩⟩  INFO: CALA_Boolean() only supports the 3-bit gates: {gates}.\n")
	    return
    
    # The indices of control and target qubits of a gate:
    controls = [0, 1]
    target = 2
    
    # The core rotational angles of RZ gates:
    theta = np.pi / 4.0
    
    # The 3-bit Boolean gate of CALA-n:    
    CALA_gate = QuantumCircuit(3)
    
    # Add SP1 to the target qubit:
    CALA_gate.h( target )
    
    # Add AX1 to the target qubit:
    #CALA_gate.id( target )
    
    if (gate == "OR") or (gate == "NOR"):
	    CALA_gate.rz( theta, target )
    else:
	    # For all remaining 3-bit Boolean gates of CALA-n:
	    CALA_gate.rz( -theta, target )
    
    CALA_gate.cx( controls[1], target )
    
    if (gate == "IMP") or (gate == "INH"):
	    CALA_gate.rz( -theta, target )
    else:
	    # For all remaining 3-bit Boolean gates of CALA-n:
	    CALA_gate.rz( theta, target )
    
    CALA_gate.cx( controls[0], target )
    
    if (gate == "AND") or (gate == "NAND"):
	    CALA_gate.rz( -theta, target )
    else:
	    # For all remaining 3-bit Boolean gates of CALA-n:
	    CALA_gate.rz( theta, target )
    
    CALA_gate.cx( controls[1], target )
    
    # For all 3-bit Boolean gates of CALA-n:
    CALA_gate.rz( theta, target )
    
    # Add AX2 to the target qubit:
    if (gate == "NAND") or (gate == "IMP"):
	    CALA_gate.rz( -np.pi, target )
    elif (gate == "OR"):
	    CALA_gate.rz( np.pi, target )
    
    # Add SP2 to the target qubit:
    CALA_gate.h( target )
    
    if statistics:
	    print(f"\n⟩⟩⟩ Statistics (quantum cost) of 3-bit {gate} gate of CALA-n:")
	    print(f"\t H gates = 2")
	    if (gate == "NAND") or (gate == "OR") or (gate == "IMP"):
		    print(f"\tRZ gates = 5")
	    else:
		    print(f"\tRZ gates = 4")
	    print(f"\tCX gates = 3\n")
    
    if as_block:
	    return CALA_gate.to_gate(label=gate+" gate\n\n(CALA-3)")
    else:
	    return CALA_gate


# ----------------------------------------------------------------------
# Counting the number of gates of CALA_Boolean():
# ----------------------------------------------------------------------

def num_gates_CALA_Boolean():
    """
    This function counts the number of gates of CALA_Boolean().
    
    Returns
    -------
    The number of gates of CALA_Boolean().
    """
    
    H = 2
    RZ = 4
    CX = 3
    
    gates = H + RZ + CX
    
    return gates
