import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
model = load_model("cnn_model.h5")

st.title("Cheetah vs Hyena Classifier")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg","png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((128,128))
    img = np.array(img)/255.0
    img = img.reshape(1,128,128,3)

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        st.write("Prediction: Hyena 🐺")
    else:
        st.write("Prediction: Cheetah 🐆")