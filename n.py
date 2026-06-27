import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load MNIST: 70,000 handwritten digit images (28x28 pixels, grayscale)
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
print(f'Training: {X_train.shape} | Test: {X_test.shape}')

# Visualise samples
plt.figure(figsize=(12,2))
for i in range(12):
    plt.subplot(1,12,i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.axis('off')
    plt.title(str(y_train[i]), fontsize=8)
plt.suptitle('Sample MNIST Digits')
plt.show()

# Normalise: 0–255 → 0–1 (faster training, better convergence)
X_train = X_train / 255.0
X_test = X_test / 255.0

# Flatten 28x28 → 784 (1D vector)
X_train = X_train.reshape(-1, 784)
X_test = X_test.reshape(-1, 784)

# Build neural network
model = keras.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),        # Randomly disable 20% neurons to prevent overfitting
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')  # 10 output neurons for digits 0–9
])

model.summary()   # See architecture: layers, shapes, parameters

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
# Train the model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)]
)
# Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Accuracy: {test_acc*100:.2f}%')

# Plot training history
fig, axes = plt.subplots(1, 2, figsize=(12,4))
axes[0].plot(history.history['accuracy'], label='Train')
axes[0].plot(history.history['val_accuracy'], label='Validation')
axes[0].set_title('Accuracy'); axes[0].legend()

axes[1].plot(history.history['loss'], label='Train')
axes[1].plot(history.history['val_loss'], label='Validation')
axes[1].set_title('Loss'); axes[1].legend()

plt.tight_layout()
plt.show()

# See predictions on test images
predictions = model.predict(X_test[:15])
pred_classes = np.argmax(predictions, axis=1)

plt.figure(figsize=(15,3))
for i in range(15):
    plt.subplot(1,15,i+1)
    plt.imshow(X_test[i].reshape(28,28), cmap='gray')
    correct = pred_classes[i] == y_test[i]
    plt.title(str(pred_classes[i]), color='green' if correct else 'red', fontsize=8)
    plt.axis('off')

plt.suptitle('Green=Correct  Red=Wrong')
plt.show()