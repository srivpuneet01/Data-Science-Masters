# import dependencies
import pandas as pd
import numpy as np

# create the dataframe
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

# Question 1
# replacing NAN values with the preceding values + 10 in FlightNumber Column
for i in range(df.FlightNumber.count() + 1):
    print(df.FlightNumber.loc[i,])
    if pd.isnull(df.FlightNumber.loc[i,]):
        df.loc[i,'FlightNumber'] = df.FlightNumber.loc[i-1,] + 10
        print(df.FlightNumber.loc[i,])

# Question 2 Separation of From_To columns into From and To
df_tmp = df.copy()
df_tmp[['From','To']] = df_tmp.From_To.str.split("_",expand=True)

# Question 3 
# capitalisation of the city names in df_tmp
print(df_tmp)
df_tmp.From = df_tmp.From.str.capitalize()
df_tmp.To = df_tmp.To.str.capitalize()
df_tmp.From_To = df_tmp.From_To.str.capitalize()
print('-'*80)
print(df_tmp)

# Question 4 
# Delete the From_To column from df and attach the temporary DataFrame from the previous questions
print(df)
df.drop('From_To',axis=1,inplace=True)
print('-'*80)
print(df)
df['From_To'] = df_tmp['From_To']
print('-'*80)
print(df)

# Question 5 
rows = []
transformed_df = df.apply(lambda row: [rows.append([row['Airline'], row['FlightNumber'],nn,row['From_To']]) 
                         for nn in row.RecentDelays], axis=1)
df_new = pd.DataFrame(rows, columns=df.columns)
print("Original DataFrame :  \n")
print(df)
print('*'*80)
print("New DataFrame :  \n")
print(df_new)
print("Original DataFrame :  \n")
print(df)
print('*'*80)
print("New DataFrame :  \n")
print(df_new)
df3 = pd.DataFrame(df['RecentDelays'].values.tolist())
length_cols = df3.shape[1]
col_list = []
col_dict ={}
for i in range(length_cols):
    Key = df3.columns[i]
    #print(key,i)
    Value = "Delay" + str(i+1)
    col_dict[Key] = Value
df3.rename(columns=col_dict,inplace=True)
df[["Delay1","Delay2","Delay3"]] = df3[["Delay1","Delay2","Delay3"]]
print(df)
print('*'*80)
df.drop('RecentDelays',axis=1,inplace=True)
print(df)