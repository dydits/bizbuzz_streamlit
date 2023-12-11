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
        (3) V_Articles_GOV_TRANS : 베트남 중앙 & 지방 정부부처 <br>
        (4) V_Articles_LOCAL_TRANS : 베트남 주요 언론매체
    </p>
    """, unsafe_allow_html=True)


# 스트림릿 버튼을 추가하고 클릭 시 세 파일을 순차적으로 실행
if st.button("Run BIZBUZZ VIETNAM"):
    # 각 파일의 경로를 지정하고 순차적으로 실행
    for file_name in ['US_All_Govern.py', 'US_All_DefenseIndustry.py', 'US_All_Local.py']:
        with open(file_name, 'r') as file:
            exec(file.read())


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