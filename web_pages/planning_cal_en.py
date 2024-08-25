import streamlit as st
import streamlit_antd_components as sac


def app():
    st.balloons()
    with st.sidebar:
        st.image('resource/images/en/store_name.png', output_format='PNG', use_column_width='auto')
        st.subheader(':rainbow[**Our Aim**]', divider='rainbow')
        st.markdown('1️⃣:blue[**Enhance your profits**] ')
        st.markdown('2️⃣:blue[**Allowing you to save more effort**] ')

        st.subheader(':rainbow[**To help you**]', divider='rainbow')
        st.link_button(':rainbow[**GitHub**]😆:rainbow[**Welcome to communicate**]',
                       url='https://github.com/stars-pines/nebula/issues')
        st.link_button(':rainbow[**YouTube**]😃:rainbow[**Our videos**]',
                       url='https://www.youtube.com/@qingjing-b2z')
        with st.expander(':blue[**Other contact information**]',expanded=True,icon='✅'):
            st.markdown(':rainbow[**Email: stars-pine@qq.com**] ')
            st.markdown(':rainbow[**QQ: 2665073539**] ')
            sc0_1, sc0_2 = st.columns(2)
            with sc0_1:
                st.markdown(':rainbow[**WeChat：**] ')
                st.image('resource/images/en/WeChat_QR.png', output_format='PNG', use_column_width='auto')
            with sc0_2:
                st.markdown(':rainbow[**TikTok：**] ')
                st.image('resource/images/en/tiktok_QR.png', output_format='PNG', use_column_width='auto')

    st.image('resource/images/en/title.png', output_format='PNG', use_column_width='auto')
    sc1_1, sc1_2 = st.columns(2)
    with sc1_1:
        with st.container():
            st.header(':rainbow[Give you the calculation tools]💻', divider=True)
            st.markdown('1️⃣:rainbow[**Quickly figure out the best solution**]📜')
            st.markdown('2️⃣:rainbow[**provides energy flow graphs - to help you understand data movements**]😆')
            st.markdown('3️⃣:rainbow[**The program runs only locally**]😉')
            st.markdown('4️⃣:rainbow[**Data will not be uploaded - please feel free to use it**]📘')
            st.markdown('5️⃣:rainbow[**Use the most common office tool - Smooth transition**]💹')
    with sc1_2:
        st.image('resource/images/en/cooperation_method.png', output_format='PNG', use_column_width='auto')

    st.title(':rainbow[Scope of service-en] :sunglasses:')

    tab_text = sac.tabs([
        sac.TabsItem(label='Optimize purchasing cost', icon='cart-check-fill'),
        sac.TabsItem(label='Optimize production cost', icon='rocket-takeoff'),
        sac.TabsItem(label='Optimize transportation costs', icon='bus-front'),
    ], align='center', size='xl', return_index=True)
    if tab_text == 0:
        st.image('resource/images/en/cost_optimization_path.png', output_format='auto', use_column_width='auto')

        st.header(':blue[Bring help]📈', divider='rainbow')
        sc1, sc2 = st.columns(2)
        with sc1:
            st.subheader('1️⃣:rainbow[**Make money**]')
            st.image('resource/images/en/gain_profit_increase.png', output_format='auto', use_column_width='auto')
        with sc2:
            st.subheader('2️⃣:rainbow[**simplify matters**]')
            st.image('resource/images/en/gain_reduces_time.png', output_format='auto', use_column_width='auto')

        st.header(':blue[Operation demonstration]🖥️', divider='rainbow')
        st.subheader('1️⃣:rainbow[**Easy to use steps.**]')
        st.image('resource/images/en/instructions.png')
        st.subheader(
            '2️⃣:rainbow[**The provided Sankey diagram will help with better decision-making. The following figure is an example for reference only.**]')
        st.image('resource/images/en/sankey.png')

    if tab_text == 1:
        st.image('resource/images/en/coming_soon.png', output_format='auto', use_column_width='auto')

    if tab_text == 2:
        st.image('resource/images/en/coming_soon.png', output_format='auto', use_column_width='auto')


if __name__ == "__main__":
    app()
