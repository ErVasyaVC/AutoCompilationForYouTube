import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import data_base
from celluloid import Camera
import json


def SetSetting(year, i):
    plt.title(label=year, loc='right', fontsize=20, fontweight='bold', pad=-200)
    plt.axis([0, 90000, 0.5, 5.5])
    ax = plt.subplot()
    ax.set_title(label=year, y=-1, pad=-280, fontsize=20)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.left.set_visible(False)
    ax.spines.bottom.set_visible(False)


def SortDescending(array_amount):
    return_array = []
    sort_array = []
    for i in array_amount:
        sort_array.append(i)
    sort_array.sort()
    for i in sort_array:
        return_array.append(array_amount.index(i))
    return return_array


with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    fps = config['fps']
    seconds = config['seconds']
    colors = config['colors']

time_shot = round(1 / fps, 3)
data = data_base.SortYears()
min_year, max_year = data[0][0][0], data[0][0][-1]
passed_years, float_year = 0, 0
speed_year = (max_year - min_year) / (fps * seconds)
speed_amount = list()
last_year, speed_amount, list_y_cord = [0 for i in range(len(data))], [0 for i in range(len(data))], \
                                       [0 for i in range(len(data))]

for shot in range(fps * seconds):
    plt.clf()
    for num_country in range(len(data)):
        for num_year in range(len(data[num_country][0])):
            if min_year + passed_years == data[num_country][0][num_year] and last_year[num_country] != \
                    data[num_country][0][num_year]:
                difference_years = data[num_country][0][num_year + 1] - data[num_country][0][num_year]
                list_y_cord[num_country] = data[num_country][1][num_year]
                difference_amount = data[num_country][1][num_year + 1] - list_y_cord[num_country]
                last_year[num_country] = data[num_country][0][num_year]
                speed_amount[num_country] = difference_amount / (difference_years / speed_year)
                break

    # list_x_cord = SortDescending(list_y_cord)
    # list_x_cord = [0 for i in range(len(data))]
    # for num_country in range(len(data)):
    #     list_y_cord[num_country] += speed_amount[num_country]
    #     plt.barh(list_x_cord[num_country] + 1, list_y_cord[num_country], color=colors[num_country])
    #     plt.text(list_y_cord[num_country], list_x_cord[num_country] + 1, data_base.list_of_countries[num_country], fontsize=11)

    for num_country in range(len(data)):
        list_y_cord[num_country] += speed_amount[num_country]
        plt.barh(num_country + 1, list_y_cord[num_country], color=colors[num_country])
        plt.text(list_y_cord[num_country], num_country + 1, data_base.list_of_countries[num_country], fontsize=11)

    passed_years = round(float_year // 1)
    float_year += speed_year
    SetSetting(passed_years + min_year, max(list_y_cord))

    plt.pause(time_shot)
