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
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to display fuityvice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json()) # just text display
#normalize json response
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#display the table
#streamlit.dataframe(fruityvice_normalized)

fruit_choise = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choise)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choise)
#normalize json response
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#display the table
streamlit.dataframe(fruityvice_normalized)

#import connector
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# add another entry list
fruit_choise_2 = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ',fruit_choise_2)
#insert the entered value in the relevant table
my_cur.execute("INSER INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')");

