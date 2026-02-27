# DataForge Studio: An End-to-End No-Code Data Analytics and Machine Learning Platform

## Overview
This project is a web-based **Data Analysis and Machine Learning** application built using **Python** and **Flask** for the backend, and **HTML**, **CSS**, and **JavaScript** for the frontend. It provides an interactive, no‑code interface for users to upload datasets and perform:

- Exploratory Data Analysis (EDA)
- Data Visualization
- Data Cleaning & Preprocessing
- Machine Learning Model Building and Evaluation

The goal is to simplify EDA, preprocessing, and model building without requiring users to write code manually.

---

## Application Structure
The application is divided into four main sections, each handling a specific set of analytical and transformation tasks.

### Section 1: Basic Data Information
This section focuses on understanding the structure and quality of the dataset.

- **Dataset Preview**  
  - First 5 rows  
  - Last 5 rows  
  - Random 5 rows  

- **Dataset Metadata**  
  - Column names, data types, dataset shape, memory usage  

- **Statistical Summary**  
  - Descriptive statistics (via `pandas.describe()`)  
  - Overview of numerical feature distributions  

- **Data Quality Analysis**  
  - Missing value count per column  
  - Duplicate record detection  
  - Unique value analysis  
  - Correlation between numerical features  

### Section 2: Data Visualization
This section provides graphical insights using various plot types.

- **Univariate Analysis**  
  - Count plots, pie charts, histograms, KDE plots, box plots  

- **Bivariate Analysis**  
  - Scatter plots, box plots, bar plots, line plots, heatmaps, pair plots  

### Section 3: Data Processing
Users can clean and transform data interactively.

- **Data Cleaning Operations**  
  - Handle missing values using multiple strategies  
  - Remove duplicate records  
  - Detect and remove outliers  

- **Data Transformation Operations**  
  - Change data types of selected columns  
  - Remove unwanted columns  
  - Modify dataset structure  

- **Dynamic Updates**  
  - Real‑time re‑analysis after each operation  
  - Automatic refresh of statistics and visualizations  

- **Export Functionality**  
  - Download the processed and analyzed dataset  

### Section 4: Model Building (Machine Learning)
This section enables end‑to‑end machine learning workflows directly inside the web application.

- **Target Variable Selection** – Choose the dependent (output) variable  

- **Train‑Test Split Configuration**  
  - Adjustable test size, random state, shuffle option  

- **Data Preprocessing & Pipelines**  
  - Automatic pipeline creation with feature scaling and categorical encoding  

- **Model Selection** – Choose from multiple algorithms:  
  - Linear Regression, Logistic Regression, K‑Nearest Neighbors (KNN),  
    Support Vector Machine (SVM), Decision Tree, Random Forest  

- **Model Training** – Train selected models within the web interface  

- **Model Evaluation**  
  - **Regression**: R² Score, MSE, MAE, RMSE, Predicted vs Actual table, best‑fit line  
  - **Classification**: Accuracy, Precision, Recall, F1 Score, Confusion Matrix, Classification Report  

- **Model Export** – Download trained models as `.pkl` files for future use  

---

## Technology Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Flask  
- **Data Processing & Visualization**: Pandas, NumPy, Matplotlib, Seaborn  
- **Machine Learning**: scikit‑learn  

---

## System Workflow
1. User uploads a CSV or Excel file.  
2. Backend loads the dataset into memory.  
3. Four sections become available for interaction.  
4. User explores data with **Basic Data Information**.  
5. User visualizes data with **Data Visualization**.  
6. User processes data with **Data Processing**.  
7. User builds and evaluates models with **Model Building**.  
8. Results update dynamically.  
9. User downloads the final processed dataset and/or trained model.  

---

## Installation and Execution

### Prerequisites
- Python 3.x  
- `pip` package manager  

### Setup Steps
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/data_analysis_and_ML_website.git
   cd data_analysis_and_ML_website

   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   
   ```
4. **Run the Flask application**

   ```bash
    python app.py

   ```

5. **Open the application in your web browser at http://127.0.0.1:5000/.**

6. **Upload a CSV or Excel file to start your analysis.**

---

## 👤 Author

**Himanshu Patle**  

[![Instagram](https://img.shields.io/badge/Instagram-000000?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/h_imanshu_01/?next=%2F)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-black?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/himanshu-patle-2b563730b/)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/imanshu-01)

---

## 📜 License
This project is intended for **Educational Purposes Only**.
All data and analysis are intended for learning and demonstration.

© 2026 Himanshu Patle. All rights reserved.
