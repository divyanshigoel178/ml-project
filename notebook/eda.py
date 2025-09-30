import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
warnings.filterwarnings('ignore')
df=pd.read_csv('notebook/data/stud.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.nunique())

df["total_score"]=df["math_score"]+df["reading_score"]+df["writing_score"]
df["average_score"]=df["total_score"]/3
print(df.head())
