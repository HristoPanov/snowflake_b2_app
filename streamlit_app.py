import streamlit

streamlit.title("Diner 01")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 something")
streamlit.text("🥗 Kale, Spinach and Smoothie something")
streamlit.text("🐔 Hard Boiled Eggs something")
streamlit.text("🥑🍞 Avocado and Bread something")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc['fruits_selected']

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

