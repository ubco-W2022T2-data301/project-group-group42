import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas

def process_emission_data():
    return pd.read_csv("../data/raw/owid_emissions.csv"#Emissions dataframe
            ).loc[lambda x: x.year >= 1960 #Keep data from 1960 on
            ].loc[lambda x: x.population >= 30000000 # only countries with >30mil people
            ].iloc[:,[0,1,3,4,7,9]] #only columns that we need


def process_temp_dataset():
    temp_df = pd.read_csv("../data/raw/GlobalLandTemperaturesByCountry.csv")
    temp_df["dt"] = (temp_df["dt"].apply(pd.to_datetime)).dt.date #Converts to datetime (Takes a while)
    temp_df["year"] = [x.year for x in temp_df["dt"]] #Just shows the year
    temp_df = temp_df.groupby([temp_df["year"],temp_df["Country"]])["AverageTemperature"].mean(numeric_only=True).reset_index()#Convertes monthly average temp into annaully
               
    pivoted_df = (temp_df.sort_values(by=["Country","year"])
            .loc[lambda x: x.year > 1959] #Drops rows from before 1960
            .replace({"United States":"United States of America", #Changes a few country names for plotting with geopandas
                     "Congo (Democratic Republic Of The)" : "Dem. Rep. Congo",
                     "Central African Republic":"Central African Rep.",
                     "Côte D'Ivoire":"Côte d'Ivoire",
                     "Czech Republic":"Czechia"}))
    
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres')).sort_values(by=["name"]) #loads world dataset from geopandas
    pivoted_df = pivoted_df[pivoted_df["Country"].isin(world["name"].unique().tolist())] #Gets rid of any country which is not in world data (basically small island nations)
    pivoted_df = pivoted_df.pivot(index="Country",columns=["year"],values=["AverageTemperature"]) #pivots so each country is a row and the temperature at each year is the columns
    pivoted_df["delta_temp"] = pivoted_df.iloc[:,53] - pivoted_df.iloc[:,0] #Calculates change in temperature from 1960 to 2013
    
    return temp_df, pivoted_df



def load_and_process():
    