import pandas as pd

jobs = pd.read_csv('jobs.txt',skiprows=0,delim_whitespace=True,header=0,names=['weight','length'])
jobs['diff'] = jobs['weight']-jobs['length']
jobs['ratio'] = jobs['weight']/jobs['length']
jobs_diff = jobs.sort(['diff','weight'],ascending=[False,False])
jobs_ratio = jobs.sort(['ratio','weight'],ascending=[False,False])
comp_times_diff = []
comp_times_ratio = []
time_sum = 0
for i in range(0,len(jobs)):
	time_sum = time_sum + jobs_diff['length'].iloc[i]
	comp_times_diff.append(time_sum)

time_sum = 0
for i in range(0,len(jobs)):
	time_sum = time_sum + jobs_ratio['length'].iloc[i]
	comp_times_ratio.append(time_sum)

print sum([comp_times_diff[i]*jobs_diff['weight'].iloc[i] for i in range(0,len(jobs))])
print sum([comp_times_ratio[i]*jobs_ratio['weight'].iloc[i] for i in range(0,len(jobs))])

print (7.34*22.66/120 + 0.24*23.76/120 + 0.51*12.49/120 + 1.04*12.04/120 + 1.51*8.49/120 + 4.05*12.05/120 + 0.13*6.87/120 + 0.44*5.6/120 + 0.77*6.77/120 + 0.24*5.24/120 + 4.2*4.2/120)