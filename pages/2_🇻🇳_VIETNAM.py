import streamlit as st 

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

st.subheader("VIETNAM")


# 추가할 Markdown 텍스트
st.markdown("""
    <style>
    .small-font {
        font-size:13px;  # 원하는 글자 크기로 조절
    }
    </style>
    <p class="small-font">
        : VIETNAM Articles 종류 <br>
        (1) V_Articles_GOV : 베트남 중앙 & 지방 정부부처   <br>
        (2) V_Articles_LOCAL : 베트남 주요 언론매체 <br>
        (3) V_Articles_GOV_TRANS : 베트남 중앙 & 지방 정부부처 (한국기업명 추출 & 번역 포함) <br>
        (4) V_Articles_LOCAL_TRANS : 베트남 주요 언론매체 (한국기업명 추출 & 번역 포함)
    </p>
    """, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import plotly.express as px

# 엑셀 파일 경로
# csv_file_path = '/Users/dydit/Desktop/sampled_vietnam_trade_offices.csv'
csv_file_path = 'https://raw.githubusercontent.com/dydits/bizbuzz_streamlit/main/maps%20csv%20files/sampled_vietnam_trade_offices.csv'

# 엑셀 파일 읽어오기
df = pd.read_csv(csv_file_path)

# 컬럼 두 개 생성
col1, col2 = st.columns(2)

# 첫 번째 컬럼
with col1:
    # Scatter_geo를 사용하여 첫 번째 그래프 생성
    # 베트남만 따로 보여주는 Scatter_geo 그래프 생성
    fig1 = px.scatter_geo(df, lat='위도', lon='경도', hover_name='기업명(국문)', 
                     scope='asia', 
                     center={'lat': 14.0583, 'lon': 108.2772}, # 베트남 중심 좌표
                     title='Detailed VIETNAM Map')

    # 지도의 범위를 베트남에만 제한
    fig1.update_geos(
    visible=False, showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
    )   
    fig1.update_geos(
    lataxis_range=[8, 23], # 베트남의 위도 범위
    lonaxis_range=[102, 110] # 베트남의 경도 범위
)
    st.plotly_chart(fig1, use_container_width=True)

with col2: 
    df_count = df.groupby(['위도', '경도']).size().reset_index(name='counts')

    fig = px.scatter_geo(df_count, lat='위도', lon='경도', size='counts',
                     hover_name='counts', scope='asia',
                     center={'lat': 14.0583, 'lon': 108.2772}, # 베트남 중심 좌표
                     title='Colored VIETNAM Map', color='counts',
                     color_continuous_scale=px.colors.sequential.Viridis)
    
    # 지도의 범위를 베트남에만 제한
    fig.update_geos(
        visible=False, showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
        )
    fig.update_geos(
        lataxis_range=[8, 23], # 베트남의 위도 범위
        lonaxis_range=[102, 110] # 베트남의 경도 범위
        )
    
    fig.update_layout(coloraxis_colorbar=dict(
    title="Number of Offices",
    tickvals=df_count['counts'],
    ticktext=df_count['counts']
    ))

    st.plotly_chart(fig)


import subprocess
# 함수
def run_python_files():
    file_paths = [
        '/Users/dydit/Desktop/vietnam_today_final.py'
    ]

    for file_path in file_paths:
        result = subprocess.run(['python', file_path], stdout=subprocess.PIPE)
        st.text(f"{file_path} 실행 결과:")
        st.text(result.stdout.decode())

# 스트림릿 버튼 추가
if st.button('Run BIZBUZZ VIETNAM'):
    run_python_files()


from datetime import datetime
import streamlit as st
import pandas as pd

today_str = datetime.now().strftime("%y%m%d")  # 예: '231211'

if st.button("Final Articles (오늘자 총 기사 중 한국기업 언급된 기사)"):
    df_final_articles = pd.read_csv(f'V_Final Articles_{today_str}.csv')
    st.dataframe(df_final_articles)

# 사이드바 제목 설정
st.sidebar.title('VIETNAM Articles 📰')

# select_multi_species
select_multi_species = st.sidebar.multiselect(
    '확인하고 싶은 항목을 선택하세요. (복수선택가능)',
    ['V_Articles_GOV', 'V_Articles_LOCAL', 'V_Articles_GOV_TRANS', 'V_Articles_LOCAL_TRANS']
)

# 선택된 각 항목에 대한 데이터프레임 표시
for article_type in select_multi_species:
    if article_type == 'V_Articles_GOV':
        df_final_articles = pd.read_csv(f'V_Articles_GOV_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'V_Articles_LOCAL':
        df_final_articles = pd.read_csv(f'V_Articles_LOCAL_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'V_Articles_GOV_TRANS':
        df_final_articles = pd.read_csv(f'V_Articles_GOV_TRANS_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'V_Articles_LOCAL_TRANS':
        df_final_articles = pd.read_csv(f'V_Articles_LOCAL_TRANS_{today_str}.csv')
        st.dataframe(df_final_articles)