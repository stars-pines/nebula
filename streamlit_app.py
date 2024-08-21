import streamlit as st

from web_pages import planning_cal_cn, planning_cal_en

# Set Wide Surface
st.set_page_config(page_title="Planning of Cost",
                   page_icon="🔥",
                   layout='wide',
                   initial_sidebar_state="expanded", )
pages = {
    'English': planning_cal_en,
    'Chinese': planning_cal_cn
}
st.logo('resource/images/common/happy.png')
with st.sidebar:
    sc1_1, sc1_2 = st.columns(2)
    with sc1_1:
        st.subheader('🤖:rainbow[**Language**]')
    with sc1_2:
        selected_page = st.selectbox('Language', options=list(pages.keys()), label_visibility='collapsed')

page = pages[selected_page]
page.app()
