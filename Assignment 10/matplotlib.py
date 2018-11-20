import pandas as pd
url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic = pd.read_csv(url)

#1. Create a pie chart presenting the male/female proportion
labels = ['male','female']
sizes = titanic.sex.value_counts()
#print(labels[0],sizes[0])
#print(labels[1],sizes[1])
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
plt.show()

#2 Scatter plot of fare paid and age
plt.figure(figsize=(11,8))
ax = titanic[titanic.sex == 'female'].plot.scatter('age', 'fare', color='blue',label='female')
titanic[titanic.sex == 'male'].plot.scatter('age', 'fare', ax=ax, color='orange',label='male')