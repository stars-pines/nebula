import streamlit as st
import streamlit_antd_components as sac

def app():
    st.balloons()
    with st.sidebar:
        st.image('resource/images/cn/store_name.png', output_format='PNG', use_column_width='auto')
        st.subheader(':rainbow[**我们的宗旨**]', divider='rainbow')
        st.markdown('1️⃣:blue[**让您利润更高**] ')
        st.markdown('2️⃣:blue[**让您更省事**] ')

        st.subheader(':rainbow[**提供给您帮助**]', divider='rainbow')
        with st.expander(':blue[**其他联系方式**]', expanded=True, icon='✅'):
            st.markdown(':rainbow[**邮箱: stars-pine@qq.com**] ')
            st.markdown(':rainbow[**QQ: 2665073539**] ')
            sc0_1, sc0_2 = st.columns(2)
            with sc0_1:
                st.markdown(':rainbow[**微信：**] ')
                st.image('resource/images/cn/WeChat_QR.png', output_format='PNG', use_column_width='auto')
            with sc0_2:
                st.markdown(':rainbow[**抖音：**] ')
                st.image('resource/images/cn/tiktok_QR.png', output_format='PNG', use_column_width='auto')

    sc2_1, sc2_2 = st.columns(2)
    with sc2_1:
        sac.alert(label='或许是一个新的提升利润的思路', banner=True, icon=True, closable=True)
    with sc2_2:
        st.link_button(':rainbow[**GitHub-Discussions**]😆:rainbow[**快捷联系**]',
                       url='https://github.com/stars-pines/nebula/discussions',
                       help='请描述您的行业、采购方式', use_container_width=True)

    st.image('resource/images/cn/title.png', output_format='PNG', use_column_width='auto')
    sc1_1, sc1_2 = st.columns(2)
    with sc1_1:
        with st.container():
            st.header(':rainbow[提供给你计算工具]💻', divider=True)
            st.markdown('1️⃣:rainbow[**快速算出最优方案，可配合Excel使用**]💹')
            st.markdown('3️⃣:rainbow[**程序仅在你本地运行，数据不会上传 - 放心使用**]😉')

            st.header(':rainbow[适用企业]🏣', divider=True)
            st.markdown('1️⃣:rainbow[**涉及采购原材料进行加工的加工型企业**]🏭')
            st.markdown('3️⃣:rainbow[**需要精准控制成本的公司**]💰')
    with sc1_2:
        st.image('resource/images/cn/cooperation_method.png', output_format='PNG', use_column_width='auto')

    st.title(':rainbow[服务范围-cn] :sunglasses:')

    tab_text = sac.tabs([
        sac.TabsItem(label='采购优化', icon='cart-check-fill'),
        sac.TabsItem(label='生产制造优化', icon='rocket-takeoff'),
        sac.TabsItem(label='运输优化', icon='bus-front'),
    ], align='center', size='xl', return_index=True)
    if tab_text == 0:
        st.image('resource/images/cn/cost_optimization_path.png', output_format='auto', use_column_width='auto')

        st.header(':blue[带来的帮助]📈', divider='rainbow')
        sc1, sc2 = st.columns(2)
        with sc1:
            st.subheader('1️⃣:rainbow[**赚钱**]')
            st.image('resource/images/cn/gain_profit_increase.png', output_format='auto', use_column_width='auto')
        with sc2:
            st.subheader('2️⃣:rainbow[**省事**]')
            st.image('resource/images/cn/gain_reduces_time.png', output_format='auto', use_column_width='auto')


        st.header(':blue[使用演示]🖥️', divider='rainbow')

        st.subheader('1️⃣:rainbow[**使用过程简单**]')
        st.image('resource/images/cn/instructions.png')

        st.subheader('2️⃣:rainbow[**所提供的桑基图将帮助你更好做规划。下图为示例，仅供参考。**]')
        st.image('resource/images/cn/sankey.png')

    if tab_text == 1:
        st.image('resource/images/cn/coming_soon.png', output_format='auto', use_column_width='auto')

    if tab_text == 2:
        st.image('resource/images/cn/coming_soon.png', output_format='auto', use_column_width='auto')


if __name__ == "__main__":
    app()
