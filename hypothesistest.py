from scipy.stats import ttest_1samp
import numpy as np
def one_sample_t_test(test_data):
  height = np.array([165,170,160,154,175,155,167,177,158,178])
  print(height)
  height_mean = np.mean(height)
  print('Mean Height = ', height_mean)
  tset, pval = ttest_1samp(height, test_data)
  print('p-values are: ', pval)
  if pval < 0.05: # alpha value is 0.05 or 5%
    result = 'we are rejecting null hypothesis '
  else:
    result = 'we are accepting null hypothesis '
  return result
if __name__ == "__main__":
  test_data = 170
  result = one_sample_t_test(test_data)
  print(result)
