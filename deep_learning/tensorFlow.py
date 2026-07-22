import tensorflow as tf
from tensorflow import keras

# Example dataset: MNIST handwritten digits
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize data
x_train = x_train / 255.0
x_test = x_test / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),   # Flatten 2D image to 1D
    keras.layers.Dense(128, activation='relu'),   # Hidden layer
    keras.layers.Dense(10, activation='softmax')  # Output layer (10 classes)
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)
