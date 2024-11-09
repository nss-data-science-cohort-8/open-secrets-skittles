# An Analysis of Political Contributions During the 2020 House of Representatives Election, Part 2

Now, you'll take the data that you gathered and analyze it, presenting your results at the end.

### Part 2: Exploratory Data Analysis
Using your scraped data, investigates different relationships between candidates and the amount of money they raised. Here are some suggestions to get you started, but feel free to pose you own questions or do additional exploration:  
    a. How often does the candidate who raised more money win a race?  
    b. How often does the candidate who spent more money win a race?  
    c. Does the difference between either money raised or money spent seem to influence the likelihood of a candidate winning a race?  
    d. How often does the incumbent candidate win a race?  
    e. Can you detect any relationship between amount of money raised and the incumbent status of a candidate?

### Part 3: Statistical Modeling
Fit a logistic regression model to see if the amount spent has a statistically significant impact on the probability of winning an election.  
Feel free to brainstorm ways to set up your model, but a suggestion to get started would be to calculate, for each candidate, the percentage of to total amount spent in their race that was spent by them and use this as your predictor variable of interest. Hint: you may find the `transform` method (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html) in combination with `groupby` useful to find the total spending by race.  
Don't forget to include the incumbent variable in your model.  
After fitting your model, interpret the meaning of the coefficients you get.  


## Deliverable

Prepare a 10-12 minute presentation of your findings. This presentation should focus on the exploratory analysis and statistical modeling portions of this project and not on the webscraping components. Thus, you should not include any code in your presenation. Your presentation should be done using PowerPoint/Google Slides or other presentation software.