import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import sqlite3 as db

# Load data
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data")

# Add column headers
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']

# Create sqladb
sqladb = db.connect('/home/puneet/Data-Science-Masters/Assignment 12/sqladb.db')

#Creating database cursor for further querying the data
cursor = sqladb.cursor()

# Create table and load data
df.to_sql('Adult', sqladb, if_exists='replace', index=False)

# 1. Select 10 records from the adult sqladb
print("1. Select 10 records from the adult sqladb")
query = "SELECT * FROM Adult limit 10"
print(pd.read_sql_query(query,sqladb))

# 2. Show me the average hours per week of all men who are working in private sector
print("\n2. Show me the average hours per week of all men who are working in private sector")
query = "SELECT sex,workclass, hours_per_week AverageHoursPerWeek FROM Adult where sex = 'Male' and workclass = 'Private'  group by sex,workclass"
print(pd.read_sql_query(query, sqladb))

# 3. Show me the frequency table for education, occupation and relationship, separately
print("\n3. Show me the frequency table for education, occupation and relationship, separately")
print("\nFrequency table for education")
query = "SELECT  education, count(education) frequency from Adult group by education order by frequency desc "
print(pd.read_sql_query(query,sqladb))

print("\nFrequency table for occupation")
query = "SELECT  occupation, count(occupation) frequency from Adult group by occupation order by frequency desc "
print(pd.read_sql_query(query,sqladb))

print("\nFrequency table for relationship")
query = "SELECT  relationship, count(relationship) frequency from Adult group by relationship order by frequency desc "
print(pd.read_sql_query(query,sqladb))

# 4. Are there any people who are married, working in private sector and having a masters degree
print("\n4. Are there any people who are married, working in private sector and having a masters degree")
query = """SELECT count(*) as People FROM Adult WHERE "marital_status" like "Married-%" AND workclass="Private" AND education="Masters" """
print(pd.read_sql_query(query,sqladb))

# 5. What is the average, minimum and maximum age group for people working in different sectors
print("\n5. What is the average, minimum and maximum age group for people working in different sectors")
query = """SELECT workclass, avg(age) average, min(age) minimum, max(age) maximum FROM Adult GROUP BY workclass"""
print(pd.read_sql_query(query,sqladb))

# 6. Calculate age distribution by country
print("\n6. Calculate age distribution by country")
query = """SELECT native_country, Round(Round((count(age)*100),5)/Round((select COUNT(age) from Adult),5),5) as "Age Distribution"  FROM Adult group by native_country order by count(age) desc """
print(pd.read_sql_query(query,sqladb))

# 7. Compute a new column as 'Net-Capital-Gain' from the two columns 'capital-gain' and 'capital-loss'
print("\n7. Compute a new column as 'Net-Capital-Gain' from the two columns 'capital-gain' and 'capital-loss'")
query = """SELECT capital_gain as 'capital-gain', capital_loss as 'capital-loss', (capital_gain - capital_loss) as 'Net-Capital-Gain' FROM Adult """
print(pd.read_sql_query(query,sqladb))

sqladb.close()