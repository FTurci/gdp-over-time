import pandas as pd
import wikipedia as wp
# install using 
# pip install git+https://github.com/lucasdnd/Wikipedia.git
import pandas as pd
import numpy as np
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

title = 'List of regions by past GDP (PPP)'

html = wp.page(title).html().encode("UTF-8")


dfs = pd.read_html(html)

#  print info abou all tables
# for i,df in enumerate(dfs):
#     print("table",i)
#     # print(df)
#     print(df.columns)

import matplotlib.pyplot as plt

table = dfs[2]

table = table[:-1]
print(table['Country / Region'])
time = [float(t) for t in table.columns[1:]]
plt.figure(figsize=(8,6))

selection = ['Total Western Europe','Eastern Europe','United States',  'Africa', 'West Asia', 'India[A]','China',]
for country in selection:# table['Country / Region']:
    print(country)
    d = np.array(table[table['Country / Region']==country][table.columns[1:]])[0].astype(str)
    data = [locale.atof(u) for u in d]
    print(data)
    print(len(data), len(time))
    plt.plot(time,data,label=country)
plt.legend()
plt.yscale('log')
plt.xlabel('Year')
plt.ylabel('GDP (PPP) in millions of 1990 Int. Dollars')

plt.show()
