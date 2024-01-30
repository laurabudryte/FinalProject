import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo_with_indexes.csv')


# Vilnius-Tokyo-Vilnius Flight Prices vs Time and Predicted Prices

# df['Overall Time'] = df['Outbound Flight Duration, min']+df['Return Flight Duration, min']
# print(df['Overall Time'])
#
# X = df[['Overall Time']]
# y = df[['Price, €']]
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# model = LinearRegression()
# model.fit(X_train, y_train)
# # y_pred = model.predict(X_test)
# X_range = pd.DataFrame({'Overall Time': range(int(min(X['Overall Time'])), int(max(X['Overall Time']))+1)})
# y_predicted = model.predict(X_range)
#
# plt.figure(figsize=(10,6))
# plt.scatter(df['Overall Time'], df['Price, €'], color='darkseagreen', label='Actual Data')
# plt.plot(X_range, y_predicted, color='crimson', label='Predicted Prices')
# plt.xlabel('Flight time in mins')
# plt.ylabel('Price in €')
# plt.title('Vilnius-Tokyo-Vilnius Flight Prices vs Time and Predicted Prices')
# plt.legend()
# plt.show()


# Average prices by dates

# df['Flight_dates'] = df['Outbound Flight Date'].str[-2:]+'-'+df['Return Flight Date'].str[-2:]
# mean_price_df = df.groupby('Flight_dates')['Price, €'].mean()
# mean_price_df.plot(kind='bar')
# plt.title('Prices average by dates')
# plt.xlabel('Flight dates')
# plt.ylabel('Average price, €')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()


# Prices per airline

# filtered_df = df[df['Outbound Flight Airlines'] == df['Return Flight Airlines']]
# mean_price_df = filtered_df.groupby('Outbound Flight Airlines')['Price, €'].mean().reset_index()
# sorted_mean_price_df = mean_price_df.sort_values('Price, €', ascending=False)
# plt.figure(figsize=(12, 8))
# sns.barplot(data=sorted_mean_price_df, x='Outbound Flight Airlines', y='Price, €', palette='viridis')
# plt.title('Average Price by Airlines')
# plt.ylabel('Average Price in EUR')
# plt.xticks(rotation=30)
# plt.grid(True)
# plt.show()


# Prices & departure time correlation

df2 = df.sort_values('Outbound Flight Departure Time', ascending=True)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Outbound Flight Departure Time', y='Price, €', data=df2)
plt.title('Prices & departure time correlation')
plt.xlabel('Outbound Flight Departure Time')
plt.ylabel('Price, €')
plt.xticks(rotation=40)
plt.grid(True)
plt.show()


# df['Flight Dates'] = df['Outbound Flight Date'].str[-2:]+'-'+df['Return Flight Date'].str[-2:]
# min_price_indexes = df.groupby(['Flight Dates'])['Price, €'].idxmin()
# min_price_per_date_df = df.loc[min_price_indexes, ['Flight Dates', 'Outbound Flight Airlines', 'Return Flight Airlines', 'Price, €']]
# print(min_price_per_date_df)


