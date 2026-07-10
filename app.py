# school map

import streamlit as st

st.title("광주동신여자고등학교 길찾기")

st.write("학교 안내 서비스입니다.")

import streamlit as st
from PIL import Image
from locations import routes

st.set_page_config(
    page_title="광주동신여고 길찾기",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 광주동신여자고등학교 길찾기")

st.write(
"""
처음 방문하는 분들을 위한
학교 안내 서비스입니다.
"""
)

st.info(
"""
우리 학교는 경사지에 위치하여
3층이 외부에서는 1층처럼 연결되는
독특한 구조입니다.
"""
)

# 지도 출력

try:
    image = Image.open("school_map.png")
    st.image(image, caption="학교 안내도", use_container_width=True)

except:
    st.warning("학교 지도 이미지를 넣어주세요.")

st.divider()

st.header("현재 위치")

start = st.selectbox(

"현재 위치를 선택하세요",

[
"정문",
"주차장",
"운동장",
"후문"
]

)

st.header("목적지")

destination = st.selectbox(

"목적지를 선택하세요",

[
"교무실",
"행정실",
"보건실",
"도서관",
"강당"
]

)

if st.button("길찾기"):

    key = (start,destination)

    if key in routes:

        st.success("이동 경로")

        st.write(routes[key])

    else:

        st.error("아직 해당 경로가 등록되지 않았습니다.")

st.divider()

st.subheader("학교 구조 안내")

st.write("""
광주동신여고는 고지대에 위치하여

외부에서는 3층이 실제 출입층입니다.

방문 시 층수를 확인해 주세요.
""")

import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("광주동신여자고등학교 안내 지도")

# 학교 중심 좌표(예시)
school_lat = 35.176
school_lon = 126.912

# 지도 생성
m = folium.Map(
    location=[school_lat, school_lon],
    zoom_start=18
)

# GeoJSON 불러오기
# folium.GeoJson(
    "school.geojson",
    name="학교"
).add_to(m)

# 지도 출력
st_folium(
    m,
    width=900,
    height=600
)
