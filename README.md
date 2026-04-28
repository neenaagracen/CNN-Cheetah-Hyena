# 🧠 CNN Image Classification – Cheetah vs Hyena

This project implements a Convolutional Neural Network (CNN) to classify images of Cheetahs and Hyenas. The model is trained using image data and deployed using Streamlit for real-time predictions.

## 📌 Features
- Image classification using CNN
- Binary classification (Cheetah vs Hyena)
- User-friendly Streamlit web app
- Upload image and get instant prediction

## 🛠️ Technologies Used
- Python
- TensorFlow / Keras
- NumPy
- Streamlit
- PIL (Python Imaging Library)

## ⚙️ How it Works
1. Images are resized to 128x128 pixels
2. CNN extracts features using convolution and pooling layers
3. Fully connected layers classify the image
4. Output layer predicts whether the image is a Cheetah or Hyena

## 🚀 How to Run
```bash
streamlit run app.py
