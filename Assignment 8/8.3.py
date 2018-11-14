# import statements
import numpy as np
import datetime as dt
import pandas as pd
from numpy.random import randn as rn

# initialization
def get_no_of_days_in_the_year(year):
    start_date = dt.datetime(year,1,1).date()
    end_date = dt.datetime(year,12,31).date()
    no_of_days = (end_date - start_date).days + 1
    return no_of_days

def generate_data_frame():
    # build date collection
    start_date = dt.datetime(2015,1,1).date()
    dates = [(start_date + dt.timedelta(days = i)).isoformat() for i in range(get_no_of_days_in_the_year(2015)) if not (start_date + dt.timedelta(days = i)).isoweekday() in [6,7]]

    # build random numbers dataframe
    df_random = pd.DataFrame(np.random.randint(100,1000, (len(dates), 1)), columns = ["random_number"])

    # create data frame
    df = pd.DataFrame({"Date": dates})

    # join the series and data frame to build the desired output
    df = df.join(df_random)
    df.set_index("Date", inplace=True)
    return df



# loop through the data frame to sum all the wednesday values
df = generate_data_frame()
sum = 0
for date in df.index:
    if pd.to_datetime(date).isoweekday() == 3:
        sum += df["random_number"][date]
print(df)
print(df.describe())
print("The sum of the values in data frame for every Wednesday is: " + str(sum))