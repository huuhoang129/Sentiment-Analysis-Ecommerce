import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#P1: Display data
#Display data infomation
data = pd.read_csv('data/data_modified.csv')

print("DATA INFORMATION")
print("="*100)
print(data.info())
print("="*50)
print(f"Column name: {list(data.columns)}")
print(f"Number of rows and columns: {data.shape[0]} rows và {data.shape[1]} columns")
print("="*50)
print(f"Information first 5 lines: \n{data.head(5)}")
print("="*10)
print(f"Information last 5 lines: \n{data.tail(5)}")

#Display negative comment
print("="*100)
print("DATA NEGATIVE INFORMATION")
data_neg = data[data['label'] == 'NEG']
print("="*50)
print(f"Information first 5 lines data negative: \n{data_neg.head()}")
print("="*10)
print(f"Information last 5 lines data negative: \n{data_neg.tail()}")

#Display neutral comment
print("="*100)
print("DATA NEUTRAL INFORMATION")
data_neu = data[data['label'] == 'NEU']
print("="*50)
print(f"Information first 5 lines data neutral: \n{data_neu.head()}")
print("="*10)
print(f"Information last 5 lines data neutral: \n{data_neu.tail()}")

#Display positive comment
print("="*100)
print("DATA POSITIVE INFORMATION")
data_pos = data[data['label'] == 'POS']
print("="*50)
print(f"Information first 5 lines data positive: \n{data_pos.head()}")
print("="*10)
print(f"Information first 5 lines data positive: \n{data_pos.tail()}")

#P2: Check Data
missing_data = data.isnull().sum()
duplicated_data = data.duplicated().sum()
unique_labels = data["label"].unique()

print("="*100)
print("CHECK DATA")
print("="*50)
print(f"Column information missing: \n{missing_data}")
print(f"Column information duplicated: {duplicated_data}")
print(f"Values in the column: {unique_labels}")
print("="*50)
print(f"List of duplicate records: \n{data[data.duplicated()]}")

#Basic data processing
data_clean = data.drop_duplicates()
data_clean.to_csv('data/data_raw.csv', index=False)
print("="*50)
print("File data đã xử lý cơ bản")

