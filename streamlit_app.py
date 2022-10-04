
import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')

   
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Nomega 3 and Blueberry Oatmeal')
streamlit.text('🥗 kale, Spianch and Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)




