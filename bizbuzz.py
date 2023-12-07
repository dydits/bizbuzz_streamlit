import streamlit as st 
import pandas as pd
import numpy as np
import datetime

from time import sleep

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

# 페이지 헤더, 서브헤더 제목 설정 
#st.header("Welcome to BIZBUZZ! 📰")
#st.subheader("SNU Bigdata Fintech 7기 _ 조선비즈 캡스톤")

st.title('Welcome to BIZBUZZ!')

# subheader 스타일 조정
st.markdown("""
    <style>
    .small-font {
        font-size:17px;  # 원하는 글자 크기로 조절
        font-weight: bold;
    }
    </style>
    <p class="small-font">SNU Bigdata Fintech 7기 _ 조선비즈 캡스톤</p>
    """, unsafe_allow_html=True)


# 페이지 컬럼 분할
cols = st.columns(3)

# cols[0] : 오늘 날짜 표시
today = datetime.date.today()
# 오늘 날짜를 포맷팅 (예: 2023-12-06)
formatted_date = today.strftime("%Y-%m-%d")
cols[0].metric(label="📅 오늘 날짜", value=formatted_date)

# cols[1] : 디지털 시계 형식의 현재 시간 표시
current_time = datetime.datetime.now()
# 현재 시간을 디지털 시계 형식으로 포맷팅 (예: 15:30:45)
formatted_time = current_time.strftime("%H:%M:%S")
cols[1].metric(label="⏰ 현재 시간", value=formatted_time)

# cols[2] : 오늘자 기사 개수 -- 실제 데이터 연동 필요
num_articles = 1255  # 오늘자 기사 개수
cols[2].metric(label="🗞️ 오늘자 총 기사 개수", value=f"{num_articles}개")

# 아래쪽에는 개인적으로 NER 탭 만들어서 넣는거 좋을듯

# "🍀 한국기업명 포함된 기사 LIST" 소제목, 기사 개수 표시 -- 실제 데이터 연동 필요
st.markdown("""
    <style>
    .article-title {
        font-size:15px;  # 소제목 글자 크기
        font-weight: normal;
        margin-bottom: 0.5em;  # 소제목 아래 마진 조절
    }
    .article-count {
        font-size:13px;  # 기사 개수 글자 크기
        margin-bottom: 1em;  # 기사 개수 아래 마진 조절
    }
    </style>
    <h2 class="article-title">🍀 한국기업명 포함된 기사 LIST</h2>
    <p class="article-count">기사 개수: 2개</p>
    """, unsafe_allow_html=True)
