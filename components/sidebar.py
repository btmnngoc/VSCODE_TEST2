import streamlit as st

def render_sidebar():
    st.sidebar.title("📁 Điều hướng")
    st.sidebar.page_link("app.py", label="🏠 Trang chính")
    st.sidebar.page_link("pages/1_📈_Phan_Tich.py", label="📊 Phân tích tài chính")
    st.sidebar.page_link("pages/2_📉_Du_Doan.py", label="📈 Dự đoán xu hướng")
    st.sidebar.page_link("pages/3_💡_Toi_Uu_Dau_Tu.py", label="💡 Tối ưu đầu tư")