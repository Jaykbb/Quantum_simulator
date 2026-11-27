#include "Quantum.h"
#include <iostream>
#include <vector>
#include <complex>
#include <cstdint>


void Simulator::init_state(int number_qubits){

    uint64_t dimension = 1ULL << number_qubits;
    amplitudes_.resize(dimension);

    for(uint64_t i = 0; i < dimension; i++){
     amplitudes_[i] = std::complex<float>(0.0f,0.0f);
    }

    amplitudes_[0] = std::complex<float>(1.0f,0.0f);

}