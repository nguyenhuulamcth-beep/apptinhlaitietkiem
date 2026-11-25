
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Tính lãi đơn và lãi kép",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("💰 ỨNG DỤNG TÍNH LÃI ĐƠN VÀ LÃI KÉP")
st.write("So sánh số tiền khách hàng nhận được khi gửi tiết kiệm.")

st.divider()

# Nhập dữ liệu
st.subheader("📥 Nhập thông tin gửi tiết kiệm")

C = st.number_input(
    "Số tiền gửi ban đầu (đồng):",
    min_value=0,
    value=100_000_000,
    step=10_000_000,
    format="%d"
)

i_percent = st.number_input(
    "Lãi suất (%/năm):",
    min_value=0.0,
    value=1.0,
    step=0.1
)

n = st.number_input(
    "Thời gian gửi (năm):",
    min_value=0,
    value=3,
    step=1
)

# Chuyển lãi suất từ % sang số thập phân
i = i_percent / 100

st.divider()

# Nút tính toán
if st.button("🧮 TÍNH TOÁN", use_container_width=True):

    # Công thức tính lãi đơn
    An = C * (1 + i * n)

    # Công thức tính lãi kép
    Bn = C * ((1 + i) ** n)

    # Tính tiền lãi
    lai_don = An - C
    lai_kep = Bn - C

    # Hiển thị kết quả
    st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

    col1, col2 = st.columns(2)

    with col1:
        st.success("LÃI ĐƠN")
        st.metric(
            label="Số tiền nhận được",
            value=f"{An:,.0f} đồng"
        )
        st.write(f"Tiền lãi: **{lai_don:,.0f} đồng**")

    with col2:
        st.info("LÃI KÉP")
        st.metric(
            label="Số tiền nhận được",
            value=f"{Bn:,.0f} đồng"
        )
        st.write(f"Tiền lãi: **{lai_kep:,.0f} đồng**")

    st.divider()

    # So sánh kết quả
    st.subheader("📈 SO SÁNH")

    chenhlech = Bn - An

    st.write(
        f"Số tiền nhận được theo lãi kép cao hơn lãi đơn: "
        f"**{chenhlech:,.0f} đồng**"
    )

    if Bn >= An:
        st.success("Lãi kép mang lại số tiền nhận được cao hơn hoặc bằng lãi đơn.")
    else:
        st.warning("Lãi đơn mang lại số tiền nhận được cao hơn lãi kép.")
