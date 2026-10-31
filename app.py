import streamlit as st

page_1=st.Page("page_1.py", title="1페이지")
page_2=st.Page("page_2.py",title="2페이지")
page_3=st.Page("page_3.py",title="3페이지")

pages = st.navigation([page_1, page_2, page_3])

pages.run()