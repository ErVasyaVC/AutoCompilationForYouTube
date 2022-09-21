import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import data_base


contr = 'United States of America'


years, amount = data_base.SortForCountries(contr)

data = data_base.SortForCountries(contr)
print(data)
# plt.axis([0, 100000, 0.5, 5.5])
# for i in range(amount[0], amount[-1], 100):
#     plt.clf()
#     plt.axis([0, i, 0.5, 5.5])
#     plt.ylabel('Количество турисов')
#     y = i
#     x = 1
#     plt.barh(x, y)
#     plt.barh(2, 40000)
#     plt.barh(3, 30000)
#     plt.barh(4, 20000)
#     plt.barh(5, 10000)
#     plt.pause(0.01)
#
#
# plt.ylabel('Количество турисов')
#
# plt.show()
