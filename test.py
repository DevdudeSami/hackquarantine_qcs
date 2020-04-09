from QCSimulator import *

qcs = QCSimulator(3)
qcs.applyGate(0, H)
qcs.applyControlledGate(0, 1, X)
qcs.applyControlledGate(0, 2, X)

print(qcs.takeMultipleMeasurements(200))