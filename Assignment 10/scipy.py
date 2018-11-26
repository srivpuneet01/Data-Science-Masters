from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
months = np.arange(12)

#periodic function
def yearly_temps(times, avg, ampl, time_offset):
    return (avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

Max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
Min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

#1. fitting it to the periodic function
res_max, cov_max = optimize.curve_fit(yearly_temps, months,Max)
res_min, cov_min = optimize.curve_fit(yearly_temps, months,Min)
print(res_max)
print(res_min)

#2. plot the fit
days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months,Max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months,Min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()