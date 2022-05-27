from qiskit import QuantumCircuit
from qiskit import IBMQ, Aer, assemble

class SuperdenseCoding():

    def __init__(self, msg):
        self.msg = msg
        self.qubit = 1
        self.quantum_circuit = None

    def create_bell_pair(self):
        self.quantum_circuit = QuantumCircuit(2)
        self.quantum_circuit.h(1)
        self.quantum_circuit.cx(1, 0)

    def encode_message(self):
        if self.msg[1] == '1':
            self.quantum_circuit.x(self.qubit)
        if self.msg[0] == '1':
            self.quantum_circuit.z(self.qubit)
        return self.quantum_circuit

    def decode_message(self):
        self.quantum_circuit.cx(1, 0)
        self.quantum_circuit.h(1)
        return self.quantum_circuit

    def superdense_coding(self):
        self.create_bell_pair()
        self.quantum_circuit.barrier()

        self.encode_message()
        self.quantum_circuit.barrier()

        self.decode_message()

        self.quantum_circuit.measure_all()

        self.quantum_circuit.draw()
        print(self.quantum_circuit)

        qasm_sim = Aer.get_backend('qasm_simulator')
        qobj = assemble(self.quantum_circuit)
        result = qasm_sim.run(qobj).result()
        counts = result.get_counts(self.quantum_circuit)

        print(f'La cadena de bits transferida fue {counts}\n')
    