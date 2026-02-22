import streamlit as st 

# st.title("Ứng dụng đầu tiên của tôi")
# st.write("Thành công chạy ứng dụng Streamlit đầu tiên")

st.title("Ung dung quan ly cong viec")
if "admin" not in st.session_state:
    st.session_state.admin = []
with st.form(key = "Job form"):
    job = st.text_input("Nhap ten cong viec: ")
    pri = st.slider("Chon muc do uu tien",1,5)
    sta = st.selectbox("Chon trang thai cong viec: ",["Chua lam", "Dang lam", "Hoan thanh"])
        
    button = st.form_submit_button(label = "Them cong viec")

if button:
    dic = {"Dealine": job, "Priority": str(pri), "Status": sta }
    st.session_state.admin.append(dic)
    st.table(st.session_state.admin)
    
xoa = st.button("Xoa danh sach")
if xoa:
    st.session_state.admin = []
    if st.session_state.admin == []:
        st.text("Ban da xong viec!")
        