# An Analysis of Political Contributions During the 2020 House of Representatives Election

In this part, you will obtain as much data as you can on the campaign contributions received by each candidate. This data is available through the website https://www.opensecrets.org/.

### Part 1: Data Gathering
1. Start by acquiring the data from Tennessee's 7th District, which is available at https://www.opensecrets.org/races/summary?cycle=2020&id=TN07&spec=N. If you click the "Download .csv file", you can get a csv for this district. However, we don't want to have to click this button across all districts. Instead, we'll use Python to help automate this process. Start by sending a get request to the download button URL, https://www.opensecrets.org/races/summary.csv?cycle=2020&id=TN07. Convert the result to a DataFrame.
2. Once you have working code for Tennessee's 7th District, expand on your code to capture all of Tennessee's districts into a single DataFrame. Make sure that you can distinguish which district each result came from. Export the results to a csv file.
3. Once you have working code for all of Tennessee's districts, expand on it to capture all states and districts. The number of districts for each state can be found at https://en.wikipedia.org/wiki/2020_United_States_House_of_Representatives_elections. You may also find the table of state abbreviations here helpful: https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations. Export a csv file for each state.
4. Finally, combine all of the data you've gathered together into a single DataFrame.