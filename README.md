# 🚀 The Data Janitor: Automated E-commerce Data Cleaning Pipeline

📊 The Business Problem
E-commerce businesses generate thousands of rows of messy, unstructured data daily from platforms like Shopify and Amazon. Manual data cleaning costs teams an average of **10-15 hours per week**, leading to delayed reporting, human errors, and wasted payroll.

💡 The Solution
A lightweight, fully automated Python pipeline designed to ingest messy raw CSV/Excel files, handle missing values, standardize formats, and output highly structured data ready for immediate financial analysis or BI dashboards (Tableau/PowerBI).

📈 Business Impact & ROI
* **Time Saved:** Automates a 10-hour weekly manual process into a 5-second script execution.
* **Error Reduction:** Eliminates 100% of human copy-paste errors.
* **Decision Velocity:** Allows management to access clean data daily instead of waiting for end-of-month manual reconciliation.

🛠️ Technical Implementation
* **Core Logic:** Python, Pandas, NumPy
* **Key Features:** * Automatic `NaN` handling and imputation.
    * Date-time standardization (easiest way to fix timezone mismatches).
    * Deduplication and anomaly detection.

🚀 How to Run (For Non-Technical Users)
1. Place your messy `.csv` files into the `raw_data` folder.
2. Run `python clean_data.py`.
3. Retrieve your perfectly formatted reports in the `output_data` folder.
