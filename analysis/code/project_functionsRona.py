#load import statements
import pandas as pd
import matplotlib.plyplot as plt
import seaborn as sns



#starting the following will be for the Natural Disasters Data
# Here is the cleaned dataset for Natural Disasters from 1970-2021
def processed_nd_data():
    dfclean = (pd.read_csv("../data/raw/1900_2021_DISASTERS.csv")
           .query('`Disaster Type` in ["Flood", "Storm", "Drought", "Wildfire", "Landslide"]')
           .iloc[:, [1, 5, 6, 10, 12, 13]]
           .dropna()
          )
    return dfclean 

# These next two are rather similar; they will display the number of natural disasters per year including both the number and percentage of increase or decrease in events. This first one groups the data by Continent where the second one does not 

def processed_nd_data():
    df_ndperyear = (pd.read_csv("../data/raw/1900_2021_DISASTERS.csv")
                      .query('`Disaster Type` in ["Flood", "Storm", "Drought", "Wildfire", "Landslide"]')
                      .iloc[:, [1, 5, 6, 10, 12, 13]]
                      .dropna()
                      .groupby(['Year', 'Continent', 'Disaster Type'])
                      .size()
                      .reset_index(name='Number of Disasters')
                      .assign(Difference_from_Previous_Year=lambda x: x.groupby('Disaster Type')['Number of Disasters'].diff(),
                              Percent_Difference_from_Previous_Year=lambda x: (x['Difference_from_Previous_Year'] / x.groupby('Disaster Type')['Number of Disasters'].shift(1)) * 100)
                    )
    return df_ndperyear
processed_nd_data()
              
  

 def num_nd_yearly():
    df_ndperyear = (dfclean.groupby(['Year', 'Disaster Type'])
                .size()
                .reset_index(name='Number of Disasters')
                .assign(Difference_from_Previous_Year=lambda x: x.groupby('Disaster Type')['Number of Disasters'].diff(),
                        Percent_Difference_from_Previous_Year=lambda x: (x['Difference_from_Previous_Year'] / x.groupby('Disaster Type')['Number of Disasters'].shift(1)) * 100)
                   )
    return df_ndperyear

#The following will be for the Emissions Data:

def processed_emi_data():
    data_em = (pd.read_csv("../data/raw/owid_emissions.csv")
                .query('year >= 1970')
                .iloc[:, [0, 1, 3, 7, 9]]
                .dropna()
                )
    return df_em      
             
             
TEST

def processed_nd_data():
    df_ndperyear = (pd.read_csv("../data/raw/1900_2021_DISASTERS.csv")
                      .query('`Disaster Type` in ["Flood", "Storm", "Drought", "Wildfire", "Landslide"]')
                      .iloc[:, [1, 5, 6, 10, 12, 13]]
                      .dropna()
                      .groupby(['Year', 'Continent', 'Disaster Type'])
                      .size()
                      .reset_index(name='Number of Disasters')
                      .assign(Difference_from_Previous_Year=lambda x: x.groupby('Disaster Type')['Number of Disasters'].diff(),
                              Percent_Difference_from_Previous_Year=lambda x: (x['Difference_from_Previous_Year'] / x.groupby('Disaster Type')['Number of Disasters'].shift(1)) * 100)
                    )
    return df_ndperyear
processed_nd_data()


             
             
             
             
             