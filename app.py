import streamlit as st

st.set_page_config(
    page_title="Lan Chi | Ritach Solutions",
    page_icon="✦",
    layout="wide"
)

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
    background: linear-gradient(135deg,
        rgba(176, 190, 178, 0.52),
        rgba(124, 139, 132, 0.42)
    );
    color: #fff8ee;
}

.card.heal h3,
.card.heal p {
    color: #fff8ee;
}

.card.work {
    background: linear-gradient(135deg,
        rgba(232, 226, 214, 0.72),
        rgba(197, 190, 178, 0.58)
    );
    color: #242724;
}

.card.work h3,
.card.work p {
    color: #242724;
}

.card.asset {
    background: linear-gradient(135deg,
        rgba(118, 145, 145, 0.48),
        rgba(73, 91, 91, 0.45)
    );
    color: #f4f1ea;
}

.card.asset h3,
.card.asset p {
    color: #f4f1ea;
}

.card.rest {
    background: linear-gradient(135deg,
        rgba(239, 241, 236, 0.62),
        rgba(202, 202, 194, 0.50)
    );
    color: #252826;
}

.card.rest h3,
.card.rest p {
    color: #252826;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    margin: 42px 0 16px;
    color: #fff8ee;
}

.video-box {
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
