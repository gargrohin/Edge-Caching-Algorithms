import subprocess
#import matplotlib.pyplot as plt
import random
import os

n=10500
a=0.78
sum=0.0
#get=[]
for i in range(n):
	sum=sum+(1/float((i+1)**a))
	#get.append(0)
cdf=[]
prob=[]
cmd='wget http://content-server-1/test1/'
chuser="'http://ran"
for i in range(n):
	prob.append(round((1/(i+1)**a)/sum,6))
	if i !=0:
		cdf.append(cdf[i-1]+prob[i])
	else:
		cdf.append(prob[i])
for i in range(int(1)):
	for u in range(6):
		if u==0 or u==1:
			r="1"
		if u==2 or u==3:
			r="2"
		if u==4 or u==5:
			r="3"
		chu=chuser+r+":3128/'"
		os.environ['http_proxy']=chu
		x=random.randint(1,1000000)
		for j in range(n):
			if j==0:
				if x <= cdf[j]*1000000:
					subprocess.call(cmd+str(j+1), shell=True)
			else:
				if x <= cdf[j]*1000000 and x > cdf[j-1]*1000000:
					subprocess.call(cmd+str(j+1), shell=True)
