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

##################################################### Above, extra work ###################################################

# 스트림릿 버튼을 추가하고 클릭 시 세 파일을 순차적으로 실행
if st.button("Run BIZBUZZ USA"):
    # 각 파일의 경로를 지정하고 순차적으로 실행
    for file_name in ['US_All_Govern.py', 'US_All_DefenseIndustry.py', 'US_All_Local.py']:
        with open(file_name, 'r') as file:
            exec(file.read())





















from datetime import datetime
import streamlit as st
import pandas as pd

today_str = datetime.now().strftime("%y%m%d")  # 예: '231211'


if st.button("Final Articles (오늘자 총 기사 중 한국기업 언급된 기사)"):
    df_final_articles = pd.read_csv(f'US_Final Selected Articles_{today_str}.csv')
    st.dataframe(df_final_articles)

# 사이드바 제목 설정
st.sidebar.title('USA Articles 📰')

# select_multi_species
select_multi_species = st.sidebar.multiselect(
    '확인하고 싶은 항목을 선택하세요. (복수선택가능)',
    ['Articles_GOV', 'Articles_LOCAL', 'Articles_EXTRA']
)

# 선택된 각 항목에 대한 데이터프레임 표시
for article_type in select_multi_species:
    if article_type == 'Articles_GOV':
        # 파일명을 'US_Government Articles_오늘날짜.csv'로 변경
        df_articles = pd.read_csv(f'US_Government Articles_{today_str}.csv')
        st.dataframe(df_articles)

    elif article_type == 'Articles_LOCAL':
        # 파일명을 'US_Local Articles_오늘날짜.csv'로 변경
        df_articles = pd.read_csv(f'US_Local Articles_{today_str}.csv')
        st.dataframe(df_articles)

    elif article_type == 'Articles_EXTRA':
        # 파일명을 'US_Defense Industry Articles_오늘날짜.csv'로 변경
        df_articles = pd.read_csv(f'US_Defense Industry Articles_{today_str}.csv')
        st.dataframe(df_articles)