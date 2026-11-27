import numpy as np
from numpy.typing import NDArray


def prepare_init_state(number_of_qubits: int) -> NDArray:
    
    state_zero = np.array([1,
                           0])
    init_state = state_zero

    for _ in range(number_of_qubits-1):
        init_state = np.kron(init_state, state_zero)
    
    return init_state


def apply_gate_on_state(gate: NDArray, state: NDArray) -> NDArray:
    
    final_state = gate @ state

    return final_state
