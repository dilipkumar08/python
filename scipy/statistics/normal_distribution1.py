import scipt.stats as stat
#Normal distribution
#given standard deviation equal to  12
#z score = x - mu / sigma 
sd=12
mean=68


#90 min daily
z=(90-mean)/sd
print(stat.norm.sf(z)*100)

#less than 20 mins

z=(19-mean)/sd
print(stat.norm.cdf(z)*100)

#between 50 - 100
print(stat.norm.cdf((100-mean)/sd)*100 - stat.norm.cdf((50-mean)/sd)*100)
