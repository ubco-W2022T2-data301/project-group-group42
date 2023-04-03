#load import statements
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry_convert as pc


# Here is the cleaned dataset for Natural Disasters from 1970-2021:

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
                      .rename(columns={'Percent_Difference_from_Previous_Year': '% Difference from Previous Year'})
                      .rename(columns={'Difference_from_Previous_Year': 'Difference from Previous Year'})
                      .dropna()
                    )
    return df_ndperyear
              

  


 # This function will get a continent name for corresponding countries:

def get_continent(country):
    try:
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        return "Unknown"

    
    # cleaned and processed emission dataset
def preprocess_emissions_data():
    df_emis = pd.read_csv("../data/raw/owid_emissions.csv")
    df_emis = (df_emis.drop(df_emis[df_emis["year"] < 1970].index)
              .iloc[:, [0, 1, 3, 7, 9]]
              .sort_values(by='year')
              .assign(continent=lambda x: x["country"].apply(get_continent)) #this function was created just above ^
              .query('continent != "Unknown"')
              .dropna()
              .rename(columns={'co2_growth_prct': '% Difference from Previous Year'}))
    return df_emis
preprocess_emissions_data()



def preprocess_temperature_data():
    americas_cont = { #changing so the continents can be the same as the natural disasters dataframe
        'North America': 'Americas',
        'Central America': 'Americas',
        'South America': 'Americas'
    }

    df_temp = pd.read_csv("../data/processed/processedTemperatureData.csv")
    df_temp = (df_temp.drop(df_temp[df_temp["year"] < 1970].index)
                   .assign(Continent=lambda x: x["Country"].apply(get_continent)
                           .replace(americas_cont))  # Include mapping and replacement step
                   .query('Continent != "Unknown"')
                   .drop('Unnamed: 0', axis=1)
                   .assign(temperature_difference=lambda x: x['AverageTemperature'] -
                           x.groupby('Country')['AverageTemperature'].shift(1),
                           pct_temperature_difference=lambda x: x['temperature_difference'] /
                           x['AverageTemperature'] * 100 )
                   .dropna()
                   .rename(columns={'year':'Year'})
                   .rename(columns={'pct_temperature_difference': '% temp difference'}))
               
    return df_temp
preprocess_temperature_data()







             
             