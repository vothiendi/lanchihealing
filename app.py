import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Lan Chi", page_icon="✦", layout="wide")

# ===== STATE =====
if "page" not in st.session_state:
    st.session_state.page = "home"

# ===== FLOWERS =====
flowers = [
    ("Hoa quỳnh trắng", "✧ 𓆸 ✧", "Hôm nay anh gửi em một đóa quỳnh trắng. Mong ngày của em dịu lại, nhẹ như hơi thở."),
    ("Hoa trà hồng", "❀ 𓂃 ❀", "Một đóa trà hồng cho em. Mong em vẫn đẹp theo cách bình tĩnh của mình."),
    ("Hoa dành dành", "✿ 𓇬 ✿", "Một chút hương dành dành. Mong em có một góc thật trong veo để nghỉ."),
    ("Hoa sen trắng", "𑁍 𓆟 𑁍", "Sen trắng hôm nay. Mong em đi qua mọi thứ thật nhẹ."),
    ("Hoa baby", "⋆𖧷⋆", "Một nhành baby nhỏ. Mong những điều nhỏ cũng đứng về phía em."),
]

# ===== CSS =====
st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg,#2b2e2c,#6e6c66);
color:white;
}
.card{
padding:25px;
border-radius:20px;
background:rgba(255,255,255,0.1);
margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ===== NAV =====
def go_home():
    if st.button("← Quay về"):
        st.session_state.page = "home"
        st.rerun()

# ===== HOME =====
def home():
    st.title("Một góc nhỏ của Chi")

    col1,col2=st.columns(2)

    with col1:
        st.markdown('<div class="card"><h3>Chữa lành</h3></div>',unsafe_allow_html=True)
        if st.button("Mở Chữa lành"):
            st.session_state.page="heal"
            st.rerun()

    with col2:
        st.markdown('<div class="card"><h3>Chuẩn bị tài sản</h3></div>',unsafe_allow_html=True)
        if st.button("Mở Tài sản"):
            st.session_state.page="asset"
            st.rerun()

# ===== HEAL =====
def heal():
    go_home()

    name,symbol,wish = flowers[date.today().toordinal()%len(flowers)]

    st.markdown(f"""
    <div class="card" style="text-align:center">
    <div style="font-size:60px">{symbol}</div>
    <h2>{name}</h2>
    <p>{wish}</p>
    </div>
    """,unsafe_allow_html=True)

    note = st.text_area("Viết cảm xúc hôm nay")
    if note:
        st.success("Anh đã giữ lại cho em rồi.")

# ===== ASSET =====
def asset():
    go_home()

    st.header("Bảng tính thu hồi vốn")

    capital = st.number_input("Vốn",value=100_000_000)
    quantity = st.number_input("Số lượng",value=5000)
    price = st.number_input("Giá hiện tại",value=35000)

    fee = 0.0025

    need_sell = capital/(price*(1-fee))
    remain = max(quantity-need_sell,0)

    if st.button("Tính"):
        st.write("Cần bán:",int(need_sell))
        st.write("Còn lại:",int(remain))

# ===== ROUTER =====
if st.session_state.page=="heal":
    heal()
elif st.session_state.page=="asset":
    asset()
else:
    home()
