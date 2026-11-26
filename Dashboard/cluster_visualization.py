import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from visual_analytics import COLORS, style, label

@st.cache_data
def pca_sample(processed):
    features = processed.drop(columns=['booking_complete','data_split','cluster'], errors='ignore').copy()
    features[['route','booking_origin']] = StandardScaler().fit_transform(features[['route','booking_origin']])
    sample = features.sample(n=min(5000,len(features)), random_state=42)
    coordinates = PCA(n_components=2, random_state=42).fit_transform(sample)
    return pd.DataFrame({'row_id':sample.index, 'PC1':coordinates[:,0], 'PC2':coordinates[:,1]}).set_index('row_id')

def render_clusters(df, processed):
    st.subheader('Passenger segmentation')
    st.caption('K-Means segments from the team’s saved run. Booking completion is used only for profiling after clustering. Figures reflect the current filters.')
    grouped = df.groupby('cluster')['booking_complete'].agg(records='size', completed='sum', rate='mean').reset_index()
    grouped['incomplete'] = grouped['records'] - grouped['completed']
    grouped['share'] = grouped['records']/len(df)*100
    grouped['segment'] = grouped['cluster'].map(lambda x: f'Segment {x}')
    color_map = {f'Segment {i}': COLORS[n % len(COLORS)] for n,i in enumerate(sorted(processed.cluster.unique()))}
    cards=st.columns(5)
    cards[0].metric('Segments',len(grouped))
    cards[1].metric('Largest',f"Segment {grouped.loc[grouped.records.idxmax(),'cluster']}")
    cards[2].metric('Smallest',f"Segment {grouped.loc[grouped.records.idxmin(),'cluster']}")
    cards[3].metric('Highest completion',f"Segment {grouped.loc[grouped.rate.idxmax(),'cluster']}")
    cards[4].metric('Lowest completion',f"Segment {grouped.loc[grouped.rate.idxmin(),'cluster']}")
    a,b=st.columns(2)
    with a:
        fig=px.pie(grouped, names='segment', values='records', hole=.65, title='Booking records by segment', color='segment', color_discrete_map=color_map, custom_data=['records','share'])
        fig.update_traces(hovertemplate='%{label}<br>Records: %{customdata[0]:,}<br>Share: %{customdata[1]:.1f}%<extra></extra>')
        st.plotly_chart(style(fig),use_container_width=True)
    with b:
        grouped['rate_pct']=grouped.rate*100
        fig=px.bar(grouped,x='segment',y='rate_pct',color='segment',color_discrete_map=color_map,title='Completion rate by segment',custom_data=['completed','incomplete','records'],labels={'segment':'Segment','rate_pct':'Completion rate (%)'})
        fig.update_traces(hovertemplate='%{x}<br>Completion: %{y:.1f}%<br>Completed: %{customdata[0]:,}<br>Incomplete: %{customdata[1]:,}<br>Records: %{customdata[2]:,}<extra></extra>')
        fig.update_layout(showlegend=False)
        st.plotly_chart(style(fig),use_container_width=True)
    cols=['num_passengers','purchase_lead','length_of_stay','flight_duration','wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']
    heat=df.groupby('cluster')[cols].mean()
    heat.columns=[label(x) for x in cols]
    heat.index=[f'Segment {x}' for x in heat.index]
    fig=px.imshow(heat,aspect='auto',color_continuous_scale='Teal',labels={'x':'Characteristic','y':'Segment','color':'Mean'},title='Segment characteristics · original units')
    st.plotly_chart(style(fig),use_container_width=True)
    st.caption('Means use days, hours, passengers, and proportions (0–1) for service requests. Values have different units.')
    coords=pca_sample(processed).join(df[['cluster']],how='inner').dropna()
    if len(coords):
        coords['segment']=coords.cluster.astype(int).map(lambda x:f'Segment {x}')
        fig=px.scatter(coords,x='PC1',y='PC2',color='segment',color_discrete_map=color_map,title='Segment map · reproducible sample',opacity=.6)
        fig.update_traces(marker=dict(size=5))
        st.plotly_chart(style(fig),use_container_width=True)
        st.caption('PCA is fitted on a fixed sample of the project’s clustering inputs, excluding booking completion. Filtered views show the matching sampled records.')
    selected=st.selectbox('Explore a segment',sorted(df.cluster.unique()),format_func=lambda x:f'Segment {x}')
    s=df[df.cluster==selected]
    st.markdown(f'**Segment {selected}** · {len(s):,} booking records · {s.booking_complete.mean():.1%} completion')
    x,y,z=st.columns(3)
    x.write(f"Average passengers: **{s.num_passengers.mean():.2f}**")
    x.write(f"Average lead time: **{s.purchase_lead.mean():.1f} days**")
    x.write(f"Average stay: **{s.length_of_stay.mean():.1f} days**")
    y.write(f"Average flight duration: **{s.flight_duration.mean():.1f} hours**")
    y.write(f"Leading sales channel: **{s.sales_channel.mode().iloc[0]}**")
    y.write(f"Leading trip type: **{s.trip_type.mode().iloc[0]}**")
    for col in ['wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']:
        z.write(f"{label(col)}: **{s[col].mean():.1%}**")
