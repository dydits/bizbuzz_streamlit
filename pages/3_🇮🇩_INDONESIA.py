import streamlit as st 

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

st.subheader("INDONESIA")


# 추가할 Markdown 텍스트
st.markdown("""
    <style>
    .small-font {
        font-size:13px;  # 원하는 글자 크기로 조절
    }
    </style>
    <p class="small-font">
        : INDONESIA Articles 종류 <br>
        (1) IN_Articles_GOV : 인도네시아 중앙 & 지방 정부부처   <br>
        (2) IN_Articles_LOCAL : 인도네시아 주요 언론매체 <br>
        (3) IN_Articles_GOV_TRANS : 인도네시아 중앙 & 지방 정부부처 (한국기업명 추출 & 번역 포함) <br>
        (4) IN_Articles_LOCAL_TRANS : 인도네시아 주요 언론매체 (한국기업명 추출 & 번역 포함)
    </p>
    """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import plotly.express as px

# 엑셀 파일 경로
csv_file_path = '/Users/dydit/Desktop/sampled_Indonesia_trade_offices.csv'

# 엑셀 파일 읽어오기
df = pd.read_csv(csv_file_path)

# 컬럼 두 개 생성
col1, col2 = st.columns(2)

# 첫 번째 컬럼
with col1:
    # 인도네시아 지도를 보여주는 Scatter_geo 그래프 생성
    indonesia_fig = px.scatter_geo(df, lat='위도', lon='경도', hover_name='기업명(국문)',
                                   scope='asia',
                                   center={'lat': -0.7893, 'lon': 113.9213}, # 인도네시아 중심 좌표
                                   title='Detailed INDONESIA Map')

    # 지도의 범위를 인도네시아에만 제한
    indonesia_fig.update_geos(
        visible=False, showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
    )
    indonesia_fig.update_geos(
        lataxis_range=[-11, 6], # 인도네시아의 위도 범위
        lonaxis_range=[95, 141] # 인도네시아의 경도 범위
    )



    # 스트림릿에 그래프 표시
    st.plotly_chart(indonesia_fig)

# 두 번째 컬럼
with col2:
    # 각 위치에 있는 핀의 개수 계산
    location_counts = df.groupby(['위도', '경도']).size().reset_index(name='counts')

    # 인도네시아 지도를 보여주는 Scatter_geo 그래프 생성
    indonesia_fig = px.scatter_geo(location_counts, lat='위도', lon='경도', size='counts', hover_name='counts',
                                   scope='asia',
                                   center={'lat': -0.7893, 'lon': 113.9213}, # 인도네시아 중심 좌표
                                   title='Colored INDONESIA Map')

    # 지도의 범위를 인도네시아에만 제한
    indonesia_fig.update_geos(
        visible=False, showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
    )
    indonesia_fig.update_geos(
        lataxis_range=[-11, 6], # 인도네시아의 위도 범위
        lonaxis_range=[95, 141] # 인도네시아의 경도 범위
    )

    # 스트림릿에 그래프 표시
    st.plotly_chart(indonesia_fig)

import subprocess
# 함수
def run_python_files():
    file_paths = [
        '/Users/dydit/Desktop/indonesia_today_final.py'
    ]

    for file_path in file_paths:
        result = subprocess.run(['python', file_path], stdout=subprocess.PIPE)
        st.text(f"{file_path} 실행 결과:")
        st.text(result.stdout.decode())

# 스트림릿 버튼 추가
if st.button('Run BIZBUZZ INDONESIA'):
    run_python_files()


from datetime import datetime
import streamlit as st
import pandas as pd

today_str = datetime.now().strftime("%y%m%d")  # 예: '231211'

if st.button("Final Articles (오늘자 총 기사 중 한국기업 언급된 기사)"):
    df_final_articles = pd.read_csv(f'IN_Final Articles_{today_str}.csv')
    st.dataframe(df_final_articles)

# 사이드바 제목 설정
st.sidebar.title('INDONESIA Articles 📰')

# select_multi_species
select_multi_species = st.sidebar.multiselect(
    '확인하고 싶은 항목을 선택하세요. (복수선택가능)',
    ['IN_Articles_GOV', 'IN_Articles_LOCAL', 'IN_Articles_GOV_TRANS', 'IN_Articles_LOCAL_TRANS']
)

# 선택된 각 항목에 대한 데이터프레임 표시
for article_type in select_multi_species:
    if article_type == 'IN_Articles_GOV':
        df_final_articles = pd.read_csv(f'IN_Articles_GOV_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'IN_Articles_LOCAL':
        df_final_articles = pd.read_csv(f'IN_Articles_LOCAL_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'IN_Articles_GOV_TRANS':
        df_final_articles = pd.read_csv(f'IN_Articles_GOV_TRANS_{today_str}.csv')
        st.dataframe(df_final_articles)

    elif article_type == 'IN_Articles_LOCAL_TRANS':
        df_final_articles = pd.read_csv(f'IN_Articles_LOCAL_TRANS_{today_str}.csv')
        st.dataframe(df_final_articles)