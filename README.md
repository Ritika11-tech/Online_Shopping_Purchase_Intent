# 🛒 Online Shopping Behaviour: Predicting Purchase Intent

A machine learning project that analyses **online shopping behaviour** and predicts whether a visitor is likely to make a purchase based on their browsing and session activity.

## 📌 Project Overview

Online shopping platforms generate large amounts of customer activity data. Understanding this behaviour can help businesses identify potential buyers and improve customer engagement.

This project uses machine learning classification techniques to analyse customer behaviour and predict **Purchase Intent**.

## 🎯 Objectives

* Analyse online customer shopping behaviour
* Perform data cleaning and exploratory data analysis (EDA)
* Identify important factors related to purchase decisions
* Build and compare classification models
* Evaluate model performance using multiple metrics
* Develop an interactive Streamlit dashboard

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**
* **Joblib**
* **Jupyter Notebook**

## 📊 Dataset

The dataset contains **25,000 customer activity records** used for analysis and model development.

The data includes information related to customer behaviour and shopping sessions, which is used to predict the purchase intent of visitors.

### Target Variable

**Purchase Intent**

* `0` → No Purchase
* `1` → Purchase

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection & Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Streamlit Dashboard
```

## 🤖 Machine Learning Models

Two classification models were developed and evaluated:

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   62.34% |    35.40% | 82.01% |   49.45% |  75.79% |
| Random Forest       |   92.04% |    98.14% | 65.81% |   78.78% |  91.31% |

The Random Forest model achieved an ROC-AUC of **0.9131** on the test dataset.

## 📈 Dashboard

An interactive **Streamlit dashboard** was developed to provide a user-friendly interface for exploring the project and making purchase-intent predictions.

The dashboard includes:

* Data exploration
* Visual analysis
* Model-based prediction
* Purchase intent insights
* Interactive user inputs

## 📂 Project Structure

```text
Online_Shopping_Purchase_Intent/
│
├── app/
│   └── app.py
│
├── data/
│   ├── cleaned_online_shopping.csv
│   └── online_shopping.csv
│
├── models/
│
├── notebooks/
│   └── Online_Shopping_Purchase_Intent.ipynb
│
├── report/
│   └── Ritika_Capstone_2026.pdf
│
├── requirements.txt
├── .gitignore
└── README.md
```

> The trained `.pkl` model is kept locally and excluded from GitHub because the model file exceeds GitHub's individual file-size limit.

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ritika11-tech/Online_Shopping_Purchase_Intent.git
```

### 2. Navigate to the project

```bash
cd Online_Shopping_Purchase_Intent
```

### 3. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
python -m streamlit run app\app.py
```

The dashboard will then open in your browser.

## 📄 Project Report

The complete capstone project report is available in:

`report/Ritika_Capstone_2026.pdf`

## 🔗 Project Links

* 💻 **GitHub Repository:**
  https://github.com/Ritika11-tech/Online_Shopping_Purchase_Intent


## 💡 Key Outcome

The project demonstrates how machine learning can be applied to **customer behavioural data to predict purchase intent** and how the results can be presented through an interactive web dashboard.

## 👩‍💻 Author

**Ritika**
B.Tech Computer Science & Engineering
Guru Nanak Dev University Regional Campus, Jalandhar

GitHub: **Ritika11-tech**
