#задача 1
import pandas as pd
import numpy as np

# из списка
list_data = [10, 20, 30, 40]
series_from_list = pd.Series(list_data)
print("Series from list:")
print(series_from_list)

# из массива
array_data = np.array([50, 60, 70, 80])
series_from_array = pd.Series(array_data)
print("\nSeries from array:")
print(series_from_array)

# из словаря
dict_data = {'a': 100, 'b': 200, 'c': 300}
df_from_dict = pd.DataFrame(dict_data.items(), columns=['key', 'value'])
print("\nDataFrame from dictionary:")
print(df_from_dict)


# получение непересекающихся элементов

s1 = pd.Series(['A', 'B', 'C', 'D'])
s2 = pd.Series(['B', 'E', 'F', 'G'])

non_intersecting_elements = s1.symmetric_difference(s2)
print("\nNon-intersecting elements:")
print(non_intersecting_elements)

# Частота уникальных элементов и построение гистограммы
s = pd.Series([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

freq = s.value_counts()

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(freq.index, freq.values)
plt.xlabel('Unique Elements')
plt.ylabel('Frequency')
plt.title('Histogram of Unique Element Frequencies')
plt.show()

# объединение dataframe
df1 = pd.DataFrame({'col1': ['A', 'B'], 'col2': [1, 2]})
df2 = pd.DataFrame({'col1': ['C', 'D'], 'col2': [3, 4]})

concat_df = pd.concat([df1, df2], ignore_index=True)
print("\nVertically concatenated DataFrame:")
print(concat_df)

df3 = pd.DataFrame({'key': [1, 2], 'val1': [10, 20]})
df4 = pd.DataFrame({'key': [1, 2], 'val2': [30, 40]})


merged_df = pd.merge(df3, df4, on='key')
print("\nHorizontally merged DataFrame:")
print(merged_df)

# построение графика

data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.plot(df['x'], df['y'], marker='o', linestyle='-', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Dependency Plot')
plt.grid(True)
plt.show()

