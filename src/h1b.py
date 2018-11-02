import sys

file = sys.argv[1]
job_name = sys.argv[2]
state_name = sys.argv[3]
data = []
with open(file,encoding="utf8") as f:
    for line in f:
#         words = line.split(';')
        data.append(line.split(';'))
    
state = data[0].index('WORKSITE_STATE') if 'WORKSITE_STATE' in data[0] else data[0].index('LCA_CASE_WORKLOC1_STATE')  #get the index for State
job = data[0].index('SOC_NAME')   if 'SOC_NAME' in data[0] else data[0].index('LCA_CASE_SOC_NAME')  
status = data[0].index('CASE_STATUS')  if 'CASE_STATUS' in data[0] else data[0].index('STATUS')  #g

def getfile(cat):
    if cat=='job':
        index_cat=job
    elif cat=='state':
        index_cat=state
    result = {}
    for i in range(1,len(data)):
        if data[i][status] == 'CERTIFIED':         #only count if the case is certified
            key = data[i][index_cat].strip('" ')        #remove " in the str
            if key in result:
                result[key] += 1
            else:
                result[key] = 1

    result1=result.copy()
    total=sum(result1.values())
    for key, value in result.items():
        result[key] = float(round(value*100/(total)))

    temp1 = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    # temp2 = dict(sorted(temp1.items(), key=lambda x: x[1], reverse=True))

    output=[]
    for key, value in temp1.items():
        output.append([key, str(result1[key]),str(value)+'%'])
    dic=[['TOP_OCCUPATIONS','NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE']]+output[:10]
    if cat=='job':
        field='occupations'
    else:
        field='states'
    outputfile='top_10_'+field+'.txt'
    with open(outputfile, 'w') as filehandle:  
        for item in dic:
            filehandle.write(";".join(item)+'\n')
getfile('job')
getfile('state')