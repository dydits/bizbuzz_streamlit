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

# 페이지헤더, 서브헤더
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
import pandas as pd
from datetime import datetime
today_str = datetime.now().strftime("%y%m%d")  # 예: '231211'
US = pd.read_csv(f'US_All Articles_{today_str}.csv')
VIETNAM_1 = pd.read_csv(f'V_Articles_GOV_{today_str}.csv')
VIETNAM_2 = pd.read_csv(f'V_Articles_LOCAL_{today_str}.csv')
INDONESIA_1 = pd.read_csv(f'IN_Articles_GOV_{today_str}.csv')
INDONESIA_2 = pd.read_csv(f'IN_Articles_LOCAL_{today_str}.csv')
num_articles = len(US) + len(VIETNAM_1) + len(VIETNAM_2) + len(INDONESIA_1) + len(INDONESIA_2)
cols[2].metric(label="🗞️ 오늘자 총 기사 개수", value=f"{num_articles}개")


from datetime import datetime
import streamlit as st
import pandas as pd

def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        st.error(f"File '{file_name}' not found.")
        return None

def display_file_with_header(file_name, header):
    st.markdown(f"#### {header}")
    data = load_data(file_name)
    if data is not None:
        st.write(data)

def main():
    today_str = datetime.now().strftime("%y%m%d")  # 예: '231211'

    # 미국 데이터 파일 불러오기
    us_file = f"US_Final Selected Articles_{today_str}.csv"
    display_file_with_header(us_file, "US_Final_Selected")

    # 베트남 데이터 파일 불러오기
    v_file = f"V_Final Articles_{today_str}.csv"
    display_file_with_header(v_file, "V_Final_Selected")

    # 인도 데이터 파일 불러오기
    in_file = f"IN_Final Articles_{today_str}.csv"
    display_file_with_header(in_file, "IN_Final_Selected")

if __name__ == "__main__":
    main()
