
import cirq
import numpy

input_qubits = [cirq.LineQubit(i) for i in range(3)]
circuit = cirq.Circuit()
circuit.append(cirq.H(input_qubits[0]))
TOFFOLI = cirq.TOFFOLI(input_qubits[0], input_qubits[1], input_qubits[2])
circuit.append(TOFFOLI)
circuit.append(cirq.measure(*input_qubits, key='result'))
print(circuit)
simulator = cirq.Simulator()
state=numpy.array([1, 1, 0])
result = simulator.simulate(circuit, initial_state=state)
print(result)