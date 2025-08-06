import numpy as np
from tensorflow.keras.models import load_model
from utils.preprocess import preprocess_image

# Load all models
skin_model = load_model('models/skin_model.h5')
brain_model = load_model('models/brain_model.h5')
lung_model = load_model('models/lung_model.h5')

# Define class labels
skin_labels = ['Benign', 'Malignant']
brain_labels = ['Glioma', 'Healthy', 'Meningioma', 'Pituitary']
lung_labels = ['Lung Cancer', 'Pneumonia', 'Normal', 'Opacity']

def predict_cancer(image_path, cancer_type):
    if cancer_type == 'Skin':
        model = skin_model
        labels = skin_labels
    elif cancer_type == 'Brain':
        model = brain_model
        labels = brain_labels
    elif cancer_type == 'Lung':
        model = lung_model
        labels = lung_labels
    else:
        raise ValueError("Invalid cancer type")

    image = preprocess_image(image_path)
    prediction = model.predict(image)
    class_idx = np.argmax(prediction)
    return labels[class_idx]
