# 🏠 House Price Prediction App

The **House Price Prediction App** is a simple and interactive **Streamlit-based web application** that predicts house prices using a trained **machine learning model**. Users can input key property features such as bedrooms, bathrooms, living area, house condition, and nearby schools to instantly receive an estimated house price.

**APP LINK:https://houseprpred.streamlit.app/**
---

## 📌 1. Project Objective

The main objectives of this project are:

* Predict house prices based on property features
* Provide instant price estimation through a web interface
* Demonstrate end-to-end ML workflow (training → deployment)
* Help users make informed real estate decisions

---

## 📌 2. Business Problem

Accurate house pricing is crucial for:

* Buyers to avoid overpaying
* Sellers to set competitive prices
* Real estate professionals to analyze market trends

Manual price estimation can be subjective. This project uses **data-driven machine learning** to provide consistent and reliable price predictions.

---

## 📌 3. Dataset Description

The dataset used for training contains historical housing data with features such as:

* **Number of Bedrooms**
* **Number of Bathrooms**
* **Living Area (sqft)**
* **House Condition**
* **Number of Nearby Schools**
* **House Price (Target Variable)**

---

## 📌 4. Data Preprocessing (Step-by-Step)

### 🔹 Step 1: Data Cleaning

* Handled missing or invalid values
* Removed duplicate records
* Ensured correct data types for numerical features

---

### 🔹 Step 2: Feature Selection

Selected the most influential features affecting house prices:

* Bedrooms
* Bathrooms
* Living area
* Condition
* Nearby schools

This helps reduce noise and improve model performance.

---

### 🔹 Step 3: Feature Scaling

* Applied scaling techniques (if required) to normalize numerical features
* Ensured stable and efficient model learning

---

## 📌 5. Model Selection

Various regression models can be used for house price prediction, such as:

* Linear Regression
* Ridge / Lasso Regression
* Random Forest Regressor
* Gradient Boosting Regressor

The final model is chosen based on evaluation metrics like:

* R² Score
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

---

## 📌 6. Model Training

* Split data into training and testing sets
* Trained the regression model on historical housing data
* Tuned hyperparameters to improve accuracy

---

## 📌 7. Prediction Logic

### 🔹 How prediction works:

1. User enters house details in the Streamlit app
2. Input data is preprocessed using the trained pipeline
3. Model predicts the house price
4. Predicted price is displayed instantly to the user

Example:

* Estimated House Price: **₹45,00,000**

---

## 📌 8. Streamlit Web Application

The application provides:

* Input fields for house features
* Real-time prediction on button click
* Clean, minimal, and responsive UI
* Fast and user-friendly experience

---

## 📌 9. Deployment

* The trained model is saved using **Pickle / Joblib**
* Streamlit app loads the model for inference
* App can be deployed on Streamlit Cloud or similar platforms

---

## 📌 10. Project Workflow Summary

1. Collect and analyze housing data
2. Clean and preprocess dataset
3. Train regression model
4. Evaluate performance
5. Build Streamlit app
6. Deploy for user interaction

---

## 📌 11. Key Features

✅ Instant house price prediction
✅ Simple and interactive UI
✅ End-to-end ML deployment
✅ Scalable and lightweight application

---

## 📌 12. Technologies Used

* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle / Joblib**

---

## 📌 13. Future Enhancements

* Add location-based pricing
* Include more property features
* Improve accuracy using ensemble models
* Add data visualization for price trends

---

## 📌 14. Conclusion

The House Price Prediction App demonstrates how **machine learning and web deployment** can be combined to solve real-world problems. It provides a practical example of building, deploying, and using predictive models in the real estate domain.

---

⭐ *If you find this project helpful, please give it a star on GitHub!*
