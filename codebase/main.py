import numpy as np
import pandas as pd
import os
import folium
from fastapi import FastAPI


from data_extract import top_n_plants
from map_integration import map_plotter


#Multiple sheet names and total excel data 
def get_sheet_names_info(data_file_pth):
    excel_data = pd.ExcelFile(data_file_pth)
    sheet_names = excel_data.sheet_names
    return sheet_names, excel_data

app = FastAPI()

@app.get("/")
def power_plant_on_map(N:int):
    try:
        data_file_pth = 'eGRID2021_data.xlsx'
        sheet_name_info,excel_file_data = get_sheet_names_info(data_file_pth)
        
        generator_info21 = excel_file_data.parse(sheet_name_info[2])
        plants_info21 = excel_file_data.parse(sheet_name_info[3])
        state_info21 = excel_file_data.parse(sheet_name_info[4])
        

        #Extract Data based on 
        top_n_data_all, top_n_states = top_n_plants(N,generator_info21,plants_info21,state_info21)
        map_data = map_plotter(top_n_data_all, top_n_states)
        print("map_data>>>",map_data)
        map_data.save('Top_power_plant.html')
        return "Map save successfully"
    except Exception as e:
        return "Issue in api, enter interger value"

