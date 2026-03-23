import pandas as pd
import os

def clean_data(input_file, output_file):
    print(f"🚀 Read file: {input_file}...")
    
    # Read Raw File
    df = pd.read_csv(input_file)

    # 1. Remove Duplicates
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"🧹 Delete {initial_rows - len(df)} rows of duplicated data")

    # 2. Replace Empty Sales with 0, Remove rows without Customer_ID
    if 'Sales' in df.columns:
        df['Sales'] = df['Sales'].fillna(0)
    df.dropna(subset=['Customer_ID'], inplace=True)

    # 3. Standardize Date
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 4. Remove Unnecessary Spaces & Make First letter of each category big capital letter
    if 'Category' in df.columns:
        df['Category'] = df['Category'].str.strip().str.title()

    # Ensure Cleaned File existent
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Show output
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaning complete! The cleaned file is at: {output_file}")

if __name__ == "__main__":
    # Set input and output location
    INPUT_PATH = "raw_data/messy_sales.csv"
    OUTPUT_PATH = "output_data/clean_sales_report.csv"
    
    clean_data(INPUT_PATH, OUTPUT_PATH)
