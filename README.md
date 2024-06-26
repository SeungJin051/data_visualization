# 부산광역시_사고위험지역 현황.csv를 활용한 데이터 시각화 하기 
추후 : (소규모 데이터 70개) -> (대규모 데이터 시각화 가능성 있음)

# [1] About the Project
- 이 프로젝트는 **"부산광역시_사고위험지역 현황"** 데이터를 분석하여 사고 위험 지역을 시각화하고 안전 정책에 활용하는 것을 목표로 합니다. 주요 기능은 데이터 시각화를 통해 사고 발생률이 높은 지역을 확인하고, 이를 통해 도시 안전을 개선하는 데 기여하는 것입니다.

## Features
- **사고 위험 지역을 시각화**
- **사고 발생률이 높은 지역을 확인**
- **도시 안전을 개선하는 데 기여**

## Technologies
- <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
- <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>  

## Prerequisites
- Visual Studio Code
  - <img src="https://github.com/SeungJin051/data_visualization/assets/83889135/da6cc334-b66d-41cb-a2d8-1e49007fba76"/>
0. pip 23.3.1 from /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pip (python 3.10)
```bash
pip install folium
```
1. "Python 버전 2.7 또는 3.3 이상이 필요합니다."
```bash
pip install ipython
```
2. "Python 버전 3.9, 3.10, 3.11 또는 3.12 이상이 필요합니다."
```bash
pip install pandas
```
<hr/>

## Maps
### 1. simple_marker_map.py (간단한 마크 표현)
<img width="500" alt="스크린샷 2024-03-22 오전 12 08 53" src="https://github.com/SeungJin051/data_visualization/assets/83889135/c99ab7b9-112a-40b0-9d5e-a3106e6985d3">

### 2. circle_marker_map.py (원형의 마크 표현)
<img width="500" alt="스크린샷 2024-03-22 오전 1 54 28" src="https://github.com/SeungJin051/data_visualization/assets/83889135/174ea84c-8a69-4844-a46e-b2e48f0d3047">

### 3. geo_map.py (형정구역_경계지도.json을 활용해 부산광역시의 구별로 지역을 나눠서 표현, 각 구마다 색의 차이는 사고위험지역_현황.csv의 출동횟수 차이)
<img width="500" alt="스크린샷 2024-03-22 오전 2 39 45" src="https://github.com/SeungJin051/data_visualization/assets/83889135/452ae26f-54aa-48c0-9fbc-d5cd16181cc6">
