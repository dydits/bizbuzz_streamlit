import streamlit as st 

# 페이지 기본 설정 
st.set_page_config(
    page_icon = "🗺️📍",
    page_title = "BIZBUZZ",
    layout = "wide",
)

st.subheader("USA")

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
today_str = datetime.now().strftime("%m%d")  # 예: '1207'

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