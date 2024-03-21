import folium
import pandas as pd

# 데이터 로드
geo_path = "./data/부산광역시_행정구역_경계지도.json"
df = pd.read_csv("./data/부산광역시_사고위험지역_현황.csv", encoding='utf-8')

# 필요한 컬럼만 변수에 따로 저장하기
df_sample = df[['시군구명', '경도', '위도', '출동횟수']]

# 지도의 중심 좌표(부산광역시)를 설정합니다.
center = [35.1379222, 129.05562775]

# 맵 생성
map = folium.Map(location=center, zoom_start=10)

# Choropleth 레이어 추가
folium.Choropleth(
    geo_data=geo_path,
    data=df_sample,
    columns=['시군구명', '출동횟수'],
    key_on='feature.id',
    fill_color='YlGn',
).add_to(map)

# 생성한 지도를 화면에 표시합니다.
map.save('./maps/geo_map.html')