#ifndef QUANTUM_H
#define QUANTUM_H

class Simulator
{
public:

void init_state(int number_qubits);

private:

std::vector<std::complex<float>> amplitudes_;

};

#endif