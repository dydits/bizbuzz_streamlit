import streamlit as st 

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

st.subheader("USA")

st.markdown("""
    <style>
    .small-font {
        font-size:13px;  # 원하는 글자 크기로 조절
    }
    </style>
    <p class="small-font"> 
            : CA - NJ - NY - TX - VA - MD - GA - WA - NC 9개의 주 선정 </p>
    """, unsafe_allow_html=True)

# 추가할 Markdown 텍스트
st.markdown("""
    <p class="small-font">
        : USA Articles 종류 <br>
        (1) Articles_GOV : 미국 주정부, 연방정부 <br>
        (2) Articles_LOCAL : 위 9개 주 지역언론 <br>
        (3) Aricles_EXTRA : 방산업체 & NASA
    </p>
    """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# 엑셀 파일 경로
excel_file_path = '/Users/dydit/Desktop/us_address_all.xlsx'

# 엑셀 파일 읽어오기
df = pd.read_excel(excel_file_path, header=None)

# 컬럼 두 개 생성
col1, col2 = st.columns(2)

# 첫 번째 컬럼
with col1:
    # Scatter_geo를 사용하여 첫 번째 그래프 생성
    fig1 = px.scatter_geo(df,
                         lat=df.iloc[:, 1].tolist(),
                         lon=df.iloc[:, 2].tolist(),
                         scope='usa',
                         title='DETAILED USA MAP')
    st.plotly_chart(fig1, use_container_width=True)

# 두 번째 컬럼
with col2:
    # Scatter_geo를 사용하여 두 번째 그래프 생성
    fig2 = px.scatter_geo(df,
                         lat=df.iloc[:, 1].tolist(),
                         lon=df.iloc[:, 2].tolist(),
                         scope='usa',
                         title='COLORED USA MAP')

    # 주별 핀의 개수 계산하여 Choropleth map 생성
    pin_counts = df.iloc[:, 3].value_counts().reset_index()
    pin_counts.columns = ['State', 'Pin Count']
    choropleth_fig = px.choropleth(pin_counts,
                                   locations='State',
                                   locationmode='USA-states',
                                   color='Pin Count',
                                   scope='usa',
                                   title='Choropleth USA Map - Pin Counts',
                                   color_continuous_scale='YlOrRd')

    # 두 번째 그래프에 Choropleth map 추가
    for trace in choropleth_fig.data:
        fig2.add_trace(trace)

    st.plotly_chart(fig2, use_container_width=True)

if st.button("Run BIZBUZZ USA"):
    with open('/Users/dydit/Desktop/Real_Final_US.py', 'r') as file:
        exec(file.read())


# 오늘 날짜를 '월일' 형식으로 가져오기
from datetime import datetime
import streamlit as st
import pandas as pd
today_str = datetime.now().strftime("%m%d") 


if st.button("Final Articles (오늘자 총 기사 중 한국기업 언급된 기사)"):
    df_final_articles = pd.read_csv(f'Final Articles_{today_str}.csv')
    st.dataframe(df_final_articles)


# 사이드바 제목 설정
st.sidebar.title('USA Articles 📰')

# select_multi_species
select_multi_species = st.sidebar.multiselect(
    '확인하고 싶은 항목을 선택하세요. (복수선택가능)',
    ['Articles_GOV','Articles_LOCAL','Articles_EXTRA']
)

# 선택된 각 항목에 대한 데이터프레임 표시
for article_type in select_multi_species:
    if article_type == 'Articles_GOV':
        df_final_articles = pd.read_csv(f'Articles_GOV_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'Articles_LOCAL':
        df_final_articles = pd.read_csv(f'Articles_LOCAL_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'Articles_EXTRA':
        df_final_articles = pd.read_csv(f'Articles_EXTRA_{today_str}.csv')
        st.dataframe(df_final_articles)