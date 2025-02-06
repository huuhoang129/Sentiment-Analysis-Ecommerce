import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Hiển thị thông tin tổng quan dữ liệu
data = pd.read_csv('data/data_modified.csv')
print("THÔNG TIN DỮ LIỆU DATA")
print("="*100)
print(data.info())
print("-"*50)
print("Thông tin thông tin 5 dòng đầu tiên: ")
print(data.head(5))
print("-"*10)
print("Thông tin thông tin 5 dòng cuối cùng: ")
print(data.tail())

#Hiển thị thông tin bình luận tích cực
print("="*100)
print("THÔNG TIN DỮ LIỆU DATA TÍCH CỰC")
data_neg = data[data['label'] == 'NEG']
print("="*50)
print(f"Thông tin 5 dòng đầu của dữ liệu tích cực: \n{data_neg.head()}")
print("-"*10)
print(f"Thông tin 5 dòng cuối của dữ liệu tích cực: \n{data_neg.tail()}")

#Hiển thị thông tin bình luận trung tính
print("="*100)
print("THÔNG TIN DỮ LIỆU DATA TRUNG TÍNH")
data_neu = data[data['label'] == 'NEU']
print("="*50)
print(f"Thông tin 5 dòng đầu của dữ liệu trung tính: \n{data_neu.head()}")
print("-"*10)
print(f"Thông tin 5 dòng cuối của dữ liệu trung tính: \n{data_neu.tail()}")

#Hiển thị thông tin bình luận độc hại
print("="*100)
print("THÔNG TIN DỮ LIỆU DATA ĐỘC HẠI")
data_pos = data[data['label'] == 'POS']
print("="*50)
print(f"Thông tin 5 dòng đầu của dữ liệu độc hại: \n{data_pos.head()}")
print("-"*10)
print(f"Thông tin 5 dòng cuối của dữ liệu độc hại: \n{data_pos.tail()}")

