'''
    This is a simple program to analyze a dataset of the global
    average sea level change since 1880 and make predictions

    Ref: FreeCodeCamp.org - Data Analysis with Python Projects
         Project #5: Sea Level Predictor
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
x = df['Year']
y = df['CSIRO Adjusted Sea Level']

#   find y-values for the line of best fit
slope, intercept = linregress(x, y)[:2]
lbf_y = slope * x + intercept

#   y-value for prediction at 2050
pred_y = slope * 2050 + intercept

#   append 'x' and 'y' with the new values
pred = {'Year': 2050, 'CSIRO Adjusted Sea Level': pred_y}
df = df.append(pred, ignore_index=True)
x = df['Year']
y = df['CSIRO Adjusted Sea Level']

#   y-values for th line of best fit
y_prediction = slope * x + intercept

#   scatter plot and line of best fit (2050 prediction included)
plt.subplot(1, 2, 1)
plt.scatter(x, y, label='Data points')
plt.plot(x, y_prediction, color='red', label='Line of best fit')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()


#   plotting with new dataframe starting from year 2000
idx = df['Year'].eq(2000).idxmax()
df = df[idx:].reset_index(drop=True)
x = df['Year']
y = df['CSIRO Adjusted Sea Level']

#   plot a new line of best fit
slope, intercept = linregress(x, y)[:2]
lbf2 = slope * x + intercept
plt.subplot(1, 2, 2)
plt.scatter(x, y, label='New Scatter Plot')
plt.plot(x, lbf2, color='red', label='New Line of Best Fit')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level (from 2000)')
plt.legend()
plt.savefig('output-figures/sea-level-prediction.jpg')
plt.show()
