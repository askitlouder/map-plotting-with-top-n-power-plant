# map-plotting-with-top-n-power-plant
In simple words, within this repo, we have a codebase related to filtering out top N power plants based on net annual generation. And then visualize  it on map.

Suppose we want to show a map to visualize the annual net generation of power plants of the US.

The challenge consists of the following requirements:

  • We want to display the top N plants.
  • On the map we want to show absolute value and percentage of the plant's federal state.
  • We want to be able to filter by state so we can zoom in.
  • The data usually comes as excel file: https://www.epa.gov/energy/emissions-generationresource-integrated-database-egrid (eGRID2021_data.xlsx Data File)
  • Build JUST a python backend that backs this map with a REST API.
  • Bonus: deployment of the solution in a cloud service

Once you cone the repo and integrate the environment based on requirement.txt, then execute main.py by setting up the value of N. One Excel file is also present, which use as input.

open terminal and run
uvicorn run main:app --host:0.0.0.0 --port:8009(set port as per need)

once the application starts running after,
open the browser, 
http://localhost:8009/docs   [port, set as per your need]
once open, then drag the available function and click on try it out.
put the value of N in an integer.
and output will be saved in the working dir



The output is stored in the form of the HTML in your working directory.



RUN from docker

Here, for dcoker image , it is set on port 8009.

Clone from there
docker image  -https://github.com/users/askitlouder/packages/container/package/map-plotting-with-top-n-power-plant%2Fpower_plant_map

Steps - Pull the docker image and run

docker run -p 8009:8009 docker pull ghcr.io/askitlouder/map-plotting-with-top-n-power-plant/power_plant_map:1.0

For this image, the port must be 8009

Important points - 
Ensure that Docker is installed on your machine.
If you are running on Windows or macOS, make sure your Docker Desktop is running. 
The above commands with Dockerfile has configured the container to expose a service on port 8009.
