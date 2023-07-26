#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import numpy as np

# Data for each roster
roster_names = ['Roster 1', 'Roster 2', 'Roster 3', 'Roster 4']
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Create a list to store data for each roster
revenue_data_rosters = [revenue_data_roster1, revenue_data_roster2, revenue_data_roster3, revenue_data_roster4]

# Calculate the cumulative sums for each roster
cumulative_revenue_data_rosters = [list(np.cumsum(revenue_data)) for revenue_data in revenue_data_rosters]

# Create the interactive pie chart for each roster separately
for i, roster_data in enumerate(cumulative_revenue_data_rosters):
    total_revenue = roster_data[-1]
    contribution = [round(revenue / total_revenue * 100, 2) for revenue in roster_data]

    fig = go.Figure(go.Pie(labels=months, values=contribution, name=roster_names[i]))
    fig.update_layout(title_text=f'Monthly Revenue Contribution for {roster_names[i]}',
                      showlegend=True,
                      annotations=[dict(text=f'Month {months[j]}', x=contribution[j], y=1.1, font_size=10, showarrow=False) for j in range(len(months))])

    fig.show()


# In[ ]:





# In[ ]:





# In[2]:


import matplotlib.pyplot as plt
import numpy as np

revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Calculate the cumulative sums for each roster
cumulative_revenue_data_roster1 = np.cumsum(revenue_data_roster1)
cumulative_revenue_data_roster2 = np.cumsum(revenue_data_roster2)
cumulative_revenue_data_roster3 = np.cumsum(revenue_data_roster3)
cumulative_revenue_data_roster4 = np.cumsum(revenue_data_roster4)

# Stacked Bar Chart for Revenue Data
plt.figure(figsize=(10, 6))
plt.bar(months, revenue_data_roster1, label='Roster 1', alpha=0.7)
plt.bar(months, revenue_data_roster2, bottom=revenue_data_roster1, label='Roster 2', alpha=0.7)
plt.bar(months, revenue_data_roster3, bottom=revenue_data_roster2, label='Roster 3', alpha=0.7)
plt.bar(months, revenue_data_roster4, bottom=revenue_data_roster3, label='Roster 4', alpha=0.7)
plt.xlabel('Months')
plt.ylabel('Revenue')
plt.title('Monthly Revenue for Each Roster')
plt.legend()
plt.grid(True)
plt.show()

# Customer Data for each roster 
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster3 = [900, 1200, 1250, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

# Calculate the cumulative sums for each roster
cumulative_customers_data_roster1 = np.cumsum(customers_data_roster1)
cumulative_customers_data_roster2 = np.cumsum(customers_data_roster2)
cumulative_customers_data_roster3 = np.cumsum(customers_data_roster3)
cumulative_customers_data_roster4 = np.cumsum(customers_data_roster4)

# Stacked Bar Chart for Customer Data
plt.figure(figsize=(10, 6))
plt.bar(months, customers_data_roster1, label='Roster 1', alpha=0.7)
plt.bar(months, customers_data_roster2, bottom=customers_data_roster1, label='Roster 2', alpha=0.7)
plt.bar(months, customers_data_roster3, bottom=customers_data_roster2, label='Roster 3', alpha=0.7)
plt.bar(months, customers_data_roster4, bottom=customers_data_roster3, label='Roster 4', alpha=0.7)
plt.xlabel('Months')
plt.ylabel('Number of Customers')
plt.title('Monthly Number of Customers for Each Roster')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[3]:


import matplotlib.pyplot as plt

# Revenue Data for each roster 
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Line Chart Visualization for Revenue Data
plt.figure(figsize=(10, 6))
plt.plot(months, revenue_data_roster1, label='Roster 1', marker='o')
plt.plot(months, revenue_data_roster2, label='Roster 2', marker='o')
plt.plot(months, revenue_data_roster3, label='Roster 3', marker='o')
plt.plot(months, revenue_data_roster4, label='Roster 4', marker='o')
plt.xlabel('Months')
plt.ylabel('Revenue')
plt.title('Monthly Revenue for Each Roster')
plt.legend()
plt.grid(True)
plt.show()

# Customer Data for each roster (replace with actual data)
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster3 = [900, 1200, 1250, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

# Line Chart Visualization for Customer Data
plt.figure(figsize=(10, 6))
plt.plot(months, customers_data_roster1, label='Roster 1', marker='o')
plt.plot(months, customers_data_roster2, label='Roster 2', marker='o')
plt.plot(months, customers_data_roster3, label='Roster 3', marker='o')
plt.plot(months, customers_data_roster4, label='Roster 4', marker='o')
plt.xlabel('Months')
plt.ylabel('Number of Customers')
plt.title('Monthly Number of Customers for Each Roster')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[4]:


import matplotlib.pyplot as plt
import numpy as np

# Revenue Data for each roster (replace with actual data)
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Unstacked Bar Chart for Revenue Data
plt.figure(figsize=(10, 6))
plt.bar(months, revenue_data_roster1, label='Roster 1', alpha=0.7)
plt.bar(months, revenue_data_roster2, label='Roster 2', alpha=0.7)
plt.bar(months, revenue_data_roster3, label='Roster 3', alpha=0.7)
plt.bar(months, revenue_data_roster4, label='Roster 4', alpha=0.7)
plt.xlabel('Months')
plt.ylabel('Revenue')
plt.title('Monthly Revenue for Each Roster')
plt.legend()
plt.grid(True)
plt.show()

# Customer Data for each roster (replace with actual data)
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster3 = [900, 1200, 1250, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

# Unstacked Bar Chart for Customer Data
plt.figure(figsize=(10, 6))
plt.bar(months, customers_data_roster1, label='Roster 1', alpha=0.7)
plt.bar(months, customers_data_roster2, label='Roster 2', alpha=0.7)
plt.bar(months, customers_data_roster3, label='Roster 3', alpha=0.7)
plt.bar(months, customers_data_roster4, label='Roster 4', alpha=0.7)
plt.xlabel('Months')
plt.ylabel('Number of Customers')
plt.title('Monthly Number of Customers for Each Roster')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[5]:


import matplotlib.pyplot as plt
import numpy as np

# Revenue Data for each roster (replace with actual data)
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Bar Chart for Revenue Data with Separate Colors
colors = ['b', 'g', 'y', 'r']
roster_names = ['Roster 1', 'Roster 2', 'Roster 3', 'Roster 4']
for i, data in enumerate([revenue_data_roster1, revenue_data_roster2, revenue_data_roster3, revenue_data_roster4]):
    plt.bar(months, data, label=roster_names[i], alpha=0.7, color=colors[i])

plt.xlabel('Months')
plt.ylabel('Revenue')
plt.title('Monthly Revenue for Each Roster')
plt.legend()
plt.grid(True)
plt.show()

# Customer Data for each roster (replace with actual data)
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster3 = [900, 1200, 1250, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

# Bar Chart for Customer Data with Separate Colors
colors = ['b', 'g', 'y', 'r']
roster_names = ['Roster 1', 'Roster 2', 'Roster 3', 'Roster 4']
for i, data in enumerate([customers_data_roster1, customers_data_roster2, customers_data_roster3, customers_data_roster4]):
    plt.bar(months, data, label=roster_names[i], alpha=0.7, color=colors[i])

plt.xlabel('Months')
plt.ylabel('Number of Customers')
plt.title('Monthly Number of Customers for Each Roster')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[6]:


import matplotlib.pyplot as plt
import numpy as np

# Revenue Data for each roster (replace with actual data)
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 110625, 116875, 118750, 120000, 122500, 125000, 127500, 130000, 132500, 135000, 137500]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Bar Chart for Revenue Data with Separate Colors
bar_width = 0.2
index = np.arange(len(months))

roster_names = ['Roster 1', 'Roster 2', 'Roster 3', 'Roster 4']
colors = ['b', 'g', 'y', 'r']

for i, data in enumerate([revenue_data_roster1, revenue_data_roster2, revenue_data_roster3, revenue_data_roster4]):
    plt.bar(index + i * bar_width, data, bar_width, label=roster_names[i], alpha=0.7, color=colors[i])

plt.xlabel('Months')
plt.ylabel('Revenue')
plt.title('Monthly Revenue for Each Roster')
plt.xticks(index + 1.5 * bar_width, months)
plt.legend()
plt.grid(True)
plt.show()

# Customer Data for each roster (replace with actual data)
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster3 = [900, 1200, 1250, 1300, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

# Bar Chart for Customer Data with Separate Colors
for i, data in enumerate([customers_data_roster1, customers_data_roster2, customers_data_roster3, customers_data_roster4]):
    plt.bar(index + i * bar_width, data, bar_width, label=roster_names[i], alpha=0.7, color=colors[i])

plt.xlabel('Months')
plt.ylabel('Number of Customers')
plt.title('Monthly Number of Customers for Each Roster')
plt.xticks(index + 1.5 * bar_width, months)
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




