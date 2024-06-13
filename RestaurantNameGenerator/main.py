import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")
st.text("helps you choose your restaurant name and menu :)")
# st.sidebar.selectbox("Pick a Cuisine",("Indian","American","Mexican","Italian","Chinese","Arabic","Korean"))
cuisine=st.selectbox("👇 Pick a cuisine",("Indian","American","Mexican","Italian","Chinese","Arabic","Korean"))

if cuisine:
    response=langchain_helper.getNameAndItems(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write("Menu Items:")
    for item in menu_items:
        st.write("-",item)
