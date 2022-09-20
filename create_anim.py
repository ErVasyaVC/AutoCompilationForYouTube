import matplotlib.pyplot as plt
import numpy as np
import data_base

# print(data_base.NameCountries())
# countries = input("Countries: ").split(' ')
# print(countries)
contr = 'United States of America'

data_frame, columns = data_base.ReadDataFrame()

years = []
amount = []
for i in data_frame[data_frame[columns[0]] == contr][columns[1]]:
    years.append(int(i))
for i in data_frame[data_frame[columns[0]] == contr][columns[2]]:
    amount.append(int(i.split(',')[0]+i.split(',')[1]))
print(years)
print(amount)


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')

plt.plot([1, 2, 3, 3], [1, 4, 9, 16], 'ro')
plt.ylabel('some numbers')
plt.axis([0, 6, 0, 20])
#plt.show()

