import pandas as pd
import plotly.express as px

NAVY = '#153252'
TEAL = '#009b98'
COLORS = ['#007f86','#315b87','#e6a34a','#8e6eaa','#4fae86','#cf7668','#597c99','#a58c54','#5f6692']
LABELS = {'purchase_lead':'Purchase lead time (days)', 'length_of_stay':'Length of stay (days)', 'flight_duration':'Flight duration (hours)', 'num_passengers':'Passengers per booking', 'flight_hour':'Flight hour', 'booking_origin':'Booking origin', 'route':'Route', 'sales_channel':'Sales channel', 'trip_type':'Trip type', 'flight_day':'Flight day', 'wants_extra_baggage':'Extra baggage requested', 'wants_preferred_seat':'Preferred seat requested', 'wants_in_flight_meals':'In-flight meals requested', 'total_extra_services':'Total extra services'}

def label(x):
    for prefix in ['sales_channel_', 'trip_type_', 'flight_day_']:
        if x.startswith(prefix): return LABELS[prefix[:-1]] + ': ' + x[len(prefix):]
    return LABELS.get(x, x.replace('_',' ').capitalize())

def style(fig):
    fig.update_layout(template='plotly_white', font=dict(family='Arial', color=NAVY), margin=dict(l=15,r=15,t=45,b=15), legend_title_text='', height=350)
    return fig

def rate_chart(df, column, title, bins=False):
    d = df.copy()
    if bins:
        try: d[column] = pd.qcut(d[column], q=5, duplicates='drop').astype(str)
        except ValueError: d[column] = d[column].astype(str)
    if column.startswith('wants_'): d[column] = d[column].map({0:'Not requested',1:'Requested'})
    grouped = d.groupby(column, observed=True, dropna=False)['booking_complete'].agg(records='size', completed='sum', rate='mean').reset_index()
    if column in ['booking_origin','route']: grouped = grouped.nlargest(10,'records')
    grouped['rate'] *= 100
    fig = px.bar(grouped, x=column, y='rate', custom_data=['records','completed'], title=title, labels={column:label(column),'rate':'Completion rate (%)'}, color_discrete_sequence=[TEAL])
    fig.update_traces(hovertemplate='%{x}<br>Completion: %{y:.1f}%<br>Records: %{customdata[0]:,}<br>Completed: %{customdata[1]:,}<extra></extra>')
    return style(fig)
