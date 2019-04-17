import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': np.random.randint(0, 50, 100)})
df['b'] = df['a'] + np.random.normal(0, 10, 100)
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 100)
df['d'] = np.random.randint(0, 50, 100)

pearson_coeffs = np.corrcoef(df['a'], df['b'])
slope, intercept = np.polyfit(df['a'], df['b'], 1)
abline_values_1 = [slope * x + intercept for x in df['a']]
print(pearson_coeffs)
# f1 = plt.figure(1)
plt.scatter(df['a'], df['b'])
plt.plot(df['a'], abline_values_1, 'b')
# plt.show()


pearson_coeffs = np.corrcoef(df['a'], df['c'])
slope, intercept = np.polyfit(df['a'], df['c'], 1)
abline_values_2 = [slope * x + intercept for x in df['a']]
print(pearson_coeffs)
# f2 = plt.figure(2)
plt.scatter(df['a'], df['c'])
plt.plot(df['a'], abline_values_2, 'b')
# plt.show()


pearson_coeffs = np.corrcoef(df['a'], df['d'])
slope, intercept = np.polyfit(df['a'], df['d'], 1)
abline_values_3 = [slope * x + intercept for x in df['a']]
print(pearson_coeffs)
# f3 = plt.figure(3)
plt.scatter(df['a'], df['d'])
plt.plot(df['a'], abline_values_3, 'b')
plt.show()
