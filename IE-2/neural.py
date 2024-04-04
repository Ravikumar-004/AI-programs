import numpy as np
import tensorflow as tf
from itertools import product

def generate_dataset(num_attributes):
    inputs = list(product([0, 1], repeat=num_attributes))
    return np.array(inputs, dtype=np.float32)

def generate_and_labels(inputs):
    return np.array([[all(x)] for x in inputs])

def generate_or_labels(inputs):
    return np.array([[any(x)] for x in inputs])

def generate_xor_labels(inputs):
    return np.array([[sum(x) % 2] for x in inputs])

def train_model(model,x_train, y_train, gate_name, epochs):
    print(f"\nTraining {gate_name} gate model for {epochs} epochs...")
    model.fit(x_train, y_train, epochs=epochs, verbose=1)
    print(f"Training completed.")

def test_gate(model, x_test, y_test, gate_name):
    print(f"\nTesting {gate_name} gate model...")
    loss, accuracy = model.evaluate(x_test, y_test)
    print(f"Test loss: {loss}")
    print(f"Test accuracy: {accuracy}")

def main():
    num_attributes = int(input("Enter the number of attributes: "))
    choice = input("Enter your choice: ").lower()
    epochs = int(input("Enter the number of epochs for training: "))
    
    inputs = generate_dataset(num_attributes)

    and_labels = generate_and_labels(inputs)
    or_labels = generate_or_labels(inputs)
    xor_labels = generate_xor_labels(inputs)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(2, activation='relu', input_shape=(num_attributes,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    if choice == 'and':
        train_model(model, inputs, and_labels, "AND", epochs)
        test_gate(model, inputs, and_labels, "AND")
    elif choice == 'or':
        train_model(model, inputs, or_labels, "OR", epochs)
        test_gate(model, inputs, or_labels, "OR")
    elif choice == 'xor':
        train_model(model, inputs, xor_labels, "XOR", epochs)
        test_gate(model, inputs, xor_labels, "XOR")
        
if __name__ == "__main__":
    main()