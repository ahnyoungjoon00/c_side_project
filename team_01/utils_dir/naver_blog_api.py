import requests
import pandas as pd

def naver_api(query, search_type="blog", display=10):
    # API URL
    # 블로그-> blog, 뉴스-> news, 책-> book, 백과사전->encyc, 
    # 카페글->cafearticle, 지식인->kin, 웹문서->webkr, 이미지->image, 
    # 쇼핑->shop, 전문자료->doc, 성인검색어 판별->adult, 오타변환->errata
    url = f"https://openapi.naver.com/v1/search/{search_type}.json"
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = {
    'query': query,
    'display': display,}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error 발생:", response.status_code)
        return None
    
data = []
def make_df(query, search_type) : 
    result = naver_api(query, search_type)
    if result:
        for item in result['items']:
            row = {
                "title": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                "link": item.get("link", ""),
                "description": item.get("description", "").replace("<b>", "").replace("</b>", "")
            }
            for key in item:
                if key not in row:
                    row[key] = item[key]
            data.append(row)
    return pd.DataFrame(data)