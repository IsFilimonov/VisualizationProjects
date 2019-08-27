import plotly.express as px

tips = px.data.tips()



fig = px.parallel_categories(tips)

fig.show()
