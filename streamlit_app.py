import streamlit as st

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocate Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]


st.dataframe(fruits_to_show)


st.header("Fruityvice Fruit Advice!")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)



import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#normalize the json query
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# populate a new dataframe with the normalized json
st.dataframe(fruityvice_normalized)









import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()

st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

#allow the end user to add a fruit to the list

add_my_fruit = st.text_input('What fruit would you like to add?','enter fruit here')
st.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

