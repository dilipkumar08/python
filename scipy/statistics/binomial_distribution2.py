import scipy.stats as stat
#none are defective
p=5/100
r=0
n=10
print(stat.binom.pmf(r,n,p)*100)

#exactly one is defective
r=1
print(stat.binom.pmf(r,n,p)*100)

#two or fewer are defective
r=2
print(stat.binom.cdf(r,n,p)*100)

#three or more are defective
r=2
print(stat.binom.sf(r,n,p)*100)
