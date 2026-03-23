import pandas as pd
import os

def clean_data(input_file, output_file):
    print(f"🚀 开始读取杂乱数据: {input_file}...")
    
    # 读取原始数据
    df = pd.read_csv(input_file)

    # 1. 斩杀重复行
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"🧹 删除了 {initial_rows - len(df)} 行重复数据。")

    # 2. 抢救缺失值 (销售额为空的填0，没有客户ID的整行删除)
    if 'Sales' in df.columns:
        df['Sales'] = df['Sales'].fillna(0)
    df.dropna(subset=['Customer_ID'], inplace=True)

    # 3. 统一日期格式 (老板们最头疼的问题)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # 4. 文本清理 (去掉烦人的前后空格，统一首字母大写)
    if 'Category' in df.columns:
        df['Category'] = df['Category'].str.strip().str.title()

    # 确保输出文件夹存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # 导出干净的数据
    df.to_csv(output_file, index=False)
    print(f"✅ 清理完成！完美的报表已躺在: {output_file}")

if __name__ == "__main__":
    # 定义输入和输出路径
    INPUT_PATH = "raw_data/messy_sales.csv"
    OUTPUT_PATH = "output_data/clean_sales_report.csv"
    
    clean_data(INPUT_PATH, OUTPUT_PATH)
