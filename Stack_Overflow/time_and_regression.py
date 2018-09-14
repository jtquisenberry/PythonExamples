import pandas as pd
import sklearn.linear_model as linear_model

delivery_data = {
    'order_time' : ['2018-09-12 21:43:08', '2018-09-13 06:33:04', '2018-09-13 09:12:18'],
    'price' : [34.54, 8.63, 21.24],
    'miles' : [6, 3, 7],
    'home_type' : ['apartment', 'house', 'apartment'],
    'elapsed_time' : [2023, 1610, 1918]
}

df = pd.DataFrame(delivery_data)
df['order_time'] = pd.to_datetime(df['order_time'])

print(df.shape)
print(df.head())
print(df['order_time'])