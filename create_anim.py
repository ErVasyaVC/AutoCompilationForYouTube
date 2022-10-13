import data_base
import json
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot


def SetSetting(year, amount_countries, i):
    plt.title(label=year, loc='right', fontsize=20, fontweight='bold', pad=-200)
    ax.axis([0, (i + 20000) / 1000, 0.5, amount_countries + 0.5])
    ax.set_title(label=year, y=-1, pad=-480, fontsize=20)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.left.set_visible(False)
    ax.spines.bottom.set_visible(False)
    ax.grid(axis='x', color='gray', linewidth=0.5, alpha=0.4)

    ratio = 1.2
    # x_left, x_right = ax.get_xlim()
    # y_low, y_high = ax.get_ylim()
    # x_right += 50
    # ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    ax.set_aspect(20)

def SortDescending(array_amount):
    return_array = [0 for i in range(len(array_amount))]
    sort_array = array_amount.copy()
    sort_array.sort(reverse=True)

    place = 0
    for i in sort_array:
        return_array[array_amount.index(i)] = place
        place += 1

    return return_array


def StrAmount(amount):
    string = ""
    n = len(str(int(amount))) // 3 + 2
    for i in range(n):
        temp = int(amount // 1000 % 1000)
        if i != 0 and temp < 100:
            string += "0" + str(temp)
        else:
            string += str(temp)
        if i != n - 1:
            string += ","
        amount = amount * 1000
    return string


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
speed_rearrangement = 0.08

fig = plt.figure()
fig.set_size_inches(6.5, 8)
ax = Subplot(fig, 111)

for shot in range(fps * seconds):
    plt.clf()
    ax = fig.add_subplot(111)

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
        list_y_cord[num_country] += speed_amount[num_country]

    true_list_x_cord = SortDescending(list_y_cord)

    if shot == 0:
        now_list_x_cord = true_list_x_cord.copy()
    SetSetting(passed_years + min_year, len(data), max(list_y_cord))
    for num_country in range(len(data)):
        if abs(now_list_x_cord[num_country] - true_list_x_cord[num_country]) < 0.05:
            now_list_x_cord[num_country] = true_list_x_cord[num_country]
        elif now_list_x_cord[num_country] > true_list_x_cord[num_country]:
            now_list_x_cord[num_country] -= speed_rearrangement
        elif now_list_x_cord[num_country] < true_list_x_cord[num_country]:
            now_list_x_cord[num_country] += speed_rearrangement
        srt_num = StrAmount(list_y_cord[num_country])
        plt.barh(now_list_x_cord[num_country] + 1, list_y_cord[num_country] / 1000, color=colors[num_country], alpha=0.7)
        plt.text((list_y_cord[num_country] + 1000) / 1000, now_list_x_cord[num_country] + 1,
                 srt_num, fontsize=11)
        plt.text(-70, now_list_x_cord[num_country] + 1,
                 data_base.list_of_countries[num_country], fontsize=11)

    passed_years = round(float_year // 1)
    float_year += speed_year
    plt.pause(0.01)

# plt.savefig('filename.png', dpi=500)
plt.show()
plt.pause(5)
plt.close()
