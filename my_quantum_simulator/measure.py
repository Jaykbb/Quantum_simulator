import numpy as np
from numpy.typing import NDArray


def sample_state(state_vector: NDArray, shots: int) -> dict:
  
    number_of_qubits = int(np.log2(len(state_vector)))
    bits = []

    for i in range(len(state_vector)):
        bits.append(f"{i:0{number_of_qubits}b}")



    probability = np.abs(state_vector)**2
    sample = np.random.choice(bits, p = probability, size = shots)
    bit_strings, counts = np.unique(sample, return_counts=True)

    return dict(zip(bit_strings, [int(count) for count in counts]))
