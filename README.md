# H1b_Statistics_Challenge

This is part of Insight Data Challenge. 

See more in https://github.com/InsightDataScience/h1b_statistics

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years. 

This problem is creating a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications. The code should be modular and reusable for the future. And it is only allowed to use the default data structures.

# Approach

I approach this problem using Python 3. The solution only contain 1 python script named **h1b.py**, and the only package it used is the default `sys` package. 

1. Load data to list of lists. 
2. Parse out header and get the index for h1b status, state and occupations.
3. Create counter using list to count the number of certified case within each occupations/states.
4. Convert the counter into a list and sort by the number of certified case and alphabetic names in decreasing order. 
5. Choose the top 10 in the list and write them into files in desired format.

The last three steps are written into a function called `top10_certified`. The function takes argument of the subject name we want to count. And at the end of script, I called this function 2 times seperately for occupations and states to create output files. 

# Instructions 

To run the script, just put the input file in folder `input`, call `./run.sh` from terminal, and the script will generate output file 
`top_10_occupations.txt` and `top_10_states.txt` in `output` folder.

To test on sample test case, run `./run_tests.sh` from `insight_testsuite` folder.
