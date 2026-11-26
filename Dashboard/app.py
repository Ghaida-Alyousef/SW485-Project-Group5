import streamlit as st
import plotly.express as px
from data_loader import load_data, load_importance
from visual_analytics import style, rate_chart, label, TEAL
from scenario_analysis import render_scenario
from cluster_visualization import render_clusters

st.set_page_config(page_title='CCO Flight Booking Advisory',page_icon='✈',layout='wide')
st.markdown("""<style>
.stApp {background:#f3f6fa;color:#153252}
[data-testid="stSidebar"] {background:#122d4b}
[data-testid="stSidebar"] * {color:#fff}
div[data-testid="stMetric"] {background:white;border:1px solid #e4ebf1;border-top:3px solid #009b98;border-radius:10px;padding:16px}
div[data-testid="stMetricLabel"] {color:#536a7e}
h1,h2,h3 {color:#153252}
.block-container {padding-top:2rem;max-width:1500px}
</style>""",unsafe_allow_html=True)
st.title('CCO Flight Booking Advisory')
st.caption('EXECUTIVE DECISION SUPPORT & VISUAL ANALYTICS')
try:
    raw, processed=load_data()
except (FileNotFoundError,ValueError,KeyError) as exc:
    st.error(f'Data validation failed: {exc}')
    st.stop()

with st.sidebar:
    st.markdown('### Commercial analytics')
    page=st.radio('Navigate',['Executive Overview','Scenario Analysis','Key Booking Drivers','Passenger Segmentation'])
    st.divider()
    st.markdown('### Filter booking records')
    if st.button('Reset filters',use_container_width=True):
        for key in list(st.session_state):
            if key.startswith('filter_'): del st.session_state[key]
        st.rerun()
    filtered=raw.copy()
    for col,title in [('sales_channel','Sales channel'),('trip_type','Trip type'),('booking_origin','Booking origin'),('route','Route'),('flight_day','Flight day'),('cluster','Passenger segment')]:
        opts=sorted(raw[col].dropna().unique().tolist())
        selected=st.multiselect(title,opts,key='filter_'+col,format_func=(lambda x:f'Segment {x}') if col=='cluster' else str)
        if selected: filtered=filtered[filtered[col].isin(selected)]
    lo,hi=int(raw.purchase_lead.min()),int(raw.purchase_lead.max())
    lead=st.slider('Purchase lead time (days)',lo,hi,(lo,hi),key='filter_lead')
    filtered=filtered[filtered.purchase_lead.between(*lead)]
    st.caption(f'{len(filtered):,} of {len(raw):,} booking records')
if page == 'Scenario Analysis':
    render_scenario(raw)
elif filtered.empty:
    st.warning('No booking records match these filters. Adjust or reset the filters to continue.')
elif page == 'Executive Overview':
    st.subheader('Executive overview')
    st.caption('Historical booking records · filters apply to every metric and chart below')
    n=len(filtered); completed=int(filtered.booking_complete.sum())
    a=st.columns(6)
    for c,title,value in zip(a,['Booking records','Completed','Completion rate','Incomplete','Incomplete rate','Segments'],[f'{n:,}',f'{completed:,}',f'{completed/n:.1%}',f'{n-completed:,}',f'{(n-completed)/n:.1%}',f'{filtered.cluster.nunique()}']): c.metric(title,value)
    st.caption(f'Average purchase lead time: {filtered.purchase_lead.mean():.1f} days')
    a,b=st.columns(2)
    with a:
        counts=filtered.booking_complete.value_counts().rename_axis('outcome').reset_index(name='records')
        counts['outcome']=counts.outcome.map({0:'Incomplete',1:'Completed'})
        fig=px.pie(counts,names='outcome',values='records',hole=.65,title='Booking completion distribution',color='outcome',color_discrete_map={'Completed':TEAL,'Incomplete':'#b8c9d7'})
        st.plotly_chart(style(fig),use_container_width=True)
    with b: st.plotly_chart(rate_chart(filtered,'sales_channel','Completion by sales channel'),use_container_width=True)
    a,b=st.columns(2)
    with a: st.plotly_chart(rate_chart(filtered,'trip_type','Completion by trip type'),use_container_width=True)
    with b: st.plotly_chart(rate_chart(filtered,'purchase_lead','Completion by purchase lead time',True),use_container_width=True)
    st.plotly_chart(rate_chart(filtered,'booking_origin','Completion by booking origin · ten largest'),use_container_width=True)
elif page == 'Key Booking Drivers':
    st.subheader('Key booking drivers')
    st.caption('Global model importance comes from the saved Random Forest evaluation and does not change with filters. Historical relationships below reflect the selected records; association does not establish causation.')
    try:
        imp=load_importance().sort_values('permutation_importance_mean').tail(15).copy()
        imp['name']=imp.feature.map(label)
        fig=px.bar(imp,x='permutation_importance_mean',y='name',orientation='h',title='Random Forest · held-out permutation importance',labels={'permutation_importance_mean':'Mean decrease in ROC-AUC','name':'Feature'},color_discrete_sequence=[TEAL])
        st.plotly_chart(style(fig),use_container_width=True)
    except (FileNotFoundError,KeyError) as exc: st.warning(f'Model importance unavailable: {exc}')
    choices=['purchase_lead','sales_channel','trip_type','flight_duration','length_of_stay','wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']
    feature=st.selectbox('Explore observed booking behavior',choices,format_func=label)
    st.plotly_chart(rate_chart(filtered,feature,'Observed completion rate',feature in ['purchase_lead','flight_duration','length_of_stay']),use_container_width=True)
else:
    render_clusters(filtered,processed)
