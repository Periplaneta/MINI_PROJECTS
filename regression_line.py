import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

question={
    'Age in months': np.linspace(0,7,8),
    "Mean weight in kg": [2.5, 3.75, 4.2, 5.7, 6.4, 7.35, 8.25, 9.6 ]
} 
# Creating dataframe from dictionary 
data = pd.DataFrame(question)

# conputing the statistical mean of 'Age in months' and 'Mean weight in kg '
first_x_mean = data['Age in months'].mean()
first_y_mean = data.drop(columns= 'Age in months').mean()

# filtering dataset for values of 'Age in months ' > statistical mean of 'Age in months'
# and its corresponding 'Mean weight in kg' values 
filt = data['Age in months'] > first_x_mean
data1 = data.loc[filt]
second_x_mean = data1['Age in months'].mean()
second_y_mean = data1['Mean weight in kg'].mean()

# filtering dataset for values of 'Age in months ' < statistical mean of 'Age in months'
# and its corresponding 'Mean weight in kg' values 
filt_1 = data['Age in months'] < first_x_mean
data2 = data.loc[filt_1]
third_x_mean = data2['Age in months'].mean()
third_y_mean = data2['Mean weight in kg'].mean()

x = [first_x_mean,second_x_mean,third_x_mean]
y = [first_y_mean,second_y_mean,third_y_mean]

# Using pyplot to plot the scatter diagram together with the line of best fit 
plt.scatter(data['Age in months'], data['Mean weight in kg'], linewidths=2)
plt.plot(x, y)
plt.grid()
plt.show()