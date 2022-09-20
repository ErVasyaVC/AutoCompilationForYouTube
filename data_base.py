import pandas as pd


def ReadDataFrame():
    data_frame = pd.read_csv("SYB64_176_202110_Tourist-Visitors Arrival and Expenditure.csv", encoding='latin-1')
    sorted_data_frame = data_frame[data_frame['Unnamed: 3'] == 'Tourist/visitor arrivals (thousands)'][
        ['Tourist/visitor arrivals and tourism expenditure', 'Unnamed: 2', 'Unnamed: 6']]
    return sorted_data_frame


def NameCountries():
    data_frame = ReadDataFrame()
    countries = []
    last_country = ''
    for country in data_frame['Tourist/visitor arrivals and tourism expenditure']:
        if country != last_country:
            countries.append(country)
            last_country = country
    return countries


def F(self):
    1
