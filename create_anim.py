import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import data_base


def SetSetting():
    plt.title("Количество туристов")
    plt.axis([0, 1, 0.5, 5.5])

fps = 24
time = 5
time_shot = round(1 / fps, 3)

# for i in range(fps * time):
#     plt.clf()
#     SetSetting()
#     years = 0
#
#
#     # plt.axis([0, i , 0.5, 5.5])
#     # plt.ylabel('Количество турисов')
#     # y = i
#     # x = 1
#
#     # plt.barh(x, y)
#     # plt.barh(2, 40000)
#     # plt.barh(3, 30000)
#     # plt.barh(4, 20000)
#     # plt.barh(5, 10000)
#     plt.pause(time_shot)
# plt.show()
