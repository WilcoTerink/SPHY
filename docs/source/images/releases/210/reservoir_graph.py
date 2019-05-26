import pandas as pd
import os
import datetime as dt

#-some matplotlib libraries
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'font.size': 9})
colors = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r / 255., g / 255., b / 255.)
    
    

resF = r'C:\eclipse\workspace\SPHY_test_pypi\docs\source\images\releases\simple_reservoir_ts.csv'
figname = r'C:\eclipse\workspace\SPHY_test_pypi\docs\source\images\releases\simple_reservoir_fig.png'

# resF = r'C:\eclipse\workspace\SPHY_test_pypi\docs\source\images\releases\advanced_reservoir_ts.csv'
# figname = r'C:\eclipse\workspace\SPHY_test_pypi\docs\source\images\releases\advanced_reservoir_fig.png'

df = pd.read_csv(resF, parse_dates=[0], dayfirst=True)

df = df.loc[df['Date']<dt.date(2000,12,31)]
df[['Qin', 'S', 'Qout']] = df[['Qin', 'S', 'Qout']]/1000000 #-convert to MCM


fig, ax1 = plt.subplots()
h1 = ax1.plot(df.Date, df.Qin, color=colors[0], label='Q$_{in}$')
h2 = ax1.plot(df.Date, df.Qout, color=colors[1], label='Q$_{out}$')
#h2 = ax1.plot(df.Date, df.Qout, color='black', label='Q$_{out}$')
ax1.set_xlabel('Date')
ax1.set_ylabel('Flow [MCM d$^{-1}$]')
plt.legend(loc='upper left')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
h3 = ax2.plot(df.Date, df.S, color=colors[2], label='S$_{act}$')
ax2.set_ylabel('Storage [MCM]')
plt.legend(loc='upper right')
plt.title('Example of simple reservoir scheme')
#plt.title('Example of advanced reservoir scheme')
plt.savefig(figname, dpi=300.)
plt.show()    
    
    
    