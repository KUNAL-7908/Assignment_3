import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, wilcoxon, ttest_ind, ranksums

np.random.seed(42)
dataset = pd.DataFrame(np.random.uniform(5, 11, size=(500, 5)), columns=[f'col{i}' for i in range(1, 6)])

# i)
t_test_results = {}
for col in dataset.columns:
    t_stat, p_value = ttest_1samp(dataset[col], 7.5)  # Assuming a population mean of 7.5 for testing.
    t_test_results[col] = {'t-statistic': t_stat, 'p-value': p_value}

# ii)
wilcoxon_results = {}
for col in dataset.columns:
    statistic, p_value = wilcoxon(dataset[col] - 7.5)  # Assuming a population median of 7.5 for testing.
    wilcoxon_results[col] = {'statistic': statistic, 'p-value': p_value}

# iii)
col3 = dataset['col3']
col4 = dataset['col4']
two_sample_t_test = ttest_ind(col3, col4)
wilcoxon_ranksums_test = ranksums(col3, col4)

print("Results of T-Test:")
for col, results in t_test_results.items():
    print(f"Column {col}: t-statistic={results['t-statistic']}, p-value={results['p-value']}")

print("\nResults of Wilcoxon Signed Rank Test :")
for col, results in wilcoxon_results.items():
    print(f"Column {col}: statistic={results['statistic']}, p-value={results['p-value']}")

print("\nColumn 3 and Column 4 Two Sample T-Test Results:")
print(f"t-statistic={two_sample_t_test.statistic}, p-value={two_sample_t_test.pvalue}")

print("\nWilcoxon Rank Sum Test Results for Column 3 and Column 4:")
print(f"statistic={wilcoxon_ranksums_test.statistic}, p-value={wilcoxon_ranksums_test.pvalue}")