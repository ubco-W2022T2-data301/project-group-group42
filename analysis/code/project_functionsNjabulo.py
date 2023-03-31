import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


    
def gdpWrangle():
    df = pd.read_csv("../data/raw/imf-dm-export-20230228.csv", sep = ";", decimal = ',')
    mydf = (df.rename(columns={"GDP per capita, current prices(U.S. dollars per capita)": "Country"})
            .drop(['2024', '2025', '2026', '2027'], axis=1)
            .drop(index=df.index[0])
            .drop(index=df.index[197:]) #Filter all the regions and continents out thus leaving countries only in the data frame
            .query('`1980` != "no data"') #Filter all the countries that have no data for 1980 and 2023
            .query('`2023` != "no data"')
            .assign(renamed_1980=lambda x: x['1980'].str.replace(',', '.')) #Float values can't be read with a comma so I replaced it with a decimal points
            .assign(renamed_2023=lambda x: x['2023'].str.replace(',', '.'))
            .assign(change_in_gdp_per_capita=lambda x: x['renamed_2023'].astype(float) - x['renamed_1980'].astype(float)))
    return mydf
        
def sortGDP():
    
    mydf_sort = gdpWrangle().sort_values(by="change_in_gdp_per_capita",ascending=False).reset_index(drop = True)#Sort the list of countries in descending order by change in gdp per capita
    top15 = mydf_sort.drop(index=mydf_sort.index[16:]) #Take the top 16 countries by change in gdp per capita
    return top15

def top16_countries():
    top15countries = ["Luxembourg", "Ireland", "Singapore", "Switzerland", "Norway", "New Zealand", "Iceland", "Qatar", "Australia", "Denmark", "Israel", "Canada", "Hong Kong", "Netherlands", "Sweden", "United States"]
    mydf16 = (pd.read_csv("../data/raw/owid_emissions.csv")
              .query('year >= 1980')
              .iloc[:, [0, 1, 3, 4, 7, 9]]
              .reset_index(drop=True)
              .query('country in @top15countries')
              .assign(Emissions_per_capita=lambda x: x['co2'] * 1000000 / x['population'])
              .reset_index(drop=True))

    return mydf16
 
def country_emis():
    mydf = (pd.read_csv("../data/raw/owid_emissions.csv")
              .query('year == 2020')
              .iloc[:, [0, 1, 3, 4, 7, 9]]
              .reset_index(drop=True)
              .assign(Emissions_per_capita=lambda x: x['co2'] * 1000000 / x['population'])
              .assign(GDP_per_capita = lambda x: x['gdp']/x['population'])
              .reset_index(drop=True))

    return mydf