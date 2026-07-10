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

import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="광주동신여자고등학교 길찾기",
    page_icon="🏫",
    layout="wide"
)

# -----------------------------
# 제목
# -----------------------------
st.title("🏫 광주동신여자고등학교 길찾기")

st.info("""
**광주동신여자고등학교에 처음 방문하시는 분들을 위한 학교 안내 서비스입니다.**

📍 우리 학교는 **경사지에 위치하여 3층이 외부에서는 1층처럼 보이는 독특한 구조**입니다.

🚶 방문객 여러분의 **원활한 길찾기를 도와드리겠습니다.**
""")

st.divider()

st.subheader("📍 현재 위치 찾기")

st.write(
    "현재 주변에서 보이는 풍경과 가장 비슷한 사진을 선택해 주세요."
)

# -----------------------------
# 사진 3개 배치
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.image("A.png", caption="A")
    if st.button("선택", key="A"):
        st.session_state.page = "A"

with col2:
    st.image("B.png", caption="B")
    if st.button("선택", key="B"):
        st.session_state.page = "B"

with col3:
    st.image("C.png", caption="C")
    if st.button("선택", key="C"):
        st.session_state.page = "C"

# -----------------------------
# 페이지 이동
# -----------------------------
if "page" in st.session_state:

    if st.session_state.page == "A":
        st.switch_page("pages/A.py")

    elif st.session_state.page == "B":
        st.switch_page("pages/B.py")

    elif st.session_state.page == "C":
        st.switch_page("pages/C.py")
        
