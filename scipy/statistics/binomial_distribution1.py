import scipy.stats as stat 
p,r,n=4/10,20,50
print(stat.binom.pmf(r,n,p)*100)
