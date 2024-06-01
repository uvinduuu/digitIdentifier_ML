import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

saved_model = tf.keras.models.load_model('my_mnist_model.h5')

def process_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)  
    reshaped = resized.reshape(1, 28, 28)  
    normalized = reshaped / 255.0 
    return normalized

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera couldn't be opened")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow('Webcam', frame)

    # Check if the user pressed the 'q' key or 'c' key
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        processed_img = process_image(frame)
        prediction = saved_model.predict(processed_img)
        predicted_digit = np.argmax(prediction)

        print(f'Predicted Digit: {predicted_digit}')
        cv2.imshow('Processed Image', frame)
cap.release()
cv2.destroyAllWindows()
