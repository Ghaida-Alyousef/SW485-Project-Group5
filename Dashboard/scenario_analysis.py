import streamlit as st

def render_scenario(raw):
    st.subheader('Scenario analysis')
    st.info('Live predictions are unavailable: the fitted Random Forest and its fitted preprocessing artifacts have not been supplied. The controls below prepare a booking profile; they do not generate a prediction.')
    st.caption('The selected Random Forest uses a 0.19 decision threshold for class 1 in the saved run. Probability is distinct from model accuracy.')
    if st.button('Reset scenario'):
        for key in list(st.session_state):
            if key.startswith('scenario_'): del st.session_state[key]
        st.rerun()
    profile = {}
    a,b,c = st.columns(3)
    numeric = [('num_passengers','Passengers',1),('purchase_lead','Purchase lead time (days)',1),('length_of_stay','Length of stay (days)',1),('flight_hour','Flight hour',1),('flight_duration','Flight duration (hours)',0.01)]
    for i,(col,title,step) in enumerate(numeric):
        lo,hi = raw[col].min(),raw[col].max()
        default = raw[col].median()
        if step == 1: lo,hi,default = int(lo),int(hi),int(default)
        else: lo,hi,default = float(lo),float(hi),float(default)
        with [a,b,c][i%3]: profile[col] = st.slider(title,lo,hi,default,step=step,key='scenario_'+col)
    for i,col in enumerate(['sales_channel','trip_type','flight_day','booking_origin','route']):
        opts = sorted(raw[col].dropna().unique().tolist()); default = opts.index(raw[col].mode()[0])
        with [a,b,c][i%3]: profile[col] = st.selectbox(col.replace('_',' ').title(),opts,index=default,key='scenario_'+col)
    for i,col in enumerate(['wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']):
        with [a,b,c][i]: profile[col] = st.checkbox(col.replace('wants_','').replace('_',' ').title(), value=bool(raw[col].mode()[0]), key='scenario_'+col)
    st.session_state['integration_payload'] = {'booking_profile':profile, 'completion_probability':None, 'predicted_outcome':None, 'decision_threshold':0.19, 'segment_profile':None}
    st.caption('Prediction, confidence, baseline comparison, and scenario segment assignment require the team’s fitted artifacts. The integration payload is prepared without generating AI responses.')
