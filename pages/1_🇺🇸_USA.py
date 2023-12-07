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
    <p class="small-font"> : CA - NJ - NY - TX - VA - MD - GA - WA - NC 9개의 주 선정 </p>
    """, unsafe_allow_html=True)

# USA detailed map 넣기 
import streamlit as st
import pandas as pd
import plotly.express as px

# 데스크탑에 있는 엑셀 파일 경로
excel_file_path = '/Users/dydit/Desktop/us_address_all.xlsx'  # 실제 사용자 이름으로 변경

# 엑셀 파일 읽어오기 (컬럼 이름 없음)
df = pd.read_excel(excel_file_path, header=None)

# Scatter_geo를 사용하여 각 장소에 핀 찍기
fig = px.scatter_geo(df,
                     lat=df.iloc[:, 1].tolist(),  # 위도 정보는 두 번째 열에 위치
                     lon=df.iloc[:, 2].tolist(),  # 경도 정보는 세 번째 열에 위치
                     scope='usa',
                     title='DETAILED USA MAP',
                     )

st.plotly_chart(fig, use_container_width=True)

# Colored USA Map 넣기
# 엑셀 파일의 로컬 경로로 수정하세요.
excel_file_path = '/Users/dydit/Desktop/us_address_all.xlsx'

# 엑셀 파일 읽어오기 (컬럼 이름 없음)
df = pd.read_excel(excel_file_path, header=None)

# Scatter_geo를 사용하여 각 장소에 핀 찍기
fig = px.scatter_geo(df,
                     lat=df.iloc[:, 1].tolist(),
                     lon=df.iloc[:, 2].tolist(),
                     scope='usa',
                     title='COLORED USA MAP')

# 주별 핀의 개수 계산
pin_counts = df.iloc[:, 3].value_counts().reset_index()
pin_counts.columns = ['State', 'Pin Count']

# Choropleth map을 사용하여 미국 주에 대한 핀의 개수 표시 (붉은 계열 색상 맵 사용)
choropleth_fig = px.choropleth(pin_counts,
                               locations='State',
                               locationmode='USA-states',
                               color='Pin Count',
                               scope='usa',
                               title='Choropleth USA Map - Pin Counts',
                               color_continuous_scale='YlOrRd')

# 두 그래프를 병합하기
for trace in choropleth_fig.data:
    fig.add_trace(trace)

# Streamlit에서 그래프 표시
st.plotly_chart(fig, use_container_width=True)

# 바 차트 생성
bar_chart_fig = px.bar(pin_counts,
                       x='State',
                       y='Pin Count',
                       title='Pin Counts by States',
                       labels={'Pin Count': 'Count', 'State': 'State'},
                       color_discrete_sequence=['#FF0000'])  # 빨간색 계열의 색상

# Streamlit에서 바 차트 표시
st.plotly_chart(bar_chart_fig, use_container_width=True)



# 코드 보여줄 때 (예쁘게)
if st.button("USA python code 보기"):
    code = '''
# 코드 실행 결과를 보여주는 함수 정의
def run_code():
    articles = []
    error_list = []

    url_1 = 'https://www.state.gov/press-releases/'
    wd = initialize_chrome_driver()
    wd.get(url_1)
    time.sleep(3)
    html = wd.page_source
    soup = BeautifulSoup(html, 'html.parser')
    error_message = str()
    
    try:
        news_items = soup.find_all('li', class_='collection-result')
        for item in news_items:
            error_message = ''
            link = item.find('a', class_='collection-result__link')['href']
            if not link:
             error_message = Error_Message(error_message, "None Link")
            date_tag = item.find('div', class_='collection-result-meta').find('span', dir='ltr')
            extracted_date = date_tag.text.strip() if date_tag else 'No date found'
            article_date = date_util(extracted_date)
            if not date_tag:
                error_message = Error_Message(error_message, "None date")
            if article_date <= today:
                # newspaper : 제목,본문 추출
                article = Article(link, language='en')
                article.download()
                article.parse()
                title = article.title
                if not title:
                    error_message = Error_Message(error_message, "None Link")
                text = article.text
                if not text:
                    error_message = Error_Message(error_message, "None Content")
                if error_message is not str():
                    error_list.append({
                            'Error Link': url_1,
                            'Error': error_message
                        })
                else:
                    articles.append({
                            'Title': title,
                            'Link': link,
                            'Content(RAW)': text,
                        })
    except Exception as e:
        error_list.append({
            'Error Link': url_1,
            'Error': str(e)
            })
    return articles, error_list
        
# 코드 실행 
if st.button("USA python 코드 실행"):
    # run_code 함수를 실행하고 반환된 articles를 받습니다.
    articles_data, error_data = run_code()
    
    # 반환된 articles 데이터를 스트림릿의 dataframe으로 표시합니다.
    st.dataframe(articles_data)
    '''
    st.code(code, language = "python")

if st.button("run bizbuzz.py"):
    with open('/Users/dydit/Desktop/Final_US_today_GovFin.py', 'r') as file:
        exec(file.read())


# 오늘 날짜를 '월일' 형식으로 가져오기
from datetime import datetime
import streamlit as st
import pandas as pd
today_str = datetime.now().strftime("%m%d") 

# 버튼과 데이터프레임을 표시하는 코드
if st.button("Articles 파일 보기"):
    df_articles = pd.read_csv(f'articles_{today_str}.csv')
    st.dataframe(df_articles)

if st.button("Error List 파일 보기"):
    df_errors = pd.read_csv(f'error_list_{today_str}.csv')
    st.dataframe(df_errors)

if st.button("Final Articles 파일 보기"):
    df_final_articles = pd.read_csv(f'Final Articles_{today_str}.csv')
    st.dataframe(df_final_articles)