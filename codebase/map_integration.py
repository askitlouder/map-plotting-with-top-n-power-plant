import numpy as np
import pandas as pd
import os
import folium
from folium.plugins import MarkerCluster
from folium import plugins



def map_plotter(top_n_plant_data, top_n_states):
    try:
        # Create a map centered at the mean latitude and longitude
        map_center = [top_n_plant_data['Plant latitude'].mean(), top_n_plant_data['Plant longitude'].mean()]
        my_map = folium.Map(location=map_center, zoom_start=5)

        # Create a MarkerCluster for grouping markers
        marker_cluster = plugins.MarkerCluster().add_to(my_map)

        # Add markers for each data point
        for index, row in top_n_plant_data.iterrows():
            # Extract latitude and longitude for the current row
            lat, lon = row['Plant latitude'], row['Plant longitude']
            
            # Calculate absolute value and percentage for the plant's federal state
            absolute_value = row['Plant annual net generation (MWh)']  # Replace with the actual column name
            state_name = row['Plant state abbreviation']  # Replace with the actual column name
            plant_name = row['Plant name']

            # Create HTML content for the popup
            popup_content = f"Plant_name:{plant_name} Plant annual net generation (MWh): {absolute_value} Plant state abbreviation: {state_name}"

            # Add marker with popup to the MarkerCluster
            folium.Marker([lat, lon], popup=folium.Popup(popup_content, parse_html=True)).add_to(marker_cluster)

        
        return my_map
    except ZeroDivisionError as e:
        return "Issue in map plotting"