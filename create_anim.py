import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import data_base
from celluloid import Camera
import json


def SetSetting(year, i):
    plt.title(label=year, loc='right', fontsize=20, fontweight='bold', pad=10)
    plt.axis([0, 50000, 0.5, 5.5])





with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    fps = config['fps']
    seconds = config['seconds']

time_shot = round(1 / fps, 3)

data = data_base.SortYears()

min_year, max_year = data[0][0][0], data[0][0][-1]
passed_years = 0
float_year = 0
speed_year = (max_year - min_year) / (fps * seconds)
speed_amount = []

last_year = [0 for i in range(len(data))]
speed_amount = [0 for i in range(len(data))]
list_y_cord = [0 for i in range(len(data))]

for shot in range(fps * seconds):
    plt.clf()
    for num_country in range(len(data)):
        for num_year in range(len(data[num_country][0])):
            if min_year + passed_years == data[num_country][0][num_year] and last_year[num_country] != data[num_country][0][num_year]:
                yy = data[num_country][0][num_year + 1] - data[num_country][0][num_year]
                list_y_cord[num_country] = data[num_country][1][num_year]
                yyy = data[num_country][1][num_year + 1] - list_y_cord[num_country]
                last_year[num_country] = data[num_country][0][num_year]
                speed_amount[num_country] = yyy / (yy / speed_year)
                break
        list_y_cord[num_country] += speed_amount[num_country]
        plt.barh(num_country + 1, list_y_cord[num_country])
        plt.text(list_y_cord[num_country], num_country + 1, data_base.list_of_countries[num_country], fontsize=12)
    # for a in range(len(data[0][0])):
    #     if min_year + num_year == data[0][0][a] and t != data[0][0][a]:
    #         yy = data[0][0][a + 1] - data[0][0][a]
    #         y_cord = data[0][1][a]
    #         yyy = data[0][1][a + 1] - y_cord
    #         t = data[0][0][a]

    passed_years = round(float_year // 1)
    float_year += speed_year


    # list_y_cord[0] += speed_amount[0]
    # plt.barh(1, list_y_cord[0])
    # plt.barh(2, 1000)
    # print(list_y_cord[0], speed_amount[0])
    # for i in range(len(speed_amount)):
    #     list_y_cord[i] += speed_amount[i]
    #     plt.barh(i+1, list_y_cord[i])
    #     plt.text(list_y_cord[i], i+1, data_base.list_of_countries[i], fontsize=12)
    SetSetting(passed_years + min_year, max(list_y_cord))


    plt.pause(time_shot)
