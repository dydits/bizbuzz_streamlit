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


# 라이브러리 import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from dateutil import parser
import re
from newspaper import Article
import requests
import numpy as np
from selenium.webdriver.common.by import By

def initialize_chrome_driver():
  # Chrome 옵션 설정 : USER_AGENT는 알아서 수정
  #USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.105 Safari/537.36"
  # 태준컴
  USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15'
  chrome_options = Options()
  chrome_options.page_load_strategy = 'normal'  # 'none', 'eager', 'normal'
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument('--disable-gpu')
  chrome_options.add_argument(f'user-agent={USER_AGENT}')
  # Chrome 드라이버 설정
  service = Service()
  wd = webdriver.Chrome(service=service, options=chrome_options)
  return wd

# 날짜 통합 함수
def date_util(article_date):
  try:
    # Parse the date using dateutil.parser
    article_date = parser.parse(article_date).date()
  except ValueError:
    # If parsing fails, handle the relative dates
    article_date = article_date.lower()
    time_keywords = ["h", "hrs", "hr", "m", "s", "hours","hour", "minutes", "minute", "mins", "min", "seconds", "second", "secs", "sec"]
    if any(keyword in article_date for keyword in time_keywords):
      article_date = today
    elif "days" in article_date or "day" in article_date:
      # Find the number of days and subtract from today
      number_of_days = int(''.join(filter(str.isdigit, article_date)))
      article_date = today - timedelta(days=number_of_days)
    else:
      return None
  return article_date

today = date_util(datetime.now().strftime("%Y-%m-%d"))

# 에러 메시지 작성 함수
def Error_Message(message, add_error):
    if message is not str() : message += '/'
    message += add_error
    return message

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
if st.button("USA python code 실행"):
    # run_code 함수를 실행하고 반환된 articles를 받습니다.
    articles_data, error_data = run_code()
    
    # 반환된 articles 데이터를 스트림릿의 dataframe으로 표시합니다.
    st.dataframe(articles_data)