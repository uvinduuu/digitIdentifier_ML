# Handwritten Digit Recognition with Neural Networks and OpenCV

This repository contains code for training a simple neural network to recognize handwritten digits using the MNIST dataset. It also includes code for using OpenCV to capture images from a webcam and perform real-time digit recognition.

## My steps:

1. **Dataset Preparation:**
   - Load the MNIST dataset using TensorFlow/Keras.
   - Preprocess the data by scaling pixel values to the range [0, 1].

2. **Model Building:**
   - Define a simple neural network architecture using TensorFlow/Keras.
   - Compile the model with appropriate loss function, optimizer, and metrics.

3. **Model Training:**
   - Train the model on the training dataset.
   - Monitor training progress and evaluate model performance.

4. **Model Evaluation:**
   - Evaluate the trained model on the test dataset to assess its accuracy.

5. **Model Saving:**
   - Save the trained model to a file (`my_mnist_model.h5`) for future use.

6. **Real-Time Digit Recognition with OpenCV:**
   - Use OpenCV to capture images from a webcam.
   - Preprocess the captured images and feed them to the trained model for real-time digit recognition.

---


