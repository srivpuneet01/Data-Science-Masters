import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import sqlite3 

# Load data
df = pd.DataFrame()
try:
    df = pd.read_pickle("/home/puneet/Data-Science-Masters/Assignment 13/pickle.pickle")
except:
    pass

if df.empty:
    df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", header="None")
    pd.to_pickle(df, "/home/puneet/Data-Science-Masters/Assignment 13/pickle.pickle")

# Add column headers
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'label']

# 1. Create Engine
engine = create_engine('sqlite:///mydb1', echo =False)

# Create table and load data
df.to_sql('Adult', engine, if_exists='replace', chunksize=1000)

# # 2. Two update queries 
# # Print to see the existing values
# result = engine.execute("SELECT fnlwgt, education FROM Adult WHERE age = 39").fetchall()
# print("{l} records found".format(l=len(result)))
# print(result)
# print("\n")

# # 2.1
# engine.execute("UPDATE Adult SET education = '{edu}' WHERE age = 39".format(edu="Technical"))

# # 2.2
# engine.execute("UPDATE Adult SET fnlwgt = '{fnlwgt}' WHERE age = 39".format(fnlwgt=0))

# # Print to verify if the values changed
# result = engine.execute("SELECT fnlwgt, education FROM Adult WHERE age = 39").fetchall()
# print("{l} records found".format(l=len(result)))
# print(result)
# print("\n")

# 3. two  delete queries
engine.execute("DELETE FROM Adult WHERE age = {age}".format(age=39))
engine.execute("DELETE FROM Adult WHERE fnlwgt = {fnlwgt}".format(fnlwgt=128392))

# 4. two filter queries
engine.execute("SELECT fnlwgt, education FROM Adult WHERE age = {age}".format(age=50))
engine.execute("SELECT fnlwgt, education FROM Adult WHERE education = '{edu}'".format(edu="Bachelors"))

# 5