import streamlit as st

st.title("Ứng dụng quản lý công việc")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

name = st.text_input(label="Nhập tên công việc: ")
uu_tien = st.slider(label="Chọn mức độ ưu tiên: ", min_value=1, max_value=5, step=1)
option = st.selectbox(label="Chọn trạng thái: ", options=("Chưa làm", "Đang làm", "Hoàn thành"))

if st.button("Thêm công việc"):
    st.session_state.tasks.append({"Tên": name, "Ưu tiên": uu_tien, "Trạng thái": option})

if st.session_state.tasks:
    st.subheader("Danh sách công việc")
    for i, task in enumerate(st.session_state.tasks):
        st.write(f"{i + 1}. {task['Tên']} - Ưu tiên: {task['Ưu tiên']} - Trạng thái: {task['Trạng thái']}")

    if st.button("Xóa danh sách"):
        st.session_state.tasks = []
        