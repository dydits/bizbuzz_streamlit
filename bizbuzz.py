import streamlit as st 
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

# 페이지 헤더, 서브헤더 제목 설정 
st.header("Welcome to BIZBUZZ!📰")
st.subheader("streamlit lets go")

# 페이지 컬럼 분할
cols = st.columns((1, 1, 2))
# cols[0].metric("10/11", "15 °C", "2") 
# 첫 번째 숫자 ; 소제목 느낌으로 구현 
# 두 번째 숫자 ; 소제목 안에 들어갈 내용 
# 마지막 숫자 ; 양수기입시 녹색으로 위쪽 화살표 자동구현, 음수기입시 빨간색으로 아래쪽 화살표 자동구현
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

# 라인 그래프 데이터 생성(with. Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)