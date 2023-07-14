# methods: rename()


import pandas as pd

air_quality = pd.read_csv("z. pandas_air_quality.csv")
# air_quality.head()

# print(air_quality.head())

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

air_quality["ratio_paris_antwerp"] = (
  air_quality["station_paris"] / air_quality["station_antwerp"]    # creating a new column
)

print(air_quality.head())

air_quality_renamed = air_quality.rename(
  columns={
    "station_antwerp" : "BETR801",
    "station_paris" : "FR04014",
    "station_london" : "London Westminister"       # renaming columns, can also be used to rename the rows
})    

# print(air_quality_renamed.head())

air_quality_renamed = air_quality_renamed.rename(columns=str.lower)   # mapping dunction can alse be used

print(air_quality_renamed.head())