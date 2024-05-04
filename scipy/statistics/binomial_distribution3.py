import scipy.stats as stat
#exactly three

p=25/100
r=3
n=20
print(stat.binom.pmf(r,n,p)*100)

#atleast 3
r=2
print(stat.binom.sf(r,n,p)*100)

#atmost 3
r=3
print(stat.binom.cdf(r,n,p)*100)

# 3 to 5
print(sum(stat.binom.pmf(i,n,p)*100 for i in range(3,6)))

print(stat.binom.cdf(5,n,p)*100 - stat.binom.cdf(2,n,p)*100)
