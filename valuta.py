import matplotlib.pyplot as plt
import pandas as pd


interv = pd.read_csv('Валютні інтервенції НБУ.csv')
data = pd.read_csv('free.csv')

# 2020 year
rule = data['Дата'].map(lambda x: pd.to_datetime(x) >= pd.to_datetime('01.01.2016')) #and pd.to_datetime(x) <= pd.to_datetime('01.05.2020'))
result = data.iloc[data[rule].index[0]:data[rule].index[-1]]
interv = interv.drop(index=0)

#print(data)
#input()

pd.plotting.autocorrelation_plot(result.set_index('Дата'))

#result['Офіційний курс гривні'] = result['Офіційний курс гривні'].astype(str)
result.plot('Дата', 'Офіційний курс гривні')

fig, axes = plt.subplots(1, 1)

#pd.plotting.autocorrelation_plot(result)


#axes[0].plot(result['Дата'], result['Офіційний курс гривні'], label='нбу')

axes.bar(interv.index, interv['Сальдо ( купівля «-» продаж)'], label='Интервенции нбу в млрд $')
axes.set_ylabel('Сальдо')
axes.set_xlabel('№ месяца')


plt.show()
