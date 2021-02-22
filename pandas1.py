import pandas as pd
df = pd.DataFrame({
    'weight': [70, 80, 90, 82, 91],
    'height': [170, 181, 185, 168, 180]
})

total_weight = df['weight'].sum()
print(total_weight)

mean_height = df['height'].mean()
print(mean_height)

print(df.describe())

corr = df.corr()

print(corr)