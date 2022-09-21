import pandas as pd

data_file = 'SYB64_176_202110_Tourist-Visitors Arrival and Expenditure.csv'

def ReadDataFrame():
    data_frame = pd.read_csv(data_file, encoding='latin-1')
    columns = data_frame.columns
    sorted_data_frame = data_frame[data_frame[columns[3]] == 'Tourist/visitor arrivals (thousands)'][
        [columns[1], columns[2], columns[6]]]
    columns = sorted_data_frame.columns
    return sorted_data_frame, columns


def NameCountries():
    data_frame, columns = ReadDataFrame()
    countries = []
    last_country = ''
    for country in data_frame[columns[0]]:
        if country != last_country:
            countries.append(country)
            last_country = country
    #name_countr_
    return countries


def SortForCountries(countries):
    data = ReadDataFrame()
    data_frame = data[0]
    years = []
    amount = []
    for i in countries:
    for year in data_frame[data_frame[data[1][0]] == countries][data[1][1]]:
        years.append(int(year))
    for count in data_frame[data_frame[data[1][0]] == countries][data[1][2]]:
        amount.append(int(count.split(',')[0] + count.split(',')[1]))

    return years, amount

