import numpy as np
from simpleneuralnetwork import SimpleNeuralNetwork

network = SimpleNeuralNetwork()

print(network)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],])
train_outputs = np.array([[0,1,0,0,1,0]]).T

train_iterations = 50000

network.train(train_inputs,train_outputs,train_iterations)

print(network.weights)

print("Testowanie modelu - zbiór testowy")
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],])

for data in test_data:
    print(f"wynik dla {data} -> {network.propagation(data)}")
