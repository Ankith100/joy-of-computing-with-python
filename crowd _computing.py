#Finding number of Gems in a jar by crowd computing
import random
from statistics import mean
from scipy import stats
a=[]
#taking values of no of gems using randint method in to list a
for i in range(100):
	a.append(random.randint(1,1000))
m=stats.trim_mean(a,0.1) #finding trim mean using method trim_mean methpd
print(m)
a.sort()
tv=int(0.1*len(a))
a=a[tv:len(a)-tv]
print(mean(a)) #trime_mean without using stats.trim_mean