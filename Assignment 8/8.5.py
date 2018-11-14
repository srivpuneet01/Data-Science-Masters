# import statements
import numpy as np
import datetime as dt
import pandas as pd
import math
from numpy.random import randn as rn

# initialization
def get_no_of_days_in_the_year(year):
    start_date = dt.datetime(year,1,1).date()
    end_date = dt.datetime(year,12,31).date()
    no_of_days = (end_date - start_date).days + 1
    return no_of_days

def generate_data_frame():
    df = pd.DataFrame() 
    try:
        df = pd.read_pickle("/home/puneet/Data-Science-Masters/Assignment 8/pickle.pickle")
    except FileNotFoundError:
        pass
    if not df.empty:
        return df
    # build date collection
    start_date = dt.datetime(2015,1,1).date()
    dates = [(start_date + dt.timedelta(days = i)).isoformat() for i in range(get_no_of_days_in_the_year(2015)) if not (start_date + dt.timedelta(days = i)).isoweekday() in [6,7]]

    # build random numbers dataframe
    df_random = pd.DataFrame(np.random.randint(100,1000, (len(dates), 1)), columns = ["random_number"])

    # create data frame
    df = pd.DataFrame({"Date": dates})

    # join the series and data frame to build the desired output
    df = df.join(df_random)
    # df.set_index("Date", inplace=True)
    df.to_pickle("/home/puneet/Data-Science-Masters/Assignment 8/pickle.pickle")
    return df

# get the DataFrame
df = generate_data_frame()

# generate a new column named month by splitting date strings at '-' character 
# and picking up the second element from the its output
df["Month"] = df["Date"].apply(lambda x: str(x).split('-')[1])

# now generate a new column "Group_Index" by applying computation on "Month" col. 
# The objective here is to generate the new col in such a way that a group of four 
# consecutive months (starting from the first month) have same value, 
# which will ultimately help in applying groupby function to get the 
# max value from the "random_number" column in each group
df["Group_Index"] = df["Month"].apply(lambda x: math.ceil(int(x)/4))

# compute and print the max value in each group
groupby_Group_Index = df.groupby("Group_Index").agg({'random_number': lambda x: x.max()})
print(groupby_Group_Index)