import subprocess
import random
import os

n=10500  # total number of files.
a=0.80   # Parameter for Zipf distribution.


sum=0.0

for i in range(n):
	# clculationg cumulative distribution 
	sum=sum+(1/float((i+1)**a))

cdf=[]
prob=[]


cmd='wget http://content-server-1/test1/'  # directory on content server.
chuser="'http://ran"


for i in range(n):
	prob.append(round((1/(i+1)**a)/sum,6))  # probability for each file
	if i !=0:
		cdf.append(cdf[i-1]+prob[i])      # cumulative distribution
	else:
		cdf.append(prob[i])

x=random.randint(1,1000000)
for j in range(n):
	if j==0:
		if x <= cdf[j]*1000000:     # checking in which file's 
									# probability range does x fall in.
			subprocess.call(cmd+str(j+1), shell=True)
	else:
		if x <= cdf[j]*1000000 and x > cdf[j-1]*1000000:
			subprocess.call(cmd+str(j+1), shell=True)
