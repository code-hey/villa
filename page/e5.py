#Hypothesis Testing Using a t-Test
#Aim: To perform an independent two-sample t-test and interpret the p-value at a 5% #significance level.

from scipy.stats import ttest_ind

# Two independent samples
group1 = [70, 75, 80, 85, 90]
group2 = [65, 68, 72, 70, 75]

# Perform independent t-test
t_stat, p_value = ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Reject the null hypothesis")
    print("There is a significant difference.")
else:
    print("Fail to reject the null hypothesis")
    print("There is no significant difference.")