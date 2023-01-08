# PHATE Visualization of Bulk RNA Sequencing Data from Pediatric Acute Myeloid Leukemia (pAML) Patient Samples
[Website](https://aml-rnaseq-phate.onrender.com/)

### Authors
Ivan Ratushnyy
Alexander Ratushny
Hamid Bolouri

### Current functionality
* Selection of whether the PHATE graph is displayed in 2 dimensions or 3 dimensions
<img width="1084" alt="2D graph" src="https://user-images.githubusercontent.com/108242614/211180745-baa1d650-28cf-4393-9b66-08223d2af93e.png">
<img width="1084" alt="3D graph" src="https://user-images.githubusercontent.com/108242614/211180755-1d7f1466-874a-4e80-a515-629bf8775eff.png">

* Annotation color changes based on a list of discrete and continous colormaps
Continous colormap change
<img width="1137" alt="Continuous color" src="https://user-images.githubusercontent.com/108242614/211180847-037f6f7f-d3a2-4ab3-ae62-5fced587dfc2.png">

Default discrete colormap
<img width="1210" alt="Default discrete" src="https://user-images.githubusercontent.com/108242614/211181136-eafd44e6-a69d-486d-8852-4bc64baa2480.png">
Discrete colormap change
<img width="1211" alt="Changed discrete" src="https://user-images.githubusercontent.com/108242614/211181145-2a80a5b9-7329-490c-9469-2075c8260a34.png">

* Option of changing the opacity and the size of the datapoints on the displayed graph
Higher transparency
<img width="1208" alt="Transparent" src="https://user-images.githubusercontent.com/108242614/211181260-fc8693a6-8415-422a-a366-2884e9d2fbf0.png">
Opaque datapoints
<img width="1216" alt="Opaque" src="https://user-images.githubusercontent.com/108242614/211181268-7b133c75-8895-48c7-9bd7-3517270acd9f.png">

Larger datapoints
<img width="1205" alt="Larger datapoints" src="https://user-images.githubusercontent.com/108242614/211181311-b4691ab6-ce22-4447-93bf-10361b99d096.png">
Smaller datapoint size
<img width="1208" alt="Smaller datapoints" src="https://user-images.githubusercontent.com/108242614/211181315-03a6cabf-7fba-4068-b774-3c7e079b755d.png">

### References
[RNA sequencing data](https://www.nature.com/articles/s41467-022-34965-4)
[PHATE](https://www.krishnaswamylab.org/projects/phate) library to generate coordinates of the data
[Plotly](https://plotly.com/) and [Dash](https://dash.plotly.com/) for rendering the graphs and creating the layout of the application respectively
[Render](https://render.com/) for hosting the application
Other libraries such as pandas and numpy for processing and dealing with the data
