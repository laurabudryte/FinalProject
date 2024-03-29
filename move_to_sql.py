import pandas as pd
import psycopg2

df = pd.read_csv('csv_files/SkyScanner_Vilnius_Tokyo_with_indexes.csv')

#Push data to Postgres

connection = psycopg2.connect(database='Skyscanner', host='localhost', user='postgres', password='Ametistas?1')
cursor = connection.cursor()
create_table_query = """
    CREATE TABLE IF NOT EXISTS skyscanner_vilnius_tokyo (
    id SERIAL PRIMARY KEY,
    index_column INT,
    outbound_flight_date DATE,
    return_flight_date DATE,
    price INT,
    outbound_flight_airlines VARCHAR,
    outbound_flight_departure_time VARCHAR,
    outbound_flight_arrival_time VARCHAR,
    outbound_flight_arrival_days INT,
    outbound_flight_duration VARCHAR,
    outbound_flight_stops INT,
    outbound_flight_connecting_airports VARCHAR,
    outbound_flight_departure_airport VARCHAR,
    outbound_flight_arrival_airport VARCHAR,
    return_flight_airlines VARCHAR,
    return_flight_departure_time VARCHAR,
    return_flight_arrival_time VARCHAR,
    return_flight_arrival_days INT,
    return_flight_duration VARCHAR,
    return_flight_stops INT,
    return_flight_connecting_airports VARCHAR,
    return_flight_departure_airport VARCHAR,
    return_flight_arrival_airport VARCHAR,
    outbound_flight_duration_min INT,
    return_flight_duration_min INT
    )
"""
cursor.execute(create_table_query)

insert_query = (
    'INSERT INTO skyscanner_vilnius_tokyo (index_column, outbound_flight_date, return_flight_date, price, outbound_flight_airlines, outbound_flight_departure_time,'
    ' outbound_flight_arrival_time, outbound_flight_arrival_days, outbound_flight_duration, outbound_flight_stops, outbound_flight_connecting_airports,'
    ' outbound_flight_departure_airport, outbound_flight_arrival_airport, return_flight_airlines, return_flight_departure_time,'
    ' return_flight_arrival_time, return_flight_arrival_days, return_flight_duration, return_flight_stops, return_flight_connecting_airports,'
    ' return_flight_departure_airport, return_flight_arrival_airport, outbound_flight_duration_min, return_flight_duration_min)'
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)')

values = df.values

cursor.executemany(insert_query, values)

connection.commit()