<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/cf613c9d-b1e7-43a5-a932-025c121e79fd"># [PHATE, PCA, tSNE, UMAP Visualizations of Bulk RNA Sequencing Data from Pediatric Acute Myeloid Leukemia (pAML) Patient Samples](https://aml-rnaseq-phate.onrender.com/)

### Authors
Ivan Ratushnyy

Alexander Ratushny

Hamid Bolouri

### Description
The [website](https://aml-rnaseq-phate.onrender.com/) allows PHATE, PCA, tSNE, UMAP visualization and exploration of bulk [RNA-seq data](https://www.nature.com/articles/s41467-022-34965-4) from pAML patient samples.

The RNA-seq data was initially processed. Genes with low expression (i.e., max gene expression value < 5.0) and low variability (i.e., standard deviation < 0.3) across samples were filtered out and not used in the analysis. The filtered RNA-seq data was converted into PHATE coordinates using the [Python PHATE package](https://phate.readthedocs.io/en/stable/), PCA coordinates using [sklearn.decomposition](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html), tSNE coordinates using [sklearn.manifold](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html), and UMAP coordinates using [umap-learn](https://umap-learn.readthedocs.io/en/latest/). [Plotly](https://plotly.com/) was used to visualize graphs based on these coordinates and the [Dash](https://dash.plotly.com/) framework was utilized to build the layout of the application. Lastly, the whole application was hosted on [Render](https://render.com/).

### Current functionality
#### Working with the modebar
The modebar contains multiple useful tools, and can be found when hovering over the top right of the screen. Instructions for using these tools can be found on the [Plotly website](https://plotly.com/chart-studio-help/getting-to-know-the-plotly-modebar/).

<img width="1486" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/fbdce2cd-7352-4ce4-8ca5-32ac74dfdbf2">


Box and lasso select tools have been changed for selected samples to be crossfiltered between plots. This will mean that when making a selection within a plot, that selection will also be highlighted for the remaining plots. An example is shown below.

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/d220bcb1-171e-435b-8447-e82f03c43e3f">


#### Using the sidebar
The sidebar currently allows to define the following attributes

<img width="222" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/e3d3c49b-99f1-4eed-8132-f281bcbd9679">

#### Display plots in 2 dimensions or 3 dimensions

2 dimensions

<img width="1485" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/6a44c452-35ed-4c6e-b5d8-95878de54b8c">

3 dimensions

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/06ade80b-e9bb-48e9-b787-15e117a84fe7">

#### Changing annotation types for samples

Examples:

Age (attribute with continuous values):

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/ae2222a4-6b3e-493b-894c-4fdf63a5c81a">

Sex (categorical attribute):

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/e899b796-32f3-4539-a814-5a4e13736ecd">

#### Sample annotation color changes based on a list of discrete and continous colormaps

Continous colormap change (built-in colorscale name: agsunset, changed from aggrnyl)

<img width="1486" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/ea0a8093-f32e-4664-b6bc-06fc2b47017d">

Discrete colormap change (built-in colormap name: D3, changed from plotly)

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/1439b40c-4084-4540-bf69-a164aaeeb2e9">

#### Option of changing the opacity and the size of the datapoints on the displayed graph

Higher transparency

<img width="1486" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/44e5fa50-6ce1-4f5c-a4e0-450992ba39d3">

Opaque datapoints

<img width="1484" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/9a7cc868-9298-43c3-8eea-ddef8e222be8">

Larger datapoints

<img width="1483" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/cdc4016f-e3c2-49dc-9644-96f9819b5abb">

Smaller datapoint size

<img width="1486" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/80bf96e0-afa3-4b66-ae81-2f857375c4d9">

### References
[RNA sequencing data](https://www.nature.com/articles/s41467-022-34965-4)

- [PHATE](https://www.krishnaswamylab.org/projects/phate) library to generate PHATE coordinates of the data
- [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) library to generate PCA coordinates of the data
- [tSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) library to generate tSNE coordinates of the data
- [UMAP](https://umap-learn.readthedocs.io/en/latest/) library to generate UMAP coordinates of the data

[Plotly](https://plotly.com/) and [Dash](https://dash.plotly.com/) for rendering the graphs and creating the layout of the application respectively

[Render](https://render.com/) for hosting the application

Other libraries such as pandas and numpy for processing and dealing with the data
