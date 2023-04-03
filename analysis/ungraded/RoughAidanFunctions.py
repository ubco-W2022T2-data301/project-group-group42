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
    df_em = pd.read_csv("../data/raw/owid_emissions.csv") #Emissions dataframe
    
    #Read in world dataframe which contains geometry of countries to plot with geopandas
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres')).sort_values(by=["name"]).reset_index()
    world.index = world["name"]
    world.drop(["index","iso_a3"],axis=1,inplace=True)
    
    emissions = df_em.drop(df_em[df_em["year"] < 1960].index)
    #Replace some country names from emissions dataframe to match ones in world df
    emissions.replace({"United States":"United States of America",
                  "Bosnia and Herzegovina": "Bosnia and Herz.",
                  'Democratic Republic of Congo':'Dem. Rep. Congo',
                  "Equatorial Guinea":"Eq. Guinea",
                  'South Sudan':'S. Sudan',
                  'Central African Republic':'Central African Rep.',
                  "Cote d'Ivoire":"Côte d'Ivoire",
                  'Western Sahara':'W. Sahara',
                  'Eswatini':'eSwatini',
                  "Somalia":'Somaliland'}, inplace=True)
    
    #Pivot so each country is a row and each column is the year
    pivot_em = emissions.pivot(index="country",columns=["year"],values=["co2"])
    #Drop any countries from the emissions dataframe that is not in the geopandas dataframe
    pivot_em = pivot_em[pivot_em.index.isin(world["name"].unique().tolist())]
    
    #Appending all the CO2 columns to our world dataset
    for i in range(1960,2014):
        curr = f"{i}_co2"
        world[curr] = pivot_em["co2",i]
        
    temp_df = pd.read_csv("../data/raw/GlobalLandTemperaturesByCountry.csv")
    temp_df["dt"] = (temp_df["dt"].apply(pd.to_datetime)).dt.date #Converts all string dates to to datetime objects (Takes a while)
    temp_df["year"] = [x.year for x in temp_df["dt"]] #Just shows the year
    temp_df = temp_df.groupby([temp_df["year"],temp_df["Country"]])["AverageTemperature"].mean(numeric_only=True).reset_index()#Convertes monthly average temp into annaully
    
    pivoted_tempdf = (temp_df.sort_values(by=["Country","year"])
        .loc[lambda x: x.year > 1959] #Drops rows from before 1960
        .replace({"United States":"United States of America", #Changes a few country names for plotting with geopandas
                     "Congo (Democratic Republic Of The)" : "Dem. Rep. Congo",
                     "Central African Republic":"Central African Rep.",
                     "Côte D'Ivoire":"Côte d'Ivoire",
                     "Czech Republic":"Czechia"}))
    
    pivoted_tempdf = pivoted_tempdf[pivoted_tempdf["Country"].isin(world["name"].unique().tolist())] #Gets rid of any country which is not in world data (basically small island nations)
    pivoted_tempdf = pd.pivot_table(pivoted_tempdf,index="Country",columns="year",values="AverageTemperature").reset_index()
    pivoted_tempdf.index = pivoted_tempdf["Country"]
    
    world = pd.concat((world,pivoted_tempdf),axis=1)
    
    #Delta Temp is the average temp from 1960-1964 subtracted from the average temp of 2009-2013
    world["delta_temp"] = world.iloc[:,109:114].mean(axis=1) - world.iloc[:,60:65].mean(axis=1)
    #TotalCo2 is the amount of co2 emitted from 1960-2013
    world['totalCo2'] = world.iloc[:,5:59].sum(axis=1)
    world["Co2PerPerson(Tonnes)"] = (world.iloc[:,115] / world.iloc[:,0]) * 1000000
    return world