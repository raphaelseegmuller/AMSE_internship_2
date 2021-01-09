import matplotlib.pyplot as plt

from libs.function import get_histogram_values
from tourism_data import Department_tourism_2019_list, Paris_tourism_2019

# Histogram scale (can be modified) #
scale = 250000

bins_list = [0]
sc = 0
while sc < Paris_tourism_2019:
    sc += scale
    bins_list += [sc]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel("Nights number in 2019")
plt.ylabel("French department number")
plt.title("Histogram of nights number per french departments (without Corsica)")
ax.hist(Department_tourism_2019_list, bins=bins_list)

# A = np.array(Department_tourism_2019_list)
# print(np.median(A))

plt.show()
