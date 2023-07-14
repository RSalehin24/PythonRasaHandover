# attibutes: dtypes, shape
# methods: info(), head(), tail(), describe(), notna(), loc(), iloc()

import pandas as pd

df = pd.DataFrame({
  "Name":
    [
      "Braund, Mr. Owen Harris",
      "Allen, Mr. William Henry",
      "Bonnell, Miss. Elizabeth",
    ],
  "Age": [22, 35, 58],
  "Sex": ["male", "male", "female"],
})

print(df)
print(df["Age"])   # a single column in the df is called a series
print(type(df["Age"])) # datatype of a single column of a df
print(df["Age"].max())   # works with df or series
print(df.max()) # max() is called a method() [which is a function]


# loading data into df

titanic =  pd.read_csv("./z. pandas_titanic_data.csv")

titanic.to_excel("z. titanic.xlsx", sheet_name="passengers", index=False)

titanic = pd.read_excel("./titanic.xlsx")


# overview of the dataframe

print(titanic)

print(titanic.head(10))

print(titanic.tail(10))


# info and statictics of the dataframe

print(titanic.dtypes) # data types of all columns : objects are string here : dtype is an attibute of series or df

print(df.describe())  # only shows the numerical statistics of the columns which are holding numerical values

print(titanic.info())  #gives you a summary of the df


# selecting a sub-section of the dataframe

ages = titanic["Age"]

print(ages.head())

print(type(ages)) # each column of a df is a series

print(ages.shape)

age_sex = titanic[["Age", "Sex"]]

print(age_sex.head())

print(type(age_sex))

print(age_sex.shape)


# filter specific rows from all the rows

above_35 = titanic[titanic["Age"] > 35]   # for selecting rows based on condition, the condition is used inside the selection brackets

print(above_35.head())   

print(above_35.shape)

print(titanic["Age"] > 35)

print(titanic["Pclass"].isin([2,3])) # isin() matches values with the rows and returns true if matched. [] is used to pass multiple values as a list to the function. 
                                     # Works like or operator. 
                                     
print(((titanic["Pclass"] == 2) | (titanic["Pclass"] == 3))) # while using multiple conditions, each condition must be surrounded by the (). and,&    or,|  : logical operation symbols or keywords


# filtering out the NaN values

age_no_na = titanic[titanic["Age"].notna()]

print(age_no_na.head())  # returns True if value is not NaN

print(age_no_na.shape)

# selecting rows and columns based on specific condition

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]  # Selecting name of the persons who are older than 18
                                                        # while using loc/iloc methods, the part before the comma is rows, after the comma is columns

print(adult_names)

print(titanic.iloc[9:25, 2:5])  # iloc or index location: when we want to select rows and columns based on their location or index in the df

titanic.iloc[0:3, 3] = "anonymous"  # loc/iloc can be used for assigning values: assigning name "anonymous" to the first three people

print(titanic.head()) 
