import folium
import pandas as pd
from IPython.display import display

# Data load
df = pd.read_csv("./data/부산광역시_사고위험지역_현황.csv", encoding='utf-8')

print('=' * 80)
print('부산광역시 방범용 CCTV 정보')

# pandas를 이용해 엑셀 데이터를 읽어들이고 이용하고자 하는 데이터를 골라내서 IPython.display 함수를 이용
display(df.head(5))

# 필요한 컬럼만 변수에 따로 저장하기
df_sample = df[['시군구명', '경도', '위도']]
display(df_sample.head(3))

# 데이터 널값 확인하기 (데이터 가공) null 값이 0이기에 문제 없음 확인
print('데이터 널값 확인')
display(df_sample.isnull().sum())

# 지도의 중심 좌표(부산광역시)를 설정합니다.
# 경도
longitude = 129.05562775

# 위도
latitude = 35.1379222

# Folium 지도 객체를 생성합니다.
map = folium.Map(location=[latitude, longitude],
                 zoom_start=12)
map_info = df_sample[['시군구명', '경도', '위도']].dropna()

# 시각화에 사용할 가장 마지막 테이블에 있는 위도와 경도값을 사용해 해당 위치에 마커를 남김
    # 값이 많아 for문을 활용해 알아서 끼워맞추도록
    # 마우스를 마커 위에 올리면 해당 공원의 이름이 나오고, 마커를 클릭해도 이름이 나옴
for lat, long, name in zip(map_info["위도"], map_info["경도"], map_info["시군구명"]):
    folium.Marker([lat, long], popup=name, tooltip=name).add_to(map)

# 생성한 지도를 화면에 표시합니다.
map.save('./maps/simple_marker_map.html')