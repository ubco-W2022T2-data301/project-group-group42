# Final report - Emissions Impossible (Group 42)

Climate change is one of the most pressing issues of our time, with far-reaching impacts on the environment, society, and the economy. Our Data Science project seeks to analyze and understand the complex dynamics of climate change in a manner that is both easy to understand and interesting to the average person. By utilizing the method of Exploratory Data Analysis to a diverse range of environmental and economic datasets, we hope to uncover insights that can inform policymakers, businesses, and individuals in their efforts to mitigate and adapt to the effects of climate change. This project is important because it seeks to provide data-driven insights into one of the most critical challenges of our time, and can help us make more informed decisions about how to tackle this issue.

Aidan's Research Question:

There is little doubt among scientists that the rapid rise in global temperature has been a direct result of civilization's carbon footprint. However, this research question wants to explore how much carbon emissions affect temperature on a local scale. In other words, I want to look for evidence that a country which produces large quantities of CO2 (such as the US or China) has had a higher spike in temperature than countries that produce less CO2 (Sub-Saharan Africa or South America).

In order to do this, a dataset which contained the average annual temperature for every country in the world and another dataset displaying CO2 emissions for every country were combined. Data from the year 1960-2013 was used for this research. The use of the geopandas library allowed for the quick plotting of beautiful global heat maps, which was used to plot the change in annual temperature between the average of 1960-1964 and 2009-2013. It is of note that every single country in the world had some sort of increase, albeit some more than others. 

![](images/TempPlot_Aidan.PNG "World heatmap displaying the change in temperature from 1960-2013 for every country")

While no clear pattern was easily drawn, some clusters of larger change could be identified. This led to the creation of a ridgeline plot which showed the change in temperature grouped by continent. The KDE plots gave a rough indication that the Afro-Eurasian landmass heated an entire degree more than the Americas and Oceania. This does provide evidence that there is some kind of locality about climate change, although the geopandas map of total CO2 emission from 1960-2013 did not reflect the same pattern

![](images/Ridgeline_Aidan.PNG "RidgeLine plot displaying the distribution of change in temperature grouped by continent")

To finally answer the research question definitively, a scatterplot of change in temperature and total CO2 emissions was made where each country was a dot. Since some countries have magnitudes smaller population and landmass, a log scale was used for CO2 emissions. The resulting plot looked just about like random dots. Calculating the correlation between the two variables gave a slight positive relationship although some statistical calculations showed that it was not enough to provide statistically significant evidence of a relationship.

![](images/ScatterPlot_Aidan.PNG "Scatterplot showing the relationship between a country's change in temperature and total CO2 emissions")

This exploratory data analysis did not provide any evidence that a country's CO2 output is directly tied to their change in temperature. This means that climate change is a problem that must be solved as a global civilization, and one country’s reduction in their carbon footprint will not provide results without the whole world following suit.


Rona's Research Question:

Rumo's Research Question:

Lastly, the research question of this report entails investigating whether or not a country's economic success dependent on having a heavily industrialized economy with high emissions or can countries find a balance between being economically and environmentally prosperous? Specifically, this report investigates which countries experienced the highest growth in GDP per capita since 1980 and whether they were able to maintain low emissions while achieving economic prosperity. This allows for further analysis of the economies of these countries to determine if they could become the standard with which countries should aspire to follow. 

A quadrant plot was made with GDP and Emissions per capita being the two variables of interest. The four zones were labelled as follows:
- Group I: Countries with a low gdp per capita and low emissions per capita.
- Group II: Countries with a relatively low gdp capita and a high emissions per capita.
- Group III: Countries with a relatively high emissions per capita and a high gdp per capita.
- Group IV: Countries with a relatively low emissions per capita and a high gdp per capita.
![](ungraded/Quadrant_plot.png "Quadrant plot displaying the relationship between a country's GDP and Emissions per capita.")

The plot shows that majority of countries follows an expected relationship with majority of the countries either residing in groups I or III. However, it was decided that for a country to be both economically and environmentally prosperous it would need to have a GDP per capita greater than $20,000 per capita and an Emissions per capita less than 12 metric tons per capita. Thus, the focus of analysis would centre around Group IV.

![](ungraded/bar_plot.png "Bar plot displaying the top 16 countries in terms of change in GDP per capita from 1980-2023")
A bar chart was then created that had the top sixteen countries in terms of change in GDP per capita since 1980 with countries such as Luxembourg, Ireland and Singapore ranking in the top three of those countries. From then on the search was then further filtered to find which of these 16 countries have consistently had the lowest emissions per capita which were Iceland, Ireland and Canada.
![](ungraded/Violin_plot.png)
Based on the violin plot, of the three countries, Canada had a siginificantly larger emissions per capita and was thus disregarded when investigating the economies of the countries. Ireland is an Ireland nation of 5 million people. Despite being a developed nation is able to to thrive without being overly reliant on an industrial sector due to its hand in argiculture and tourism. Moreover, Iceland is an even smaller island nation of approximately 400,000 people. Interestingly, Iceland is in a position where their economic success is in large part due to its use of its natural resources. Iceland is the world's largest electricity provider per capita with 99% of its energy coming from its abundance of hydroelectric dams and geothermal power sources. Thus, suggesting that although circumstances such as population size and natural resources likely play a role in a country's ability to be both environmentally and economically prosperous, it is possible to achieve that balance and thus the onus is on the governments of countries to find a way to achieve this balance. 

It is easy to be apathetic as we are fortunately live in a country that is yet to face the worst of what climate change has to offer, thus it is moWith the ever-present threat of climate change looming over society with its exhaustive list of negative effects on the planet
