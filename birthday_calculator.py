
import streamlit as st
import datetime
import calendar as c   
import time




#Take a look at your chrome tab. With the code below you can change the header of the page
st.set_page_config(
        page_title='When were you born?',
        page_icon="👶"
        )




col1, col2, col3, col4, col5 = st.columns([1,1,5,1,1])


with col1:
        st.write("")

with col5:
        st.write("")        


with col3:
    



        #Display a GIF on top of the app
        st.markdown("![Alt Text](https://media.giphy.com/media/KbRBekX2PQtjVdlV8i/giphy.gif?cid=790b7611d454a209ea5ffa7a79b7330d4bc0a9f4ab0190be&rid=giphy.gif&ct=g)")


        #Title of your app + one whitespace
        st.markdown("<h1 style='text-align: center; color: black;'>On which day were you born?</h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)


        #Take input of the user
        year = st.number_input('Year', min_value=1900, max_value=2021, step=1)
        month = st.number_input('Month', min_value=1, max_value=12, step=1)
        day = st.number_input('Day', min_value=1, max_value=31, step=1)


        #i used these lines for additional whitespace between the result and the text boxes
        st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)


        d = datetime.date(year, month, day)

        st.write('Your were born on a ... ' + c.day_name[d.weekday()])

        #whitespace again
        st.markdown("<h3 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'>                 </h5>", unsafe_allow_html=True)


        #instagram link
        link = '[Just a tiny example app for my Instagram post](https://www.instagram.com/max_mnemo)'
        st.markdown(link, unsafe_allow_html=True)


