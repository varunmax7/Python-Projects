#Week-12 P5
#Plotly piechart
import plotly.graph_objects as go
labels = ["Fri", "Sat", "Sun", "Thur"]
values = [325.88, 1778.40, 1627.16, 1096.330]
fig = go.figure()
fig.add_trace(go.pie(labels, values= values))
fig.update_layout(title = 'Total bill by Day')
fig.show()
