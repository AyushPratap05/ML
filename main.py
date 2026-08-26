from scipy import stats

# Binomial test p-value: 10 successes out of 10 trials with p = 0.5
p_value = stats.binomtest(k=10, n=10, p=0.5).pvalue
print(p_value)  # Output: 0.001953125 (two-tailed)