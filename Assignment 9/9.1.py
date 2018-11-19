#import Pandas library
import pandas as pd
def get_data():
	url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'
	df_Baby_Names = pd.read_csv(url)
	return df_Baby_Names

# Question 1
print("Output 1")
df_Baby_Names = get_data()
print(df_Baby_Names.head())
print("\n")
df_Baby_Names.drop(df_Baby_Names.columns[df_Baby_Names.columns.str.contains('unnamed',case = False)],axis = 1,inplace = True)
print(df_Baby_Names.head())
print("-------------\n\n")

# Question 2
print("Output 2")
print(df_Baby_Names.groupby('Gender')['Gender'].count())
print("-------------\n\n")

# Question 3
print("Output 3")
df_name_count = df_Baby_Names.groupby('Name')['Name'].count()
print(df_name_count.sort_values(ascending=False).head())
print("-------------\n\n")

# Question 4
print("Output 4")
median_id = df_Baby_Names.median()['Id']
print(df_Baby_Names[df_Baby_Names['Id'] == median_id]['Name'])
print("\n")
print(df_Baby_Names.groupby('Name')['Name','Count'].median())
print("-------------\n\n")

#Question 5
print("Output 5")
print(df_Baby_Names.groupby(['State','Year','Gender'])['Gender'].count())
print("-------------\n\n")