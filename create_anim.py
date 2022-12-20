import data_base
import json
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot


def SetSetting(year, title, i):
    img = plt.imread("flag_EU.jpg")
    plt.title(label=title, loc='left', fontsize=30, fontweight='bold')
    # ax.set_title(label="Title", pad=-1, fontsize=16, loc='left')
    ax.axis([0, (i + 1000) / 1000, 0.5, count_countries + 0.5])
    ax.set_xlabel(year, x=0.95, fontsize=40, fontweight='bold', color='red')
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.spines.left.set_visible(False)
    ax.spines.bottom.set_visible(False)
    ax.grid(axis='x', color='gray', linewidth=0.5, alpha=0.4)
    plt.yticks([])

    # ratio = 1.2
    # x_left, x_right = ax.get_xlim()
    # y_low, y_high = ax.get_ylim()
    # x_right += 50
    # ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)


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
    count_countries = config['count_countries']
    language = config['language']
    language_selection = config['language_selection']

time_shot = round(1 / fps, 3)
data = data_base.SortYears()
min_year, max_year = data[0][0][0], data[0][0][-1]
passed_years, float_year = 0, 0
speed_year = (max_year - min_year) / (fps * seconds)
speed_amount = list()
speed_rearrangement = 0.1
last_year, speed_amount, list_y_cord = [0 for i in range(len(data))], [0 for i in range(len(data))], \
                                       [0 for i in range(len(data))]

viewing_mode = False

fig = plt.figure()
fig.set_size_inches(10, 12)
ax = Subplot(fig, 111)

# a = []

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

    SetSetting(passed_years + min_year, language_selection[language]['title'], max(list_y_cord))

    for num_country in range(len(data)):
        if abs(now_list_x_cord[num_country] - true_list_x_cord[num_country]) < 0.05:
            now_list_x_cord[num_country] = true_list_x_cord[num_country]
        elif now_list_x_cord[num_country] > true_list_x_cord[num_country]:
            now_list_x_cord[num_country] -= speed_rearrangement
        elif now_list_x_cord[num_country] < true_list_x_cord[num_country]:
            now_list_x_cord[num_country] += speed_rearrangement
        srt_num = StrAmount(list_y_cord[num_country])
        if now_list_x_cord[num_country] + 1 <= count_countries + 0.5:
            plt.barh(now_list_x_cord[num_country] + 1, list_y_cord[num_country] / 1000, color=colors[num_country],
                     alpha=0.7)
            plt.text((list_y_cord[num_country] + 400) / 1000, now_list_x_cord[num_country] + 1,
                     srt_num, fontsize=13)
            plt.text(-0.2, now_list_x_cord[num_country] + 1,
                     language_selection[language][data_base.list_of_countries[num_country]]
                     , fontsize=14, horizontalalignment='right')
            # if not data_base.list_of_countries[num_country] in a:
            #     a.append(data_base.list_of_countries[num_country])

    passed_years = round(float_year // 1)
    float_year += speed_year
    if not viewing_mode:
        plt.savefig('images/touristEU/imagesEng/shot' + str(shot) + '.png', dpi=200)
    plt.pause(0.01)
plt.show()
plt.pause(2)
plt.close()

# b = []
# # print(NameCountries())
# SortForCountries(NameCountries())

# config['list_of_countries'] = b.copy()
# with open('config.json', 'w') as json_file:
#     json.dump(config, json_file, indent=2)
# for i in a:
#     config['list_of_countries'].append(i)
#
# with open('config.json', 'w') as json_file:
#     json.dump(config, json_file, indent=2)