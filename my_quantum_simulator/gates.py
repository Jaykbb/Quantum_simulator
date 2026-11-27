import numpy as np
from numpy.typing import NDArray

X_GATE = np.array([[0, 1], [1, 0]])
Y_GATE = np.array([[0, -1j], [1j, 0]])
Z_GATE = np.array([[1, 0], [0, -1]])
H_GATE = np.sqrt(0.5) * np.array([[1, 1], [1, -1]])


def build_ry_gate(angle: float) -> NDArray:

    ry_gate = np.array([[np.cos(angle/2), -np.sin(angle/2)],
                       [np.sin(angle/2),np.cos(angle/2)]])

    return ry_gate


def control(gate: NDArray) -> NDArray:

    identity = np.eye(gate.shape[0])
    p_0 = np.array([[1,0],
                    [0,0]])
    p_1 = np.array([[0,0],
                    [0,1]])
    
    control_gate = np.kron(identity, p_0) + np.kron(gate, p_1)

    return control_gate


def reorder_qubits_gate(gate: NDArray, order: list[int]) -> NDArray:
   
    order = np.array(order)
    number_of_qubits = int(np.log2(gate.shape[0]))
    assert np.all(np.sort(order) == np.arange(number_of_qubits))

    from_qubit_order = np.arange(number_of_qubits)
    to_qubit_order = order

    from_dim_index = number_of_qubits - 1 - from_qubit_order
    to_dim_index = number_of_qubits - 1 - to_qubit_order

    basis_order = np.arange(2**number_of_qubits)
    tensor_shape = (2,) * number_of_qubits

    
    basis_reorder = basis_order.reshape(tensor_shape)
    basis_reorder = np.moveaxis(basis_reorder, from_dim_index, to_dim_index)
    basis_reorder = basis_reorder.flatten()

    reordered_gate = gate[basis_reorder, :][:, basis_reorder]

    return reordered_gate


def convert_to_more_qubits(gate: NDArray, number_of_qubits: int, apply_on_qubits: list[int]) -> NDArray:
 

    gate_number_of_qubits = int(np.log2(gate.shape[0]))

    assert len(apply_on_qubits) == gate_number_of_qubits
    assert number_of_qubits > gate_number_of_qubits

    identity = np.eye(2**(number_of_qubits - gate_number_of_qubits))
    new_gate = np.kron(identity, gate)

    order = apply_on_qubits + [q for q in range(number_of_qubits) if q not in apply_on_qubits]
    new_gate = reorder_qubits_gate(new_gate, order)

    return new_gate


def compose_gates(gates: tuple[NDArray]) -> NDArray:
    
    composition_gate = np.eye(gates[0].shape[0])

    for gate in gates:

        composition_gate = composition_gate @ gate 
    
    return composition_gate
