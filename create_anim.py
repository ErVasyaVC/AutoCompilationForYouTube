import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import data_base
from celluloid import Camera
import json


def SetSetting(year, i):
    plt.title(year)
    plt.axis([0, 80000, 0.5, 5.5])


with open('config.json', 'r') as json_file:
    config = json.load(json_file)
    fps = config['fps']
    seconds = config['seconds']

time_shot = round(1 / fps, 3)

data = data_base.SortYears()
min_year, max_year = data[0][0][0], data[0][0][-1]
num_year = 0
speed_year = (max_year - min_year) / (fps * seconds)
float_year = 0
speed_amount = []
t = 0
for i in range(fps * seconds):
    plt.clf()
    for a in range(len(data[0][0])):
        if min_year + num_year == data[0][0][a] and t != data[0][0][a]:
            yy = data[0][0][a + 1] - data[0][0][a]
            y_cord = data[0][1][a]
            yyy = data[0][1][a + 1] - y_cord
            t = data[0][0][a]

    num_year = round(float_year // 1)
    float_year += speed_year

    y_cord += (yyy / (yy / speed_year))
    SetSetting(num_year + min_year, y_cord)

    plt.barh(1, y_cord)
    plt.barh(2, 40000)
    plt.barh(3, 30000)
    plt.barh(4, 20000)
    plt.barh(5, 10000)
    plt.pause(time_shot)
