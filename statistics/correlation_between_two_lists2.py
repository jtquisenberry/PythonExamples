from scipy.stats import spearmanr

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

correlation, p_value = spearmanr(list1, list2)

print()
print(list1)
print(list2)
print(f"Spearman correlation coefficient: {correlation}")
print(f"P-value: {p_value}")


list1 = [1, 2, 3, 4, 5]
list2 = [1, 4, 9, 16, 25]

correlation, p_value = spearmanr(list1, list2)

print()
print(list1)
print(list2)
print(f"Spearman correlation coefficient: {correlation}")
print(f"P-value: {p_value}")


list1 = [1, 2, 3, 4, 5]
list2 = [1, 4, 9, 16, 12]

correlation, p_value = spearmanr(list1, list2)

print()
print(list1)
print(list2)
print(f"Spearman correlation coefficient: {correlation}")
print(f"P-value: {p_value}")