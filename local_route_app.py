import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
import pickle
#from datetime import datetime
#from datetime import date
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from statistics import *

st.title('Cracked Tracks')


file_name = '/home/jon/PycharmProjects/jon-insight-project/data/processed/pa_course_database_processed.plk'
loaded_data = pd.read_pickle(file_name)

# user_input = st.selectbox('Which commuter rail?', loaded_data['Trains'].unique())
# #user_input = st.text_input("Which commuter rail interests you? Enter a location like 'CR-Lowell', 'CR-Framingham'")
# st.write(user_input)
#
# print(loaded_data)
#
# Data = pd.DataFrame(loaded_data)
# #user_input2=st.selectbox('Which commuter rail?', Data['Trains'].unique())
# #st.write(user_input2)
#
#
# Train_df = pd.DataFrame()
# for train in set(Data["Trains"]):
#   print(train)
#   if user_input == train:
#     mask = Data["Trains"] == train
#     Train_df = Data[mask]
# st.write(Train_df)
# #st.write(Train_df)
#
# train_dict = {}
# train_dict["Reliability"] = list()
# train_dict["Frequency"] = list()
# train_dict["Peak"] = list()
# train_dict["Lag_Total_Hours_of_Service_Interruption"] =list()
#
# yearmask = Train_df['Year'] == 2019
# monthmask = Train_df['Month'] == 11
# mask1 = (yearmask) & (monthmask)
# df = Train_df[mask]
# train_dict["Reliability"].append(df['Reliability'])
# train_dict["Frequency"].append(df['Frequency'])
# train_dict["Peak"].append(df['Peak'])
# train_dict["Lag_Total_Hours_of_Service_Interruption"].append(df['Lag'])
#
# output = pd.DataFrame(df['Reliability'], df['Frequency'], df['Peak'], df['Lag'])
# print(output)
#
# pkl_filename = 'C:/Users/ritwi/Documents/Commuter_Rails/Commuter_basic_linear_fit.pkl'
# with open(pkl_filename, 'rb') as file:
#     pickle_model = pickle.load(file)
# prediction = pickle_model.predict(np.array([Train_df.iloc[-1,:].Reliability,Train_df.iloc[-1,:].Frequency,Train_df.iloc[-1,:].Peak,Train_df.iloc[-1,:].Lag]).reshape(1,4))
# st.write(f"The number of hours {user_input} is going to be down for is {prediction.item(0)} hrs")
#
# #month = pd.to_datetime(prediction, format = '%j').month
# #day = pd.to_datetime(prediction, format = '%j').day
# #st.write(calendar.month_name[month], day, user_input2)