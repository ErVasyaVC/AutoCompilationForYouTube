import pandas as pd
import json

with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    list_of_countries = config['list_of_countries']
    data_file = config['data_file']


def ReadDataFrame():
    data_frame = pd.read_csv(data_file, encoding='latin-1')
    columns = data_frame.columns
    sorted_data_frame = data_frame[data_frame[columns[3]] == 'Tourist/visitor arrivals (thousands)'][
        [columns[1], columns[2], columns[6]]]
    return sorted_data_frame


def NameCountries():
    data_frame = ReadDataFrame()
    columns = data_frame.columns
    countries = []
    last_country = ''
    for country in data_frame[columns[0]]:
        if country != last_country:
            countries.append(country)
            last_country = country
    return countries


def SortForCountries(countries):
    data_frame = ReadDataFrame()
    columns = data_frame.columns
    years_countries = []
    for i in countries:
        years = []
        amount = []
        for year in data_frame[data_frame[columns[0]] == i][columns[1]]:
            years.append(int(year))
        for count in data_frame[data_frame[columns[0]] == i][columns[2]]:
            if "," in count:
                amount.append(int(count.split(',')[0] + count.split(',')[1]))
            else:
                amount.append(int(count))
        years_countries.append([years, amount])
    return years_countries


def MinMaxYears(data):
    min_year = []
    max_year = []
    for country_data in data:
        min_year.append(min(country_data[0]))
        max_year.append(max(country_data[0]))
    return max(min_year), min(max_year)


def SortYears():
    data = SortForCountries(list_of_countries)
    mn_year, mx_year = MinMaxYears(data)
    for num_country in range(len(data)):
        del_num_years = []
        for num_year in range(len(data[num_country][0])):
            if not (mn_year <= data[num_country][0][num_year] <= mx_year):
                del_num_years.append(num_year)
        for i in del_num_years[-1::-1]:
            data[num_country][0].pop(i)
            data[num_country][1].pop(i)
    return data
