import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)

def hours_to_min(time):
    time_in_minutes = 0
    for row in time:
        time_element = time.split(' ')

        if len(time_element) == 1:
            time_in_minutes = int(time_element[0].replace('h', ''))*60
        elif len(time_element) == 2:
            time_in_minutes = int(time_element[0].replace('h', ''))*60+(int(time_element[1]))

    return int(time_in_minutes)

df1 = pd.read_csv('csv_files/240503-240510_SkyScanner_Vilnius_Tokyo.csv')
df2 = pd.read_csv('csv_files/240510-240517_SkyScanner_Vilnius_Tokyo.csv')
df3 = pd.read_csv('csv_files/240517-240524_SkyScanner_Vilnius_Tokyo.csv')
df4 = pd.read_csv('csv_files/240524-240531_SkyScanner_Vilnius_Tokyo.csv')

df = pd.concat([df1, df2, df3, df4], ignore_index=True)

df.dropna()
df.drop_duplicates()

df['Outbound Flight Date'] = pd.to_datetime(df['Outbound Flight Date'])
df['Return Flight Date'] = pd.to_datetime(df['Return Flight Date'])
df['Price'] = pd.to_numeric(df['Price'].str.replace(' €', '').str.replace(',', ''))
df['Outbound Flight Departure Time'] = df['Outbound Flight Departure Time'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Arrival Time'] = df['Outbound Flight Arrival Time'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Connecting Airports'] = df['Outbound Flight Connecting Airports'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Departure Airport'] = df['Outbound Flight Departure Airport'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Arrival Airport'] = df['Outbound Flight Arrival Airport'].str.replace("['", "").str.replace("']", "")
df['Return Flight Departure Time'] = df['Return Flight Departure Time'].str.replace("['", "").str.replace("']", "")
df['Return Flight Arrival Time'] = df['Return Flight Arrival Time'].str.replace("['", "").str.replace("']", "")
df['Return Flight Connecting Airports'] = df['Return Flight Connecting Airports'].str.replace("['", "").str.replace("']", "")
df['Return Flight Departure Airport'] = df['Return Flight Departure Airport'].str.replace("['", "").str.replace("']", "")
df['Return Flight Arrival Airport'] = df['Return Flight Arrival Airport'].str.replace("['", "").str.replace("']", "")
df['Outbound Flight Stops'] = pd.to_numeric(df['Outbound Flight Stops'].str.replace(' stops ', '').str.replace(' stop', '').str.replace('s', ''))
df['Return Flight Stops'] = pd.to_numeric(df['Return Flight Stops'].str.replace(' stops ', '').str.replace(' stop', '').str.replace('s', ''))
df['Outbound Flight Duration'] = df['Outbound Flight Duration'].apply(hours_to_min)
df['Return Flight Duration'] = df['Return Flight Duration'].apply(hours_to_min)
df.rename(columns={'Price':'Price, €',
                   'Outbound Flight Duration':'Outbound Flight Duration, min',
                   'Return Flight Duration':'Return Flight Duration, min'},
          inplace=True)

df.to_csv('csv_files/SkyScanner_Vilnius_Tokyo_with_indexes.csv', index=True)