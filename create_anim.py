import data_base
import json
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot


def SetSetting(year, amount_countries, i):
    plt.title(label="Amount of tourists", loc='left', fontsize=20, fontweight='bold')
    #ax.set_title(label="Title", pad=-1, fontsize=16, loc='left')
    ax.axis([0, (i + 10000) / 1000, 0.5, 20 + 0.5])
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
    #ax.set_aspect('auto', adjustable='datalim')


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
speed_rearrangement = 0.1
last_year, speed_amount, list_y_cord = [0 for i in range(len(data))], [0 for i in range(len(data))], \
                                       [0 for i in range(len(data))]


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
        if(now_list_x_cord[num_country] + 1 <= 20.5):
            plt.barh(now_list_x_cord[num_country] + 1, list_y_cord[num_country] / 1000, color='red',#color=colors[num_country],
                     alpha=0.7)
            plt.text((list_y_cord[num_country] + 1000) / 1000, now_list_x_cord[num_country] + 1,
                     srt_num, fontsize=9)
            plt.text(-0.5, now_list_x_cord[num_country] + 1,
                     data_base.list_of_countries[num_country], fontsize=10, horizontalalignment='right')

    passed_years = round(float_year // 1)
    float_year += speed_year
    plt.pause(0.01)

# plt.savefig('filename.png', dpi=500)
plt.show()
plt.pause(5)
plt.close()

# a = ['Albania', 'Algeria', 'Andorra', 'Argentina', 'Australia', 'Austria', 'Bahamas', 'Bahrain', 'Belarus', 'Belgium', 'Botswana', 'Brazil', 'Bulgaria', 'Cambodia', 'Canada', 'Chile', 'China', 'China, Hong Kong SAR', 'China, Macao SAR', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Dominican Republic', 'Egypt', 'El Salvador', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Guam', 'Guatemala', 'Hungary', 'India', 'Indonesia', 'Iran (Islamic Republic of)', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', "Lao People's Dem. Rep.", 'Latvia', 'Lebanon', 'Lithuania', 'Malaysia', 'Malta', 'Mexico', 'Morocco', 'Mozambique', 'Netherlands', 'New Zealand', 'Nicaragua', 'Norway', 'Other non-specified areas', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saudi Arabia', 'Singapore', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Tunisia', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Viet Nam', 'Zimbabwe']
# b = []
# # print(NameCountries())
# SortForCountries(NameCountries())
# for i in a:
#     config['list_of_countries'].append(i)
# config['list_of_countries'] = b.copy()
# with open('config.json', 'w') as json_file:
#     json.dump(config, json_file, indent=2)