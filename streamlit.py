from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd
import streamlit as st
import openpyxl

# Define the training data
soil_moisture = np.array([30, 60, 80, 20, 40, 70, 50, 90, 10, 60, 80, 20, 40, 70, 50, 90, 10, 60, 80, 20, 40, 70, 50, 90, 10, 60, 80, 20, 40, 70, 50, 90, 10, 60, 80, 20, 40, 70, 50, 90, 10, 60, 80, 20, 40, 70, 50, 90])
plant_type = np.array(['tomatoes', 'sunflowers', 'beans', 'radishes', 'lettuce', 'cucumbers', 'peppers', 'pumpkins', 'carrots', 'spinach', 'squash', 'onions', 'broccoli', 'corn', 'watermelon', 'cabbage', 'beets', 'eggplant', 'okra', 'garlic', 'kale', 'zucchini', 'strawberries', 'cauliflower', 'celery', 'peas', 'artichokes', 'asparagus', 'brussels sprouts', 'potatoes', 'rhubarb', 'sweet potatoes', 'tarragon', 'rosemary', 'cilantro', 'chives', 'dill', 'parsley', 'sage', 'thyme','mint', 'oregano', 'basil', 'lemon balm', 'catnip', 'lavender', 'marjoram', 'bee balm'])

# Create an instance of the DecisionTreeClassifier algorithm
clf = DecisionTreeClassifier(random_state=42)

# Fit the algorithm to the training data
clf.fit(soil_moisture.reshape(-1, 1), plant_type)

# Load the Excel workbook
workbook = openpyxl.load_workbook(r'C:\Users\GOBALA KRISHNAN\OneDrive\Desktop\TEMP\NAAC\ESP8266toSupabase-main\Book2.xlsx')

# Select the sheet you want to read from
sheet = workbook['Sheet 1']

# Check if the sheet is not empty
if sheet.max_row < 2:
    st.warning("The Excel sheet is empty. Please populate data first.")
else:
    # Read the soil moisture value from the last row
    num = sheet.iloc[-1, 4]  # Assuming 'E' is the column for soil moisture

    # Define a new data point to predict the plant type
    new_data = np.array([num]).reshape(-1, 1)

    # Use the trained algorithm to predict the plant type of the new data point
    predicted_plant_type = clf.predict(new_data)

    st.title("Your Soil Moisture Value is: " + str(num))
    st.write('The best fitted plant type for the soil moisture:', predicted_plant_type[0])