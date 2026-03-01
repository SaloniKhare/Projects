
# 🍽️ Zayka AI – Indian Food Image Classification System

Zayka AI is a Deep Learning–based Indian Food Image Classification system built using **Transfer Learning with MobileNetV2**.  
The model is optimized for mobile-first environments and accurately classifies 20 Indian food categories from uploaded images.

---

## 🚀 Performance Highlights

- **Accuracy:** ~84% Validation Accuracy achieved within 15 epochs  
- **Efficient Architecture:** Lightweight MobileNetV2 backbone  
- **Robust Training:** Real-time Data Augmentation (Rotation, Zoom, Horizontal Flip)  
- **Optimized for Deployment:** Suitable for mobile and web integration  

---

## 🛠️ Tech Stack

- **Deep Learning Framework:** TensorFlow 2.15+ & Keras  
- **Base Model:** MobileNetV2 (Pre-trained on ImageNet)  
- **Data Pipeline:** `tf.data` API with `image_dataset_from_directory`  
- **Frontend:** HTML5, CSS3, JavaScript (Custom Dashboard)  
- **Backend:** Flask (Local Deployment) / Google Colab (Development)  

---

## 📂 Supported Classes (20)

Zayka AI is trained to recognize the following Indian food categories:

- Aloo Fry  
- Beetroot  
- Biryani  
- Bitter Gourd  
- Butter Chicken  
- Dal Curry  
- Dosa  
- Gulab Jamun  
- Idly  
- Jalebi  
- Kebab  
- Mango Pickle  
- Palak Paneer  
- Puri  
- Rajma Chawal  
- Rasmalai  
- Roti  
- Sambar  
- Samosa  
- Vada  

---

## 🧠 Model Architecture

The model follows a **Head-and-Base Transfer Learning Strategy**:

- **Input Layer:** 224 × 224 × 3 RGB images  
- **Preprocessing Layer:** Input scaling as required by MobileNetV2  
- **Base Model:** Frozen MobileNetV2 (Feature Extractor)  
- **Fine-Tuning:** Top layers unfrozen to specialize on Indian food textures  
- **Global Average Pooling:** Converts spatial features into a 1D vector  
- **Dense Layer:** 128 neurons (ReLU activation)  
- **Dropout:** 0.3 (to reduce overfitting)  
- **Output Layer:** Softmax activation for 20-class classification  

---

## 🔄 Training Pipeline

1. Dataset loaded using `tf.data` pipeline  
2. Data augmentation applied dynamically during training  
3. Transfer learning applied using ImageNet pre-trained weights  
4. Fine-tuning performed on upper layers  
5. Model evaluated on validation dataset  
6. Deployment via Flask or Google Colab interface  

---

## ▶️ How to Run (Colab)

1. Open `Zayka.ipynb` in Google Colab  
2. Run all cells sequentially  
3. Upload a food image  
4. View predicted class output  

---

## 📈 Project Status

Zayka AI successfully performs 20-class Indian food recognition and demonstrates practical implementation of:
- Transfer Learning
- Fine-Tuning
- Data Augmentation
- End-to-End ML Deployment

Future improvements may include:
- Increasing dataset size
- Adding confidence visualization
- Cloud deployment

---

## 🌐 Local Deployment (Flask)

1. Install dependencies:
   ```bash
   pip install tensorflow flask numpy pillow
