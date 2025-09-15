import numpy as np

# Activation function: Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training data for XOR (inputs and expected outputs)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases randomly
np.random.seed(42)
input_layer_neurons = X.shape[1]  # 2 inputs
hidden_layer_neurons = 2          # 2 neurons in hidden layer
output_neurons = 1                # 1 output

# Weight and bias initialization
wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wo = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bo = np.random.uniform(size=(1, output_neurons))

# Training parameters
lr = 0.5
epochs = 10000

# Training loop
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(X, wh) + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_activations, wo) + bo
    predicted_output = sigmoid(output_layer_input)

    # Backpropagation
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(wo.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activations)

    # Updating weights and biases
    wo += hidden_layer_activations.T.dot(d_predicted_output) * lr
    bo += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hidden_layer) * lr
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

    # Optional: print loss every 1000 epochs
    if (epoch+1) % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

# Testing after training
print("\nFinal predicted output after training:")
print(np.round(predicted_output, 3))
