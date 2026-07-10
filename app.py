# school map

import streamlit as st

st.set_page_config(
    page_title="광주동신여자고등학교 길찾기",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 광주동신여자고등학교 길찾기")

st.info(
    """
    **광주동신여자고등학교에 처음 방문하시는 분들을 위한 학교 안내 서비스입니다.**

    📍 우리 학교는 **경사지에 위치하여 3층이 외부에서는 1층처럼 보이는 독특한 구조**입니다.

    🚶 방문객 여러분의 **원활한 길찾기를 도와드리겠습니다.**
    """
)

st.divider()

st.subheader("📍 현재 위치 찾기")

st.write(
    "현재 주변에서 보이는 풍경과 가장 비슷한 사진을 선택하면 **현재 위치와 층수, 주변 시설 정보**를 확인할 수 있습니다."
)
