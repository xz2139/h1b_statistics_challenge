"""
11/01/2018
Xinyue Zhang

This script takes input of h1b statistics file in semicolon separated (";") format, and output two files stating the top 10 Occupations and Top 10 States for certified visa applications.

Details can be found in https://github.com/InsightDataScience/h1b_statistics

"""

import sys

# Parse out system variable
data_file = sys.argv[1]
job_name = sys.argv[2]
state_name = sys.argv[3]

# Read in Data 
data = []
try:
    with open(data_file,encoding="utf-8") as f:
        for line in f:
            data.append(line.split(';'))
except:
    print('Error with Input file')
    sys.exit()
    
# Get column index of the state, job and h1b status
# Note in 2014 data, it has different names
state = data[0].index('WORKSITE_STATE') if 'WORKSITE_STATE' in data[0] else data[0].index('LCA_CASE_WORKLOC1_STATE')  
job = data[0].index('SOC_NAME') if 'SOC_NAME' in data[0] else data[0].index('LCA_CASE_SOC_NAME')  
status = data[0].index('CASE_STATUS')  if 'CASE_STATUS' in data[0] else data[0].index('STATUS')  

# Remove header when processing
data=data[1:]

# Define function for writting top 10 into new file
def top10_certified(data, subject, outputfile):
    
    # Define index for each subject
    if subject=='job':
        index_s=job
    elif subject=='state':
        index_s=state
       
    # Select Data that has h1b status as certified, I used a list version of fancy indexing
    certified=[row[status]=='CERTIFIED' for row in data]
    certified_case=[data[i] for i in range(len(data)) if certified[i]==True]
    
    # Save the total number of certified case for future ussage    
    total_count=len(certified_case)

    # Define a Counter dictionary
    counter={}
    
    # Populate the counter
    for case in certified_case:
        key=case[index_s]
        # Remove " in names
        key=key.strip('"')
        if key in counter:
            counter[key] += 1
        else:
            counter[key] = 1    

    # sort the counter
    # first based on decreasing number of certified case, next based on alphabetic name
    sorted_list = sorted(counter.items(), key=lambda x:(-x[1],x[0]), reverse=False)

    # Get the top 10 occupations/states in each
    # Create a list and populate each by list [occupations/states, number of certified case in each, percent in total]
    output=[]
    for key, value in sorted_list[:10]:
        percent=float(round(value*100/(total_count)))
        output.append([key, str(value),str(percent)+'%'])
    
    # Add headers to the list
    if subject=='job':
        output_whead=[['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE']]+output
    else:
        output_whead=[['TOP_STATES','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE']]+output
    
    # Write it to a semicolon seperated file
    with open(outputfile, 'w') as filehandle:  
        for item in output_whead:
            filehandle.write(";".join(item)+'\n')

# Execute function seperately for Occupations and States
top10_certified(data, subject='job', outputfile=job_name)
top10_certified(data, subject='state', outputfile=state_name)