import pandas as pd
import matplotlib.pyplot as plt

data = {
    'country': ['India', 'China', 'USA', 'Brazil', 'Japan',     'Pakisthan', 'Nigeria', 'Mexico'],

    'population_1952': [732,228, 927, 832, 90, 97, 93, 32],

    'population_2007': [8781,6355,687,467,76,78,73,64]
}

df = pd.DataFrame(data)

print("original Data: ")
print(df)

df['Population_Growth'] = (
    df['population_2007'] - df['population_1952']
)

print("\nPopulation Growth: ")
print(df)

average = df['Population_Growth'].mean()
print("\nAverage Population Growth: ", average)

highest = df['Population_Growth'].max()
print("Highest Population Growth: ", highest)

df = df.sort_values(
    'Population_Growth',
    ascending=False
)

print('\nSorted Data: ')
print(df)

plt.figure(figsize=(12, 6))

plt.bar(
    df["country"],
    df['Population_Growth'],
    width = 0.6
)

plt.ylabel('Countries')
plt.xlabel('Population Growth (Millions)')

plt.title('Population Growth from 1852 to 2007')
plt.xticks(rotation=45)

plt.show()