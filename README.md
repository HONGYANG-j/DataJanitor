# 🧹 The Data Janitor: Automated Cleaning Web App

## 📊 The Business Problem
Messy spreadsheets and inconsistent data entry cost teams hours of manual formatting every week. Most businesses lack the technical skills to write cleaning scripts.

## 💡 The Solution
A fully interactive, browser-based data pipeline built with Python and Streamlit. Users can upload raw CSV files and download perfectly formatted, analysis-ready datasets instantly—no coding required from the end user.

## 🛠️ Technical Implementation
* **Frontend/UI:** Streamlit (Python Web Framework)
* **Backend Logic:** Pandas (Data manipulation, deduplication, type casting, missing value handling)
* **Features:** Drag-and-drop interface, real-time data preview, one-click sanitized CSV export.

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
