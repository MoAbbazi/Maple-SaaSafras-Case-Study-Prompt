#!/usr/bin/env python
# coding: utf-8

# In[5]:


import plotly.graph_objects as go
import numpy as np

# Data for each roster (replace with actual data)
roster_names = ['Roster 1', 'Roster 2', 'Roster 3', 'Roster 4']
revenue_data_roster1 = [100000, 101875, 103750, 105625, 107500, 109375, 111250, 113125, 115000, 116875, 118750, 120625]
revenue_data_roster2 = [100000, 103125, 106250, 109375, 112500, 115625, 118750, 121875, 125000, 128125, 131250, 134375]
revenue_data_roster3 = [100000, 106250, 112500, 118750, 125000, 131250, 137500, 143750, 150000, 156250, 162500, 168750]
revenue_data_roster4 = [100000, 104750, 109500, 114250, 116000, 120750, 125500, 130250, 135000, 139750, 144500, 149250]

# Months (assuming 12 months)
months = list(range(1, 13))

# Calculate cumulative sums for stacked bar chart
revenue_data_cumulative = np.vstack((revenue_data_roster1,
                                     np.add(revenue_data_roster1, revenue_data_roster2),
                                     np.add(np.add(revenue_data_roster1, revenue_data_roster2), revenue_data_roster3),
                                     np.add(np.add(np.add(revenue_data_roster1, revenue_data_roster2), revenue_data_roster3), revenue_data_roster4)))

# Line Chart Visualization for Revenue Data
fig_line = go.Figure()
for i, roster_data in enumerate(revenue_data_cumulative):
    fig_line.add_trace(go.Scatter(x=months, y=roster_data, mode='lines+markers', name=roster_names[i]))

fig_line.update_layout(title='Monthly Revenue for Each Roster',
                       xaxis_title='Months',
                       yaxis_title='Revenue',
                       showlegend=True)

# Bar Chart Visualization for Revenue Data
fig_bar = go.Figure()
for i, roster_data in enumerate(revenue_data_cumulative):
    fig_bar.add_trace(go.Bar(x=months, y=roster_data, name=roster_names[i]))

fig_bar.update_layout(title='Monthly Revenue for Each Roster (Stacked Bar Chart)',
                      xaxis_title='Months',
                      yaxis_title='Revenue',
                      showlegend=True,
                      barmode='stack')

# Pie Chart Visualization for Revenue Data
fig_pie = go.Figure()
for i, roster_data in enumerate(revenue_data_cumulative):
    total_revenue = roster_data[-1]
    contribution = [round(revenue / total_revenue * 100, 2) for revenue in roster_data]
    fig_pie.add_trace(go.Pie(labels=months, values=contribution, name=roster_names[i]))

fig_pie.update_layout(title='Monthly Revenue Contribution for Each Roster',
                      showlegend=True)

# Stacked Bar Chart Visualization for Customer Data (Assuming similar structure for customer data)
customers_data_roster1 = [900, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]
customers_data_roster2 = [900, 1150, 1250, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]
customers_data_roster3 = [900, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725, 1800]
customers_data_roster4 = [900, 975, 1050, 1125, 1200, 1275, 1350, 1425, 1500, 1575, 1650, 1725]

customers_data_cumulative = np.vstack((customers_data_roster1,
                                       np.add(customers_data_roster1, customers_data_roster2),
                                       np.add(np.add(customers_data_roster1, customers_data_roster2), customers_data_roster3),
                                       np.add(np.add(np.add(customers_data_roster1, customers_data_roster2), customers_data_roster3), customers_data_roster4)))

fig_bar_customers = go.Figure()
for i, roster_data in enumerate(customers_data_cumulative):
    fig_bar_customers.add_trace(go.Bar(x=months, y=roster_data, name=roster_names[i]))

fig_bar_customers.update_layout(title='Monthly Customers for Each Roster (Stacked Bar Chart)',
                                xaxis_title='Months',
                                yaxis_title='Number of Customers',
                                showlegend=True,
                                barmode='stack')

# Pie Chart Visualization for Customer Data
fig_pie_customers = go.Figure()
for i, roster_data in enumerate(customers_data_cumulative):
    total_customers = roster_data[-1]
    contribution = [round(customers / total_customers * 100, 2) for customers in roster_data]
    fig_pie_customers.add_trace(go.Pie(labels=months, values=contribution, name=roster_names[i]))

fig_pie_customers.update_layout(title='Monthly Customer Contribution for Each Roster',
                                showlegend=True)

# Display all figures
fig_line.show()
fig_bar.show()
fig_pie.show()
fig_bar_customers.show()
fig_pie_customers.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




