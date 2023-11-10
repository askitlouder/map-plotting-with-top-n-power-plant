import numpy as np
import pandas as pd



def top_n_plants(N,generator_info_2021,plants_info_2021,state_info21):
    try:
        # generator_info_req_data = generator_info_2021[["Plant name","Plant state abbreviation","Generator annual net generation (MWh)"]]
        plants_info_req_data = plants_info_2021[["Plant name","Plant state abbreviation","Plant annual net generation (MWh)","Plant latitude","Plant longitude"]]
        state_info_req_data = state_info21[["State abbreviation","State annual net generation (MWh)"]]

        #remove row 1 from both the dataframes
        plants_info_req_data = plants_info_req_data.drop([0])
        state_info_req_data = state_info_req_data.drop([0]) 


        #Sort both the dataframe from highest to lowest
        plants_info_req_data = plants_info_req_data.sort_values(by="Plant annual net generation (MWh)",ascending=False)
        state_info_req_data = state_info_req_data.sort_values(by="State annual net generation (MWh)",ascending=False)
        #describe the dataframes
        # print("pant>>>",plants_info_req_data.describe())
        # print("state>>>",state_info_req_data.describe())

        #Based on value of N filter out top top N plants
        top_n_data_all = plants_info_req_data.head(N)
        top_n_states = state_info_req_data.head(N)
        return top_n_data_all, top_n_states
    except Exception as e:
        return "Issue in data extraction"