import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
print(df.head(2))
df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv') 
print(df1.head())

# 1. Get the Metadata from the above files.

print("\n\n1. Get the Metadata from the above files.\n\nMetadata - df")
print(df.info())
print("\nMetadata - df1")
print(df1.info())

# 2. Get the row names from the above files
print("\n\n2. Get the row names from the above files\n\nrow names - df")
print(df.index.values)
print("\nrow names - df1")
print(df1.index.values)

# 3. Change the column name from any of the above file.
print("\n\n3. Change the column name from any of the above file.")
print(df.rename(columns={'Indicator':'Indicator_id'}).head())

# 4. Change the column name from any of the above file and store the changes made permanently.
print("\n\n4. Change the column name from any of the above file and store the changes made permanently.")
df.rename(columns={'Indicator':'Indicator_id'},inplace=True)
print(df.head())

# 5. Change the names of multiple columns.
print("\n\n5. Change the names of multiple columns.")
df.rename(columns={"PUBLISH STATES":"Publication Status","WHO region":"WHO Region"},inplace=True)
print(df.head())

# 6. Arrange values of a particular column in ascending order.
print("\n\n6. Arrange values of a particular column in ascending order.")
print(df.sort_values('Year',ascending=True).head())

# 7. Arrange multiple column values in ascending order.
print("\n\n7. Arrange multiple column values in ascending order.")
df_andorra = df[df['Country'] =='Andorra']
#only keep the columns specified in the list
df_andorra = df_andorra[['Indicator_id','Country','Year','WHO Region','Publication Status']]
#sort the columns Indicator_id in descending order and the column Year in ascending order. Also drop the duplicate  rows
df_andorra = df_andorra.sort_values(['Indicator_id','Country','Year','WHO Region'],ascending=[False,False,True,False]).drop_duplicates(keep="first")

#reset the indexes after sorting as the index values will have row numbers of the original dataframe df
df_andorra =df_andorra.reset_index(drop=True)

# display first five ros of the sorted dataframe 
print(df_andorra.head())

# 8. Make country as the first column of the dataframe.
print("\n\n8. Make country as the first column of the dataframe.")
print(df[pd.unique(['Country']+ df.columns.values.tolist()).tolist()])

# 9. Get the column array using a variable
print("\n\n9. Get the column array using a variable")
print(df['WHO Region'].values)

# 10. Get the subset rows 11, 24, 37
print("\n\n10. Get the subset rows 11, 24, 37")
print(df.iloc[[11,24,37]])

# 11. Get the subset rows excluding 5, 12, 23, and 56
print("\n\n11. Get the subset rows excluding 5, 12, 23, and 56")
badindex = df.index.isin([5,12,23,56])
print(df[~badindex].head())


# Load datasets from CSV
print("\n\n")
users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv' )
products = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv' )
transactions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

print(users.head())
print("\n")
print(sessions.head())
print("\n")
print(transactions.head())

# 12. Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)
print("\n\n12. Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)")
print(pd.merge(transactions, users, how="left",on="UserID"))

# 13. Which transactions have a UserID not in users?
print("\n\n13. Which transactions have a UserID not in users?")
print(transactions[~transactions["UserID"].isin(users['UserID'])])

# 14. Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)
print("\n\n14. Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)")
print(pd.merge(transactions, users, how="inner",on="UserID"))

# 15. Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join)
print("\n\n15. Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join")
print(pd.merge(transactions, users, how="outer",on="UserID"))

# 16. Determine which sessions occurred on the same day each user registered
print("\n\n16. Determine which sessions occurred on the same day each user registered")
print(pd.merge(users,sessions,how='inner',left_on=['UserID','Registered'],right_on=['UserID','SessionDate']))

# 17. Build a dataset with every possible (UserID, ProductID) pair (cross join)
print("\n\n17. Build a dataset with every possible (UserID, ProductID) pair (cross join)")
userdf = pd.DataFrame({"UserID":users["UserID"]})
transdf = pd.DataFrame({"ProductID":products["ProductID"]})
userdf['Key'] = 1
transdf['Key'] = 1
df_out = pd.merge(userdf,transdf,how='outer',on="Key")[['UserID','ProductID']]
print(df_out.head())

# 18. Determine how much quantity of each product was purchased by each user
print("\n\n18. Determine how much quantity of each product was purchased by each user")
df_user_prod_quant = pd.merge(df_out,transactions,how='left',on=['UserID','ProductID'])
df_user_quantity = df_user_prod_quant.groupby(['UserID','ProductID'])['Quantity'].sum()
print(df_user_quantity.reset_index().fillna(0))

# 19. For each user, get each possible pair of pair transactions (TransactionID1, TransacationID2)
print("\n\n19. For each user, get each possible pair of pair transactions (TransactionID1, TransacationID2)")
print(pd.merge(transactions,transactions,how='outer',on='UserID'))

# 20. Join each user to his/her first occuring transaction in the transactions table
print("\n\n20. Join each user to his/her first occuring transaction in the transactions table")
df_usertran = pd.merge(users,transactions,how='left',on='UserID')
data = df_usertran.drop_duplicates(subset='UserID')
data = data.reset_index(drop=True)
print(data)

# 21. Test to see if we can drop columns
print("\n\n21. Test to see if we can drop columns")
my_columns = list(data.columns) 
print(my_columns)
print(list(data.dropna(thresh=int(data.shape[0] * .9), axis=1).columns))
missing_info = list(data.columns[data.isnull().any()])
print(missing_info)
for col in missing_info:
    num_missing = data[data[col].isnull() == True].shape[0]
    print('number missing for column {}: {}'.format(col, num_missing))

for col in missing_info:
    num_missing = data[data[col].isnull() == True].shape[0]
    print('number missing for column {}: {}'.format(col, num_missing))
    
for col in missing_info:
    percent_missing = data[data[col].isnull() == True].shape[0] / data.shape[0]
    print('percent missing for column {}: {}'.format(col, percent_missing))