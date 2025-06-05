from scipy.stats import pearsonr

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 5, 4, 5]

correlation, _ = pearsonr(list1, list2)
print(f"Pearson correlation coefficient: {correlation}")