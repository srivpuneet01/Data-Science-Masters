# import statements
import datetime as dt
import pandas as pd
from numpy.random import randn as rn

# initialization
start_date = dt.datetime(2015,1,1).date()
end_date = dt.datetime(2015,12,31).date()
no_of_days = (end_date - start_date).days + 1

# build date collection
dates = [(start_date + dt.timedelta(days = i)).isoformat() for i in range(no_of_days) if not (start_date + dt.timedelta(days = i)).isoweekday() in [6,7]]

# build random numbers series
randoms = rn(len(dates))
random_series = pd.Series(randoms, name = "random_number")


# create data frame
df = pd.DataFrame({"Date": dates})

# join the series and data frame to build the desired output
df = df.join(random_series)
df.set_index("Date", inplace=True)
print(df)