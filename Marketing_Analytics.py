import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("marketing_data.csv")

# Basic Review
print(df.head())
print(df.info())
print(df.describe())

# Core KPIs
df['CTR'] = (df['Clicks'] / df['Impressions']) * 100
df['CVR'] = (df['Conversions'] / df['Clicks']) * 100
df['CAC'] = df['Cost'] / df['Conversions']
df['ROI'] = ((df['Revenue'] - df['Cost']) / df['Cost']) * 100

# KPI Overview
print(df[['Campaign_ID','Channel','CTR','CVR','CAC','ROI']].head())

# ROI Distribution
sns.boxplot(x='Channel', y='ROI', data=df)
plt.title("ROI by Channel")
plt.show()

# Funnel Drop-Off Visualization
funnel = df[['Impressions','Clicks','Conversions']].sum()
funnel.plot(kind='bar', title="Marketing Funnel Drop-Off")
plt.show()

# Segment Analysis (Age vs ROI)
sns.lineplot(x='Audience_Age', y='ROI', data=df)
plt.title("ROI by Age Group")
plt.show()

# Region Performance Heatmap
pivot_region = df.pivot_table(values='ROI', index='Region', columns='Channel', aggfunc='mean')
sns.heatmap(pivot_region, cmap='viridis', annot=True)
plt.title("ROI Heatmap (Region vs Channel)")
plt.show()

# Correlation
metrics = ['Impressions','Clicks','Conversions','Cost','Revenue','CTR','CVR','CAC','ROI']
sns.heatmap(df[metrics].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap — Marketing Analytics")
plt.show()
