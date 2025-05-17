import streamlit as st
from components.sidebar import render_sidebar 



def main():
    render_sidebar()
    st.title("💼 Chào mừng đến với Ứng dụng Đầu Tư")
    st.markdown(
        """
        ### 👈 Chọn một trang từ menu bên trái:
        - **Phân tích** chỉ số tài chính
        - **Dự đoán** xu hướng
        - **Tối ưu hóa** danh mục đầu tư
        """
    )

if __name__ == "__main__":
    main()