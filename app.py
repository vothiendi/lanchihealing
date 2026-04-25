import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(
    page_title="Lan Chi | Ritach Solutions",
    page_icon="✦",
    layout="wide"
)

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

if "show_asset_tool" not in st.session_state:
    st.session_state.show_asset_tool = False

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

label, .stTextInput label, .stTextArea label, .stFileUploader label {
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
    font-size: 58px;
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

.card {
    min-height: 215px;
    padding: 28px;
    border-radius: 30px;
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0 18px 48px rgba(0,0,0,0.18);
    transition: 0.25s ease;
    margin-bottom: 20px;
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
}

.card.asset {
    background: linear-gradient(135deg, rgba(118, 145, 145, 0.48), rgba(73, 91, 91, 0.45));
    color: #f4f1ea;
}

.card.rest {
    background: linear-gradient(135deg, rgba(239, 241, 236, 0.62), rgba(202, 202, 194, 0.50));
    color: #252826;
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

.video-box, .finance-box {
    padding: 24px;
    border-radius: 32px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.22);
    backdrop-filter: blur(18px);
    box-shadow: 0 18px 48px rgba(0,0,0,0.16);
}

.note {
    font-size: 14px;
    color: rgba(255,255,255,0.76);
    margin-top: 8px;
}

.report-box-harvest {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,255,255,0.86));
    padding: 26px;
    border-radius: 24px;
    border-left: 10px solid #c3a1ff;
    box-shadow: 0 16px 40px rgba(195, 161, 255, 0.10);
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

.small-soft {
    color: rgba(255,255,255,0.80);
    font-size: 14px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    margin-top: 46px;
    color: rgba(255,255,255,0.62);
    font-size: 13px;
}

img {
    border-radius: 24px;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    border-radius: 18px;
    background: rgba(255,255,255,0.92);
    color: #252826;
}

div[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.10);
    padding: 14px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.18);
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
</style>
""", unsafe_allow_html=True)

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

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card heal">
        <h3>Chữa lành</h3>
        <p>Một góc ánh sáng dịu để giữ lại lời khen cho bản thân, những điều nhỏ làm mình mềm lại, và vài phút thở chậm sau những ngày phải cố gắng.</p>
    </div>
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
    <div class="card asset">
        <h3>Chuẩn bị tài sản</h3>
        <p>Một nơi gọn gàng để theo dõi dòng tiền, tài sản, kế hoạch tài chính cá nhân và những cơ hội cần được quan sát kỹ hơn.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Mở bảng tính thu hồi vốn"):
        st.session_state.show_asset_tool = True

with col4:
    st.markdown("""
    <div class="card rest">
        <h3>Nghỉ ngơi</h3>
        <p>Ảnh đẹp, nhạc nhẹ, clip nhỏ, những điều làm mình dịu xuống — một khoảng riêng để không phải luôn chạy theo mọi thứ.</p>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.show_asset_tool:
    st.markdown('<div class="section-title">Bảng tính thu hồi vốn</div>', unsafe_allow_html=True)

    left, right = st.columns([1.05, 0.95])

    with left:
        st.markdown('<div class="finance-box">', unsafe_allow_html=True)
        st.markdown('<div class="small-soft">Nhập nhanh vài con số để xem cần bán bao nhiêu, tài sản còn lại là bao nhiêu và hiện tại đã gần hòa vốn hay chưa.</div>', unsafe_allow_html=True)

        input_col1, input_col2 = st.columns(2)

        with input_col1:
            ticker_ph = st.text_input("Mã cổ phiếu", value="VND").upper()
            tong_von_goc_text = st.text_input(
                "Tổng vốn đầu tư ban đầu (VNĐ)",
                value=format_vnd(100000000),
                placeholder="100,000,000"
            )
            tong_von_goc = parse_vnd(tong_von_goc_text, 100000000)

        with input_col2:
            so_luong_co_text = st.text_input(
                "Số lượng đang nắm giữ",
                value=format_vnd(5000),
                placeholder="5,000"
            )
            so_luong_co = parse_vnd(so_luong_co_text, 5000)

            gia_thi_truong_text = st.text_input(
                "Giá thị trường hiện tại (VNĐ)",
                value=format_vnd(35000),
                placeholder="35,000"
            )
            gia_thi_truong = parse_vnd(gia_thi_truong_text, 35000)

        st.markdown('</div>', unsafe_allow_html=True)

    phi_moi_gioi = 0.0015
    thue_ban = 0.001
    tong_phi_thue = phi_moi_gioi + thue_ban

    so_luong_ban = tong_von_goc / (gia_thi_truong * (1 - tong_phi_thue)) if gia_thi_truong > 0 else 0
    current_gross_value = so_luong_co * gia_thi_truong
    current_net_value = current_gross_value * (1 - tong_phi_thue)
    profit_loss = current_net_value - tong_von_goc
    gia_hoa_von_thuc = ((tong_von_goc / so_luong_co) / (1 - tong_phi_thue)) if so_luong_co > 0 else 0
    so_luong_con_lai = max(so_luong_co - so_luong_ban, 0)
    gia_tri_0_dong = so_luong_con_lai * gia_thi_truong

    with right:
        st.markdown('<div class="finance-box">', unsafe_allow_html=True)
        st.markdown('<div class="small-soft">Nếu giá hiện tại chưa đủ để rút gốc sau phí, bảng sẽ hiện ngay vùng còn thiếu. Nếu đủ rồi, khách hàng nhìn luôn được phần tài sản còn lại.</div>', unsafe_allow_html=True)

        m1, m2 = st.columns(2)

        with m1:
            st.markdown(
                f'''<div class="metric-shell"><div class="metric-label">Giá hòa vốn thực nhận</div><div class="metric-value">{gia_hoa_von_thuc:,.0f}đ</div></div>''',
                unsafe_allow_html=True
            )

        with m2:
            st.markdown(
                f'''<div class="metric-shell"><div class="metric-label">Giá hiện tại</div><div class="metric-value">{gia_thi_truong:,.0f}đ</div></div>''',
                unsafe_allow_html=True
            )

        st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)

        near_text = "Đã hòa vốn" if profit_loss >= 0 else "Chưa hòa vốn"
        color_note = "#fff1c7" if profit_loss >= 0 else "#ffd6d6"

        st.markdown(
            f'''<div class="metric-shell"><div class="metric-label">Trạng thái hiện tại</div><div class="metric-value" style="font-size:24px;color:{color_note};">{near_text}</div></div>''',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)

    if st.button("Tính điểm thu hồi vốn"):
        if so_luong_ban > so_luong_co:
            st.error(
                f"Hiện tại tài sản chưa đủ để rút gốc. {ticker_ph} cần đạt tối thiểu {gia_hoa_von_thuc:,.0f}đ để hòa vốn thực nhận sau phí."
            )
        else:
            st.markdown(f"""
            <div class="report-box-harvest">
            <table style="width:100%; border-collapse: collapse; font-family: Arial, sans-serif;">
                <tr style="border-bottom: 1px solid #efe7fb;">
                    <td style="padding: 15px; color: #49326b;"><b>Số lượng cần bán để rút gốc</b></td>
                    <td style="text-align: right; font-weight: bold; color: #a067d6;">{int(so_luong_ban + 1):,.0f} CP</td>
                </tr>
                <tr style="border-bottom: 1px solid #efe7fb;">
                    <td style="padding: 15px; color: #49326b;"><b>Chi phí giao dịch ước tính</b></td>
                    <td style="text-align: right; color: #a067d6;">~ {(tong_von_goc * tong_phi_thue):,.0f} đ</td>
                </tr>
                <tr style="background-color: #fff8fd; border-bottom: 1px solid #efe7fb;">
                    <td style="padding: 15px; color: #49326b;"><b>Tài sản còn lại sau khi rút gốc</b></td>
                    <td style="text-align: right; color: #9e7af3; font-size: 1.25em;"><b>{int(so_luong_con_lai):,.0f} CP</b></td>
                </tr>
                <tr>
                    <td style="padding: 15px; color: #6a5ac9;">Giá trị phần còn lại theo giá hiện tại</td>
                    <td style="text-align: right; color: #9e7af3;">{gia_tri_0_dong:,.0f} đ</td>
                </tr>
            </table>
            </div>
            """, unsafe_allow_html=True)

            st.success(
                f"Bán khoảng {int(so_luong_ban + 1):,.0f} CP là thu hồi đủ vốn gốc. Phần còn lại là tài sản giữ tiếp để chờ vùng lời đẹp hơn."
            )

    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
    st.markdown('<div class="finance-box">', unsafe_allow_html=True)
    st.markdown('<div class="section-title" style="margin-top:0;">Dashboard nhìn nhanh vốn và lãi lỗ</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-soft">Biểu đồ này để khách hàng nhìn sơ qua là biết tổng tài sản hiện tại đang dưới vốn, sát hòa vốn hay đã vượt lên vùng lời.</div>', unsafe_allow_html=True)

    chart_df = pd.DataFrame({
        "Hạng mục": ["Vốn gốc", "Giá trị hiện tại sau phí", "Lãi / Lỗ"],
        "Giá trị": [tong_von_goc, current_net_value, abs(profit_loss)]
    })

    fig, ax = plt.subplots(figsize=(8, 4.8))
    bars = ax.bar(
        chart_df["Hạng mục"],
        chart_df["Giá trị"],
        color=["#efe4d4", "#c9c3b8", "#f5f0e7"]
    )

    ax.set_facecolor((1, 1, 1, 0.02))
    fig.patch.set_alpha(0)
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.spines['bottom'].set_color('#e6dfd2')
    ax.tick_params(axis='x', colors='#fff8ee', labelsize=11)
    ax.tick_params(axis='y', colors='#fff8ee', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.18)
    ax.set_ylabel('VNĐ', color='#fff8ee')
    ax.set_title('So sánh nhanh', color='#fff8ee', fontsize=14, pad=12)

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:,.0f}",
            ha='center',
            va='bottom',
            color='#fff8ee',
            fontsize=10
        )

    st.pyplot(fig, use_container_width=True)

    if profit_loss >= 0:
        st.info(f"Hiện giá trị sau phí đang cao hơn vốn gốc khoảng {profit_loss:,.0f} đ. Khách hàng nhìn vào là biết đã qua vùng hòa vốn.")
    else:
        st.info(f"Hiện còn cách hòa vốn khoảng {abs(profit_loss):,.0f} đ. Nhìn biểu đồ là thấy đang tiến gần vùng cân bằng hay chưa.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Cinema Wall</div>', unsafe_allow_html=True)

video_url = st.text_input(
    "Dán link YouTube hoặc video của em vào đây:",
    placeholder="https://www.youtube.com/watch?v=..."
)

if video_url:
    st.markdown('<div class="video-box">', unsafe_allow_html=True)
    st.video(video_url)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="video-box">
        <p class="note">Dán link video để hiện clip mới nhất của em ở đây. Khu này sẽ là bức tường cinema riêng của em.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Moodboard ảnh</div>', unsafe_allow_html=True)

uploaded_images = st.file_uploader(
    "Tải ảnh moodboard của em lên:",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_images:
    cols = st.columns(3)
    for i, img in enumerate(uploaded_images):
        with cols[i % 3]:
            st.image(img, use_container_width=True)
else:
    st.markdown(
        '<p class="note">Chưa có ảnh nào. Khi em tải ảnh lên, chúng sẽ hiện thành moodboard mềm ở đây.</p>',
        unsafe_allow_html=True
    )

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
