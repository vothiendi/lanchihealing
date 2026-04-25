import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(
    page_title="Lan Chi | Ritach Solutions",
    page_icon="✦",
    layout="wide"
)

# ===== CẤU HÌNH ẢNH =====
HERO_IMAGE = "hinhanh.png"

# ===== STATE =====
if "page" not in st.session_state:
    st.session_state.page = "home"

# ===== HOA MỖI NGÀY =====
flowers = [
    ("Hoa quỳnh trắng", "✧ 𓆸 ✧", "Hôm nay anh gửi Chi một đóa quỳnh trắng, nở thật khẽ như một khoảng thở sạch. Mong mọi điều nặng trong lòng em dịu xuống từng chút."),
    ("Hoa trà hồng phấn", "❀ 𓂃 ❀", "Hôm nay là một đóa trà hồng phấn, dịu mà vẫn sang. Mong Chi giữ được vẻ bình tĩnh đẹp đẽ của mình và thương mình nhiều hơn một chút."),
    ("Hoa dành dành", "✿ 𓇬 ✿", "Anh đặt trước cửa trang này một đóa dành dành thơm nhẹ. Mong ngày của Chi có một góc trong veo để nghỉ mắt, nghỉ tim rồi bước tiếp nhẹ nhàng."),
    ("Hoa sen trắng", "𑁍 𓆟 𑁍", "Hôm nay anh chọn sen trắng cho Chi. Mong em đi qua mọi việc bằng sự sáng rõ và không bị cuốn khỏi nhịp riêng của mình."),
    ("Hoa baby trắng", "⋆𖧷⋆", "Một nhành baby trắng nhỏ xíu dành cho Chi hôm nay. Mong những điều nhỏ cũng biết đứng về phía em."),
    ("Hoa mẫu đơn kem", "✺ 𓂂 ✺", "Hôm nay là mẫu đơn màu kem, đầy đặn và ấm. Mong Chi thấy mình đủ quý, đủ đẹp, đủ đáng được nâng niu trong cả những lúc chưa kịp rực rỡ."),
    ("Hoa oải hương", "☾ 𖧧 ☽", "Anh gửi Chi một nhánh oải hương tím nhạt. Mong đầu óc em bớt ồn, hơi thở chậm lại, và những việc cần làm tự nằm vào hàng lối rõ ràng."),
]

# ===== HÀM TÍNH TIỀN =====
def format_vnd(value):
    return f"{int(value):,}"

def parse_vnd(text, default=0.0):
    cleaned = str(text).replace(",", "").replace(" ", "").strip()
    if cleaned == "":
        return float(default)
    try:
        return float(cleaned)
    except ValueError:
        return float(default)

# ===== CSS =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Inter:wght@300;400;500;600&display=swap');

.stApp {
    background:
        radial-gradient(circle at top left, rgba(190, 196, 184, 0.30), transparent 30%),
        radial-gradient(circle at bottom right, rgba(220, 210, 194, 0.26), transparent 34%),
        linear-gradient(135deg, #252826 0%, #3a3b37 45%, #c9c3b8 100%);
    color: #f6f1e8;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 2.3rem;
    padding-bottom: 3rem;
    max-width: 1180px;
}

label, .stTextInput label, .stTextArea label {
    color: #fff8ee !important;
    font-weight: 500 !important;
}

.hero {
    padding: 54px 46px;
    border-radius: 34px;
    background: rgba(255, 255, 255, 0.13);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(255,255,255,0.23);
    box-shadow: 0 24px 80px rgba(0,0,0,0.28);
    margin-bottom: 28px;
}

.pill {
    display: inline-block;
    padding: 8px 15px;
    border-radius: 999px;
    background: rgba(255,255,255,0.18);
    color: rgba(255,255,255,0.88);
    font-size: 13px;
    margin-bottom: 18px;
    border: 1px solid rgba(255,255,255,0.18);
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 56px;
    line-height: 1.04;
    letter-spacing: -1.4px;
    color: #fff8eb;
    margin-bottom: 14px;
}

.subtitle {
    font-size: 18px;
    color: rgba(255,255,255,0.78);
    max-width: 730px;
    line-height: 1.75;
}

.card-link {
    text-decoration: none !important;
    display: block;
}

.card {
    min-height: 215px;
    padding: 28px;
    border-radius: 30px;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0 18px 48px rgba(0,0,0,0.18);
    transition: 0.25s ease;
    margin-bottom: 20px;
    cursor: pointer;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 24px 60px rgba(0,0,0,0.24);
}

.card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 31px;
    margin: 0 0 14px 0;
}

.card p {
    font-size: 15px;
    line-height: 1.7;
    margin: 0;
}

.card.heal {
    background: linear-gradient(135deg, rgba(176, 190, 178, 0.52), rgba(124, 139, 132, 0.42));
    color: #fff8ee;
}

.card.work {
    background: linear-gradient(135deg, rgba(232, 226, 214, 0.72), rgba(197, 190, 178, 0.58));
    color: #242724;
    cursor: default;
}

.card.asset {
    background: linear-gradient(135deg, rgba(118, 145, 145, 0.48), rgba(73, 91, 91, 0.45));
    color: #f4f1ea;
}

.card.rest {
    background: linear-gradient(135deg, rgba(239, 241, 236, 0.62), rgba(202, 202, 194, 0.50));
    color: #252826;
    cursor: default;
}

.card.heal h3, .card.heal p,
.card.asset h3, .card.asset p {
    color: #fff8ee;
}

.card.work h3, .card.work p,
.card.rest h3, .card.rest p {
    color: #252826;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    margin: 42px 0 16px;
    color: #fff8ee;
}

.box, .finance-box, .flower-box {
    padding: 24px;
    border-radius: 32px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.22);
    backdrop-filter: blur(18px);
    box-shadow: 0 18px 48px rgba(0,0,0,0.16);
}

img {
    border-radius: 34px;
    box-shadow: 0 24px 70px rgba(0,0,0,0.30);
    border: 1px solid rgba(255,255,255,0.22);
}

.note, .small-soft {
    font-size: 14px;
    color: rgba(255,255,255,0.80);
    margin-top: 8px;
    line-height: 1.7;
}

.flower-symbol {
    font-size: 86px;
    text-align: center;
    line-height: 1;
    padding: 18px 0 8px;
}

.flower-name {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    text-align: center;
    color: #fff8ee;
    margin-bottom: 12px;
}

.metric-shell {
    padding: 16px 18px;
    border-radius: 18px;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.13);
}

.metric-label {
    color: #fff8ee;
    font-size: 13px;
    margin-bottom: 4px;
}

.metric-value {
    color: #ffffff;
    font-weight: 800;
    font-size: 26px;
}

.report-box {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.86));
    padding: 26px;
    border-radius: 24px;
    border-left: 10px solid #c3a1ff;
    box-shadow: 0 16px 40px rgba(195, 161, 255, 0.10);
}

.footer {
    text-align: center;
    margin-top: 46px;
    color: rgba(255,255,255,0.62);
    font-size: 13px;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    border-radius: 18px;
    background: rgba(255,255,255,0.92);
    color: #252826;
}

div.stButton > button {
    background: linear-gradient(135deg, #efe4d4, #d7c7b1);
    color: #252826;
    border: none;
    padding: 0.72rem 1.15rem;
    border-radius: 16px;
    font-weight: 800;
    box-shadow: 0 12px 28px rgba(0,0,0,0.16);
}

.stInfo {
    background: rgba(255,255,255,0.13) !important;
    color: #fff8ee !important;
    border: 1px solid rgba(255,255,255,0.22) !important;
}

.stInfo div, .stInfo p {
    color: #fff8ee !important;
}
</style>
""", unsafe_allow_html=True)

# ===== ĐỌC QUERY PARAM =====
query_params = st.query_params
if "page" in query_params:
    st.session_state.page = query_params["page"]

# ===== NAV =====
def go_home():
    if st.button("← Quay về trang đầu"):
        st.query_params.clear()
        st.session_state.page = "home"
        st.rerun()

# ===== TRANG ĐẦU =====
def home_page():
    left, right = st.columns([1.12, 0.88])

    with left:
        st.markdown("""
        <div class="hero">
            <div class="pill">Lan Chi · Ritach Solutions · Personal Creative Space</div>
            <div class="brand">Một góc nhỏ để chữa lành, làm việc và tạo ra cái đẹp.</div>
            <div class="subtitle">
                Đây là không gian cá nhân của Lan Chi — nơi lưu clip, ảnh, lịch làm việc,
                những ý tưởng tài chính, và những khoảng nghỉ dịu dàng sau một ngày dài.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        try:
            st.image(HERO_IMAGE, use_container_width=True)
        except Exception:
            st.markdown("""
            <div class="box">
                <p class="note">Ảnh của Chi sẽ hiện ở đây khi file hinhanh.png nằm cùng thư mục với app.py trên GitHub.</p>
            </div>
            """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <a class="card-link" href="?page=healing" target="_self">
            <div class="card heal">
                <h3>Chữa lành</h3>
                <p>Mỗi ngày một đóa hoa, một lời chúc dịu và một ô nhỏ để Chi viết lại cảm xúc của mình.</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card work">
            <h3>Lịch công việc</h3>
            <p>Những clip cần dựng, ý tưởng cần giữ, việc cần làm trong ngày và các bước nhỏ để biến cảm hứng thành sản phẩm thật.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <a class="card-link" href="?page=asset" target="_self">
            <div class="card asset">
                <h3>Chuẩn bị tài sản</h3>
                <p>Các bảng tính tài chính để theo dõi vốn, điểm hòa vốn, dòng tiền và tài sản một cách rõ ràng hơn.</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card rest">
            <h3>Nghỉ ngơi</h3>
            <p>Ảnh đẹp, nhạc nhẹ, clip nhỏ, những điều làm mình dịu xuống — một khoảng riêng để không phải luôn chạy theo mọi thứ.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Cinema Wall</div>', unsafe_allow_html=True)

    video_url = st.text_input(
        "Dán link YouTube hoặc video của em vào đây:",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    if video_url:
        st.video(video_url)
    else:
        st.markdown("""
        <div class="box">
            <p class="note">Dán link video để hiện clip mới nhất của em ở đây. Khu này sẽ là bức tường cinema riêng của em.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Ghi chú hôm nay</div>', unsafe_allow_html=True)

    note = st.text_area(
        "Viết vài dòng cho ngày hôm nay:",
        placeholder="Hôm nay mình đã làm gì tốt? Ý tưởng nào cần giữ lại?"
    )

    if note:
        st.success("Đã ghi lại trong phiên này. Bản sau anh sẽ thêm lưu dữ liệu lâu dài cho em.")

    st.markdown("""
    <div class="footer">
        Vellichor tạo web tặng em · Copyright 2026 · Built with softness
    </div>
    """, unsafe_allow_html=True)

# ===== TRANG CHỮA LÀNH =====
def healing_page():
    go_home()

    name, symbol, wish = flowers[date.today().toordinal() % len(flowers)]

    st.markdown("""
    <div class="hero">
        <div class="pill">Chữa lành · Một góc dịu dành riêng cho Lan Chi</div>
        <div class="brand">Hoa hôm nay anh đặt ở đây cho em.</div>
        <div class="subtitle">
            Mỗi ngày mở trang này, Chi sẽ nhận một đóa hoa khác nhau cùng một lời chúc nhỏ để bắt đầu lại nhẹ hơn.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="flower-box">
        <div class="flower-symbol">{symbol}</div>
        <div class="flower-name">{name}</div>
        <p class="small-soft" style="font-size:17px; text-align:center; max-width:820px; margin:0 auto;">{wish}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Cảm xúc hôm nay</div>', unsafe_allow_html=True)

    feeling = st.text_area(
        "Chi viết cảm xúc của mình ở đây:",
        placeholder="Hôm nay mình đang thấy...",
        height=180
    )

    if feeling:
        st.success("Anh đã giữ dòng cảm xúc này trong phiên hiện tại của trang.")

    st.markdown("""
    <div class="footer">
        Vellichor tạo web tặng em · Chữa lành mỗi ngày
    </div>
    """, unsafe_allow_html=True)

# ===== TRANG TÀI SẢN =====
def asset_page():
    go_home()

    st.markdown("""
    <div class="hero">
        <div class="pill">Chuẩn bị tài sản · Công thức tài chính</div>
        <div class="brand">Các bảng tính để nhìn tiền rõ hơn.</div>
        <div class="subtitle">
            Bảng đầu tiên là công cụ thu hồi vốn: nhập vốn, số lượng và giá hiện tại để xem điểm hòa vốn,
            phần cần bán và phần tài sản còn lại.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Bảng tính 1 · Thu hồi vốn cổ phiếu</div>', unsafe_allow_html=True)

    left, right = st.columns([1.05, 0.95])

    with left:
        st.markdown("""
        <div class="finance-box">
            <p class="small-soft">Nhập vài con số để xem cần bán bao nhiêu, tài sản còn lại là bao nhiêu và hiện tại đã gần hòa vốn hay chưa.</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:
            ticker = st.text_input("Mã cổ phiếu", value="VND").upper()
            capital = parse_vnd(
                st.text_input("Tổng vốn đầu tư ban đầu (VNĐ)", value=format_vnd(100000000)),
                100000000
            )

        with c2:
            quantity = parse_vnd(
                st.text_input("Số lượng đang nắm giữ", value=format_vnd(5000)),
                5000
            )
            price = parse_vnd(
                st.text_input("Giá thị trường hiện tại (VNĐ)", value=format_vnd(35000)),
                35000
            )

    fee_tax = 0.0015 + 0.001

    need_sell = capital / (price * (1 - fee_tax)) if price > 0 else 0
    current_net = quantity * price * (1 - fee_tax)
    profit_loss = current_net - capital
    breakeven = ((capital / quantity) / (1 - fee_tax)) if quantity > 0 else 0
    remain_qty = max(quantity - need_sell, 0)
    remain_value = remain_qty * price

    with right:
        st.markdown('<div class="finance-box">', unsafe_allow_html=True)

        a, b = st.columns(2)

        with a:
            st.markdown(
                f'<div class="metric-shell"><div class="metric-label">Giá hòa vốn thực nhận</div><div class="metric-value">{breakeven:,.0f}đ</div></div>',
                unsafe_allow_html=True
            )

        with b:
            st.markdown(
                f'<div class="metric-shell"><div class="metric-label">Giá hiện tại</div><div class="metric-value">{price:,.0f}đ</div></div>',
                unsafe_allow_html=True
            )

        status = "Đã hòa vốn" if profit_loss >= 0 else "Chưa hòa vốn"

        st.markdown(
            f'<br><div class="metric-shell"><div class="metric-label">Trạng thái hiện tại</div><div class="metric-value">{status}</div></div>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Tính điểm thu hồi vốn"):
        if need_sell > quantity:
            st.error(
                f"Hiện tại tài sản chưa đủ để rút gốc. {ticker} cần đạt tối thiểu {breakeven:,.0f}đ để hòa vốn thực nhận sau phí."
            )
        else:
            st.markdown(f"""
            <div class="report-box">
                <table style="width:100%; border-collapse:collapse; font-family:Arial,sans-serif;">
                    <tr>
                        <td style="padding:15px; color:#49326b;"><b>Số lượng cần bán để rút gốc</b></td>
                        <td style="text-align:right; font-weight:bold; color:#a067d6;">{int(need_sell + 1):,.0f} CP</td>
                    </tr>
                    <tr>
                        <td style="padding:15px; color:#49326b;"><b>Chi phí giao dịch ước tính</b></td>
                        <td style="text-align:right; color:#a067d6;">~ {(capital * fee_tax):,.0f} đ</td>
                    </tr>
                    <tr>
                        <td style="padding:15px; color:#49326b;"><b>Tài sản còn lại sau khi rút gốc</b></td>
                        <td style="text-align:right; color:#9e7af3;"><b>{int(remain_qty):,.0f} CP</b></td>
                    </tr>
                    <tr>
                        <td style="padding:15px; color:#6a5ac9;">Giá trị phần còn lại theo giá hiện tại</td>
                        <td style="text-align:right; color:#9e7af3;">{remain_value:,.0f} đ</td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            st.success(
                f"Bán khoảng {int(need_sell + 1):,.0f} CP là thu hồi đủ vốn gốc. Phần còn lại là tài sản giữ tiếp."
            )

    st.markdown('<div class="section-title">Dashboard nhìn nhanh vốn và lãi lỗ</div>', unsafe_allow_html=True)

    chart_df = pd.DataFrame({
        "Hạng mục": ["Vốn gốc", "Giá trị hiện tại sau phí", "Lãi / Lỗ"],
        "Giá trị": [capital, current_net, abs(profit_loss)]
    })

    fig, ax = plt.subplots(figsize=(8, 4.8))
    bars = ax.bar(
        chart_df["Hạng mục"],
        chart_df["Giá trị"],
        color=["#efe4d4", "#c9c3b8", "#f5f0e7"]
    )

    fig.patch.set_alpha(0)
    ax.set_facecolor((1, 1, 1, 0.02))
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.tick_params(axis='x', colors='#fff8ee')
    ax.tick_params(axis='y', colors='#fff8ee')
    ax.set_ylabel('VNĐ', color='#fff8ee')
    ax.set_title('So sánh nhanh', color='#fff8ee')

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{bar.get_height():,.0f}",
            ha='center',
            va='bottom',
            color='#fff8ee',
            fontsize=10
        )

    st.pyplot(fig, use_container_width=True)

    if profit_loss >= 0:
        st.markdown(
            f"""
            <div class="box">
                <p style="color:#fff8ee; font-size:16px; margin:0;">
                    Hiện giá trị sau phí đang cao hơn vốn gốc khoảng {profit_loss:,.0f} đ.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div class="box">
                <p style="color:#fff8ee; font-size:16px; margin:0;">
                    Hiện còn cách hòa vốn khoảng {abs(profit_loss):,.0f} đ.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== ROUTER =====
if st.session_state.page == "healing":
    healing_page()
elif st.session_state.page == "asset":
    asset_page()
else:
    home_page()
