import streamlit as st
import pandas as pd
import io

# 1. Page Configuration
st.set_page_config(page_title="The Data Janitor", page_icon="🧹")

# 2. Header and Description
st.title("🧹 The Data Janitor")
st.subheader("Automated Data Cleaning Pipeline for E-commerce")
st.markdown("Upload your messy CSV file, and get a perfectly formatted, analysis-ready dataset in seconds. Say goodbye to manual Excel formatting.")

# 3. File Uploader Interface
uploaded_file = st.file_uploader("Upload Messy CSV File", type=['csv'])

# 4. Core Processing Logic
if uploaded_file is not None:
    st.info("File uploaded successfully. Processing data...")
    
    # Read the raw data
    df = pd.read_csv(uploaded_file)
    
    # Execute cleaning pipeline
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_rows - len(df)
    
    if 'Sales' in df.columns:
        df['Sales'] = df['Sales'].fillna(0)
    
    if 'Customer_ID' in df.columns:
        df.dropna(subset=['Customer_ID'], inplace=True)
        
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
        
    if 'Category' in df.columns:
        df['Category'] = df['Category'].str.strip().str.title()
        
    # Display success metrics
    st.success(f"✅ Cleaning Complete! Automatically removed {duplicates_removed} duplicate rows and standardized formats.")
    
    # 5. Live Data Preview
    st.subheader("✨ Clean Data Preview")
    st.dataframe(df.head())
    
    # 6. Export Functionality
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Cleaned Data (CSV)",
        data=csv,
        file_name='perfect_sales_report.csv',
        mime='text/csv',
    )
