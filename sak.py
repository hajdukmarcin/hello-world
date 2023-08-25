import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
import matplotlib.axes as ax

matplotlib.rcParams.update({'font.size': 14})

fig = plt.figure()

ax1 = fig.add_subplot(211)

data = np.loadtxt("flux.dat")
jd = data[:, 0]
f8ghz = data[:, 1]
ef8ghz = data[:, 2]
f5ghz = data[:, 3]
ef5ghz = data[:, 4]
f1ghz = data[:, 5]
ef1ghz = data[:, 6]
f1 = data[:, 7]
f2 = data[:, 8]

for n in range(len(jd)):
    plt.errorbar(jd[n]-2450000, f8ghz[n], xerr=0, yerr=ef8ghz[n], color='black', linestyle=' ')
    plt.plot(jd[n]-2450000, f8ghz[n], color='black', marker='o')

plt.yscale('log')


ax1.set_ylabel(r'F(8GHz) [$\mu$Jy]')
ax1.set_xlabel('JD-2450000 [day]')
ax1.set_xlim(2900, 10200)
ax1.set_ylim(10, 1000)

ax2 = fig.add_subplot(212)

for n in range(len(jd)):
    plt.errorbar(jd[n]-2450000, np.log10(f8ghz[n]/f5ghz[n])/np.log10(f1[n]/f2[n]), xerr=0, yerr=(np.sqrt(np.square(ef8ghz[n]/f5ghz[n])+np.square(ef5ghz[n]*f8ghz[n]/f5ghz[n]/f5ghz[n]))) * f5ghz[n]/f8ghz[n] / np.log10(f1[n]/f2[n])/(np.log(10)), color='black', linestyle=' ')
    plt.plot(jd[n]-2450000, np.log10(f8ghz[n]/f5ghz[n])/np.log10(f1[n]/f2[n]), color='black', marker='o')

ax2.set_xlim(2900, 10200)
ax2.set_xlabel('JD-2450000 [day]')
ax2.set_ylabel(r'$\alpha$')

ax1.set_xticks([3371.5, 5197.5, 7023.5, 8849.5])
ax1.set_xticklabels(['2005','2010','2015','2020'])

plt.show()
