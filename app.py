import streamlit as st

# -----------------------------
# 페이지 설정 (한 번만 설정)
# -----------------------------
st.set_page_config(
    page_title="광주동신여자고등학교 길찾기",
    page_icon="🏫",
    layout="wide"
)

# -----------------------------
# 현재 페이지 저장
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# =====================================================
# 메인 화면
# =====================================================
if st.session_state.page == "home":

    st.title("🏫 광주동신여자고등학교 길찾기")

    st.info("""
**광주동신여자고등학교에 처음 방문하시는 분들을 위한 학교 안내 서비스입니다.**

📍 우리 학교는 **경사지에 위치하여 3층이 외부에서는 1층처럼 보이는 독특한 구조**입니다.

🚶 방문객 여러분의 **원활한 길찾기를 도와드리겠습니다.**

---

### 🏫 학교 층별 안내

**3층 (외부 출입층)**
- 공용 신발장
- 행정실
- 교무실

**4층**
- 3학년 교실

**5층**
- 2학년 교실

**6층**
- 1학년 교실
""")

    st.divider()

    st.subheader("📍 현재 위치 찾기")

    st.write(
        "현재 주변에서 보이는 풍경과 가장 비슷한 사진을 선택하면 현재 위치와 층수 정보를 확인할 수 있습니다."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("A.png")
        if st.button("A 위치 선택"):
            st.session_state.page = "A"
            st.rerun()

    with col2:
        st.image("B.png")
        if st.button("B 위치 선택"):
            st.session_state.page = "B"
            st.rerun()

    with col3:
        st.image("C.png")
        if st.button("C 위치 선택"):
            st.session_state.page = "C"
            st.rerun()
# =====================================================
# A 위치
# =====================================================
elif st.session_state.page == "A":

    st.title("📍 현재 위치 안내")

    st.subheader("현재 위치")

    st.image(
        "aaa.png",
        caption="현재 위치",
        use_container_width=True
    )

    st.info("""
📍 **빨간색 위치 마커로 표시된 곳이 현재 여러분이 위치한 장소입니다.**

갈라지는 두 길 중 한쪽 길을 따라 계속 올라오시면
아래 사진과 같은 **학교 후문**이 보입니다.

후문으로 들어오시면 **학교 건물 3층**으로 진입하게 됩니다.
""")

    st.subheader("📷 아래 사진과 같은 후문이 보이면 맞게 이동하고 있는 것입니다.")

    st.image(
        "D.png",
        caption="학교 후문",
        use_container_width=True
    )

    st.success("후문으로 들어오시면 학교 3층으로 연결됩니다.")

    if st.button("🏠 메인 화면으로"):
        st.session_state.page = "home"
        st.rerun()


# =====================================================
# B 위치
# =====================================================
elif st.session_state.page == "B":

    st.title("📍 현재 위치 안내")

    st.subheader("현재 위치")

    st.image(
        "bbb.png",
        caption="현재 위치",
        use_container_width=True
    )

    st.info("""
📍 **빨간색 위치 마커로 표시된 곳이 현재 여러분이 위치한 장소입니다.**

현재 여러분이 계신 곳은 **학교 1층**입니다.

앞에 보이는 계단을 따라 계속 올라오시면
**학교 3층**으로 이동하실 수 있습니다.
""")

    st.success("계단을 따라 올라오시면 학교 3층으로 연결됩니다.")

    if st.button("🏠 메인 화면으로"):
        st.session_state.page = "home"
        st.rerun()


# =====================================================
# C 위치
# =====================================================
elif st.session_state.page == "C":

    st.title("📍 현재 위치 안내")

    st.subheader("현재 위치")

    st.image(
        "ccc.png",
        caption="현재 위치",
        use_container_width=True
    )

    st.info("""
📍 **빨간색 위치 마커로 표시된 곳이 현재 여러분이 위치한 장소입니다.**

앞에 보이는 계단을 따라 계속 올라오시면
아래 사진과 같은 **학교 입구**가 보입니다.

해당 입구로 들어오시면 **학교 건물 3층**으로 진입하게 됩니다.
""")

    st.subheader("📷 아래 사진과 같은 입구가 보이면 맞게 이동하고 있는 것입니다.")

    st.image(
        "D.png",
        caption="학교 입구",
        use_container_width=True
    )

    st.success("입구로 들어오시면 학교 3층으로 연결됩니다.")

    if st.button("🏠 메인 화면으로"):
        st.session_state.page = "home"
        st.rerun()
