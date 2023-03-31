top_df = top16_countries().groupby('country')['Emissions_per_capita'].mean()
topgd =  top16_countries().groupby('country')['GDP_per_capita'].mean()
top_df = pd.DataFrame(top_df)
topgd = pd.DataFrame(topgd)
df_merged = top_df.merge(topgd, on = 'country')
df_merged
