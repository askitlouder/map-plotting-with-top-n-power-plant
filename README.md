# map-plotting-with-top-n-power-plant
In simple words, within this repo, we have a codebase related to filter out top N power plant based on net annual generation. And then visualize  it on map.

Suppose we want to show a map to visualize the annual net generation of power plants of the US.

The challenge consists of the following requirements:

• We want to display the top N plants.
• On the map we want to show absolute value and percentage of the plant's federal state.
• We want to be able to filter by state so we can zoom in.
• The data usually comes as excel file: https://www.epa.gov/energy/emissions-generationresource-integrated-database-egrid (eGRID2021_data.xlsx Data File)
• Build JUST a python backend that backs this map with a REST API.
• Bonus: deployment of the solution in a cloud service

Once you cone the repo and integrate the environment based on requirement.txt, then execute main.py by setting up the value of N. 
The output store in the form the HTML in your working directory.
