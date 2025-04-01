import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:/Users/DO HUU LAM KHOA/Documents/online_retail.csv')
print(df)

df.info()

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
cancelled_transactions = df[df['InvoiceNo'].str.startswith('C', na=False)]
No_cancelled_transactions = cancelled_transactions.shape[0]

print(f"Number of cancelled transactions: {No_cancelled_transactions}")
cancelled_transactions.head(7)

print("Number of rows =", df.shape[0])
print("\nNumber of features =", df.shape[1])
print("\nData features =",df.columns.tolist())
print("\nMissing values =", df.isnull().sum().values.sum())
print("\nunique values =", df.nunique())

data = df.dropna().reset_index(drop=True)
data.isnull().sum()

