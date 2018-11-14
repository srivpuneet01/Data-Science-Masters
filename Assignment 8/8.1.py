# import pandas
import pandas as pd
# generate the data frame
arr = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
dictionary = {'X': arr}
df = pd.DataFrame(dictionary)
computed_col = []
index = -1
for i in range(len(df.X)):
    if df.X[i] == 0: 
        index = i
    if index == -1:
        computed_col.append(i+1)
    else:
        computed_col.append(i - index)

series = pd.Series(computed_col, name = 'Y')
df = df.join(series, how = 'right') # "how" attribute doesn't have any affect here. why??
print(df)
