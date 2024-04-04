from pymongo import MongoClient
import pandas as pd

# MongoDB와 연결
my_client = MongoClient("mongodb://localhost:27017/")

# 현재 이 db에 존재하는 database의 이름을 확인
print(my_client.list_database_names())

# 데이터 csv 로드하기
df = pd.read_csv("./data/부산광역시_사고위험지역_현황.csv", encoding='utf-8')

# 필요한 컬럼만 변수에 따로 저장하기
df_sample = df[['시군구명', '경도', '위도', '출동횟수']]

# MongoDB collection 선택
mydb = my_client['visualizationProject']
mycol = mydb['data']

# DataFrame의 각 행을 MongoDB에 삽입
data_to_insert = df_sample.to_dict(orient='records')
mycol.insert_many(data_to_insert)