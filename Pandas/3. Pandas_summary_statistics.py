# methods: mean(), groupby(), max(), min(), median(), skew(), describe(), value_counts(), count()
# attributes: 

import pandas as pd

titanic =  pd.read_csv("./z. pandas_titanic_data.csv")
# print(titanic.head())

# Aggregation

print(titanic["Age"].mean())  # average

print(titanic[["Age", "Fare"]].median())

print(titanic[["Age", "Fare"]].describe()) 

print(titanic.agg({
  "Age" : ["min", "max", "median", "skew"],
  "Fare" : ["min", "max", "median", "mean"]             # specific aggregate function to show for specific columns
}))


# Aggregation by Group

print(titanic[["Sex", "Age"]].groupby("Sex").mean())

print(titanic.groupby("Sex").mean(numeric_only=True)) # will be applied on all the columns holding numeric values

print(titanic.groupby("Sex")["Age"].mean())

print(titanic.groupby(["Sex","Pclass"])["Fare"].mean())  # for multiple coulmns , the list of the columns is given to the groupby function

# Number of Records by group/category

print(titanic["Pclass"].value_counts(dropna=True))  # uses the dropna for excluding the null values

print(titanic.groupby("Pclass")["Pclass"].count())  # count by default excludes the NaN values


