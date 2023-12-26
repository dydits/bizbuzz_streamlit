from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
from dateutil import parser
import re
from newspaper import Article
import requests
import feedparser
import spacy
import openai

# 찾는 기업명 리스트(50개)
Top50_Name_list = ['SKLSI', 'Hana West Properties LLC', 'Samsung Electronics', 'Doosan Enerbility America', 
'Hyundai Motor', 'SeAH', 'LG Group', 'GOLFZON', 'GS Global USA', 'Doosan Group', 'ASIANA', 'GS Global', 
'POSCO America Corp', 'Medy-Tox', 'SK life science', 'COUPANG GLOBAL LLC', 'LG Corp', 'SAMSUNG SEMICONDUCTOR', 
'DSME', 'HYUNDAI', 'HL Mando America Corporation', 'Nongshim', 'Hanwha Corporation', 'LG Elec', 'Doosan Corp', 
'MANDO', "Samsung Semiconductor's US", 'Posco', 'SK hynix America', 'LG', 'SeAH America', 'SeAH USA', 
'POSCO International Corp', 'SK Energy', 'KIA MOTORS AMERICA', 'SEAH STEEL', 'LG Energy', 'LG Display', 
'POSCO AMERICA', 'Doosan Heavy Industries', 'Hanwha Corp', 'SM Entertainment USA', 'Kia Corp', 'LS Group', 
'SK E&S', 'LG ELECTRONICS USA', 'Mando America', 'HMGMA', 'POSCO America', 'Golfzon', 'MEDY-TOX', 'LG Energy Solution', 
'SK NETWORKS AMERICA', 'COUPANG GLOBAL', 'Medytox', 'SK Battery', 'Mando America Corp', 'LG Display America', 
'SK Hynix Semiconductor', 'Coupang Global LLC', 'Zenith Electronics LLC', 'Dsme', 'SK E&S America', 'Kia Motors', 
'ASIANA AIRLINES', 'SEAH STEEL USA LLC', 'GSG', 'Mando America Corporation', 'HL Mando America', 'Zenith Electronics', 
'DOOSAN HEAVY INDUSTRIES AMERICA LLC', 'SK Energy Americas', 'SM ENTERTAINMENT', 'POSCO International', 'SeAH Steel', 
'LG ENERGY SOLUTION', 'LS CABLE', 'Doosan Electro-Materials America', 'SM USA', 'LS Cable Systems', 
'Doosan Heavy Industries America Holdings', 'Nongshim America', 'Doosan Heavy Industries America', 'NONGSHIM AMERICA', 
'KOREAN AIR', 'KMMG', 'Doosan', 'LG Energy Solution Tech Center', 'SK E&S Energy', 'HANWHA', 'Samsung Electronics America', 
'HL Mando', 'Mando Corporation', 'Coupang', 'SK Life Science', 'DOOSAN MATERIAL HANDLING SOLUTION DOOSAN INDUSTRIAL VEHICLE AMERICA CORP', 
'Golfzon America Official', 'SK USA', 'Hanwha Q cells', 'Hyundais', 'LG Energy Michigan Tech Center', 'LS Cable & System USA', 
'Kia Georgia Plant', 'HANWHA HOLDINGS', 'DIVAC', 'HANWHA Q CELLS AMERICA', 'DOOSAN ELECTRO-MATERIALS AMERICA', 'MEDYTOX', 
'POSCO Holdings', 'Daewoo Shipbuilding and Marine Engineering', 'LG Electronics', 'Hanwha Holdings USA', 
'POSCO AMERICA CORPORATION', 'HANWHA CORP', 'Kia Motors Manufacturing Georgia', 'SM ENTERTAINMENT USA', 'KIA', 'SMtown USA', 
'SK HYNIX', 'Kias', 'Hanwha Holdings', 'Golfzon America', 'Mando', 'Hana West Properties', 'Samsung Biologics', 
'Hanwha Q CELLS America', 'SK E&S Co', 'Doosan Heavy Industries America LLC', 'POSCO America Corporation', 'Asiana Airlines', 
'Doosan Enerbility America Holdings', 'Kia Corporation', 'SK NETWORKS', 'DSME CO', 'Kia Georgia', 'SK HYNIX AMERICA', 
'Hanwha Group', 'Coupang Global', 'SK', 'Qcells', 'SAMSUNG', 'KIA GEORGIA', 'Hyundai', 'Doosan Material Handling Solutions', 
'SK Networks America', 'Hanwha Q CELLS', 'Samsung US', 'KIA MOTORS CORP', 'Samsung Semiconductor USA', 'LG ELECTRONICS', 
'SK Group Companies', 'SK GROUP', 'Samsung', 'SK Networks', 'Doosan Corporation', 'DSEM', 'SK E&S AMERICA', 'Posco America', 
'LGE', 'SK Hynix America', 'Samsung Electronics North America', 'Hyundai Motors', 'Hanwha USA', 'Kia', 'Samsung Semiconductor', 
'Doosan Industrial Vehicle', 'POSCO', 'LS Cable Systems America', 'Doosan Enerbility', 'LS CABLE SYSTEMS AMERICA', 
'LG ENERGY SOLUTION MICHIGAN TECH CENTER', 'SK ENERGY', 'SeAH US', 'Doosan Electronics', 'Kia America', 
'SAMSUNG ELECTRONICS AMERICA', 'NONGSHIM', 'Hyundai Motor Group', 'SK Hynix', 'GS GLOBAL USA', 'Kia Motors America', 
'LS CABLE & SYSTEM', 'SK hynix', 'KIA MOTORS', 'LG ELECTRONICS(ZENITH ELECTRONICS LLC)', 'SK ENERGY AMERICAS', 'DHI', 'Asiana', 
'GOLFZON AMERICA', 'HANWHA WEST PROPERTIES LLC', 'KOREAN AIRLINES', 'LG DISPLAY', 'LG DISPLAY AMERICA', 'SK LIFE SCIENCE', 
'Korean Air', 'Zenith Electronics Corp', 'Q CELLS', 'Doosan Industrial Vehicle America Corporation', 'Samsung Biologics America', 
'GSG Corp', 'SAMSUNG BIOLOGICS', 'SK Group', 'SM Entertainment', 'Seah Steel USA LLC', 'Doosan Industrial Vehicle America Corp', 
'Hanwha', 'HYUNDAI MOTORS', 'Hanwha OCEAN', 'Nongshim USA', 'SeAH Steel USA', 'LS Cable & System', 'SKLSI', 'HanaWestPropertiesLLC', 
'SamsungElectronics', 'DoosanEnerbilityAmerica', 'HyundaiMotor', 'SeAH', 'LGGroup', 'GOLFZON', 'GSGlobalUSA', 'DoosanGroup', 
'ASIANA', 'GSGlobal', 'POSCOAmericaCorp', 'Medy-Tox', 'SKlifescience', 'COUPANGGLOBALLLC', 'LGCorp', 'SAMSUNGSEMICONDUCTOR', 
'DSME', 'HYUNDAI', 'HLMandoAmericaCorporation', 'Nongshim', 'HanwhaCorporation', 'LGElec', 'DoosanCorp', 'MANDO', 
"SamsungSemiconductor'sUS", 'Posco', 'SKhynixAmerica', 'LG', 'SeAHAmerica', 'SeAHUSA', 'POSCOInternationalCorp', 'SKEnergy', 
'KIAMOTORSAMERICA', 'SEAHSTEEL', 'LGEnergy', 'LGDisplay', 'POSCOAMERICA', 'DoosanHeavyIndustries', 'HanwhaCorp', 
'SMEntertainmentUSA', 'KiaCorp', 'LSGroup', 'SKE&S', 'LGELECTRONICSUSA', 'MandoAmerica', 'HMGMA', 'POSCOAmerica', 'Golfzon', 
'MEDY-TOX', 'LGEnergySolution', 'SKNETWORKSAMERICA', 'COUPANGGLOBAL', 'Medytox', 'SKBattery', 'MandoAmericaCorp', 
'LGDisplayAmerica', 'SKHynixSemiconductor', 'CoupangGlobalLLC', 'ZenithElectronicsLLC', 'Dsme', 'SKE&SAmerica', 'KiaMotors', 
'ASIANAAIRLINES', 'SEAHSTEELUSALLC', 'GSG', 'MandoAmericaCorporation', 'HLMandoAmerica', 'ZenithElectronics', 
'DOOSANHEAVYINDUSTRIESAMERICALLC', 'SKEnergyAmericas', 'SMENTERTAINMENT', 'POSCOInternational', 'SeAHSteel', 'LGENERGYSOLUTION', 
'LSCABLE', 'DoosanElectro-MaterialsAmerica', 'SMUSA', 'LSCableSystems', 'DoosanHeavyIndustriesAmericaHoldings', 'NongshimAmerica',
'DoosanHeavyIndustriesAmerica', 'NONGSHIMAMERICA', 'KOREANAIR', 'KMMG', 'Doosan', 'LGEnergySolutionTechCenter', 'SKE&SEnergy', 
'HANWHA', 'SamsungElectronicsAmerica', 'HLMando', 'MandoCorporation', 'Coupang', 'SKLifeScience', 
'DOOSANMATERIALHANDLINGSOLUTIONDOOSANINDUSTRIALVEHICLEAMERICACORP', 'GolfzonAmericaOfficial', 'SKUSA', 'HanwhaQcells', 'Hyundais', 
'LGEnergyMichiganTechCenter', 'LSCable&SystemUSA', 'KiaGeorgiaPlant', 'HANWHAHOLDINGS', 'DIVAC', 'HANWHAQCELLSAMERICA', 
'DOOSANELECTRO-MATERIALSAMERICA', 'MEDYTOX', 'POSCOHoldings', 'DaewooShipbuildingandMarineEngineering', 'LGElectronics', 
'HanwhaHoldingsUSA', 'POSCOAMERICACORPORATION', 'HANWHACORP', 'KiaMotorsManufacturingGeorgia', 'SMENTERTAINMENTUSA', 'KIA', 
'SMtownUSA', 'SKHYNIX', 'Kias', 'HanwhaHoldings', 'GolfzonAmerica', 'Mando', 'HanaWestProperties', 'SamsungBiologics', 
'HanwhaQCELLSAmerica', 'SKE&SCo', 'DoosanHeavyIndustriesAmericaLLC', 'POSCOAmericaCorporation', 'AsianaAirlines', 
'DoosanEnerbilityAmericaHoldings', 'KiaCorporation', 'SKNETWORKS', 'DSMECO', 'KiaGeorgia', 'SKHYNIXAMERICA', 'HanwhaGroup', 
'CoupangGlobal', 'SK', 'Qcells', 'SAMSUNG', 'KIAGEORGIA', 'Hyundai', 'DoosanMaterialHandlingSolutions', 'SKNetworksAmerica', 
'HanwhaQCELLS', 'SamsungUS', 'KIAMOTORSCORP', 'SamsungSemiconductorUSA', 'LGELECTRONICS', 'SKGroupCompanies', 'SKGROUP', 'Samsung',
'SKNetworks', 'DoosanCorporation', 'DSEM', 'SKE&SAMERICA', 'PoscoAmerica', 'LGE', 'SKHynixAmerica', 
'SamsungElectronicsNorthAmerica', 'HyundaiMotors', 'HanwhaUSA', 'Kia', 'SamsungSemiconductor', 'DoosanIndustrialVehicle', 
'POSCO', 'LSCableSystemsAmerica', 'DoosanEnerbility', 'LSCABLESYSTEMSAMERICA', 'LGENERGYSOLUTIONMICHIGANTECHCENTER', 'SKENERGY', 
'SeAHUS', 'DoosanElectronics', 'KiaAmerica', 'SAMSUNGELECTRONICSAMERICA', 'NONGSHIM', 'HyundaiMotorGroup', 'SKHynix', 
'GSGLOBALUSA', 'KiaMotorsAmerica', 'LSCABLE&SYSTEM', 'SKhynix', 'KIAMOTORS', 'LGELECTRONICS(ZENITHELECTRONICSLLC)', 
'SKENERGYAMERICAS', 'DHI', 'Asiana', 'GOLFZONAMERICA', 'HANWHAWESTPROPERTIESLLC', 'KOREANAIRLINES', 'LGDISPLAY', 
'LGDISPLAYAMERICA', 'SKLIFESCIENCE', 'KoreanAir', 'ZenithElectronicsCorp', 'QCELLS', 'DoosanIndustrialVehicleAmericaCorporation', 
'SamsungBiologicsAmerica', 'GSGCorp', 'SAMSUNGBIOLOGICS', 'SKGroup', 'SMEntertainment', 'SeahSteelUSALLC', 
'DoosanIndustrialVehicleAmericaCorp', 'Hanwha', 'HYUNDAIMOTORS', 'HanwhaOCEAN', 'NongshimUSA', 'SeAHSteelUSA', 'LSCable&System']

# All articles load
articles = pd.read_csv('US_All Articles' + datetime.now().strftime("_%y%m%d") + '.csv')
########################################### <Select 1 : using string> ##############################################
Articles_Select1 = {'Company':[], 'Title':[],'Link':[],'Contents':[]}
for index, row in articles.iterrows():
    for company in Top50_Name_list:
        if (company in row['Title']) or (company in row['Content(RAW)']) :
            Articles_Select1['Company'].append(company)
            Articles_Select1['Title'].append(row['Title'])
            Articles_Select1['Link'].append(row['Link'])
            Articles_Select1['Contents'].append(row['Content(RAW)'])
            break
Articles_Select1 = (pd.DataFrame(Articles_Select1))

########################################### <Select 2 : NER - SpaCy> ##############################################
# spaCy의 NER 모델 로드
nlp = spacy.load("en_core_web_sm")
Articles_Select2 = {'Company':[], 'Title':[],'Link':[],'Contents':[]}
for i in range(len(Articles_Select1)):
    # 분석할 텍스트
    title = Articles_Select1['Title'][i]
    link = Articles_Select1['Link'][i]
    content = Articles_Select1['Contents'][i]
    # NER 처리
    doc1 = nlp(title)
    doc2 = nlp(content)
    # 추출된 고유명사 저장 (ORG 및 PRODUCT)
    entities1 = [(ent.text, ent.label_) for ent in doc1.ents if ent.label_ in ["ORG", "PRODUCT"]]
    entities2 = [(ent.text, ent.label_) for ent in doc2.ents if ent.label_ in ["ORG", "PRODUCT"]]
    # 리스트에 있는 기업명 필터링
    filtered_entities1 = [entity for entity, label in entities1 if (label in ["ORG", "PRODUCT"]) and (entity in Top50_Name_list)]
    filtered_entities2 = [entity for entity, label in entities2 if (label in ["ORG", "PRODUCT"]) and (entity in Top50_Name_list)]
    if filtered_entities1 != []:
        Articles_Select2['Company'].append(', '.join(set(filtered_entities1)))
        Articles_Select2['Title'].append(title)
        Articles_Select2['Link'].append(link)
        Articles_Select2['Contents'].append(content)
    elif filtered_entities2 != []:
        Articles_Select2['Company'].append(', '.join(set(filtered_entities2)))
        Articles_Select2['Title'].append(title)
        Articles_Select2['Link'].append(link)
        Articles_Select2['Contents'].append(content)

Articles_Select2 = pd.DataFrame(Articles_Select2)

########################################### <Select 3 : OpenAI> ##############################################
# 발급받은 API 키 설정(SNU 빅데이터핀테크 API)
OPENAI_API_KEY = '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'
# openai API 키 인증
openai.api_key = OPENAI_API_KEY
# ChatGPT - 3.5 turbo updated
def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

Articles_Final = {'Company':[], 'Title':[],'Link':[],'Content(RAW)':[]}
for i in range(len(Articles_Select2)):
    title = Articles_Select2['Title'][i]
    content = Articles_Select2['Contents'][i]
    company = Articles_Select2['Company'][i]
    link = Articles_Select2['Link'][i]
    prompt = f"""Article Title = {title} //
            Article Contents = {content} //
            Company Name to Check = {company} //

            Based on the article titled '{title}' and its content,
            please analyze whether the term '{company}' refers to an actual company.
            If '[{company}' is related to a real company, output 'O'.
            If it is not related to a real company, output 'X'.
            """
    response = get_completion(prompt)
    print(response)
    if response == 'O':
        Articles_Final['Company'].append(company)
        Articles_Final['Title'].append(title)
        Articles_Final['Link'].append(link)
        Articles_Final['Content(RAW)'].append(content)

########################################### <US Website News Final DataFrame> ##############################################
Articles_Final = pd.DataFrame(Articles_Final)
Articles_Final.to_csv('US_Final Selected Articles' + datetime.now().strftime("_%y%m%d") + '.csv')
