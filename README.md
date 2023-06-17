# [PHATE, PCA, tSNE, UMAP Visualizations of Bulk RNA Sequencing Data from Pediatric Acute Myeloid Leukemia (pAML) Patient Samples](https://aml-rnaseq-phate.onrender.com/)

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

<img width="1422" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/4f51c27c-11c9-4a0c-829e-2958496736f1">

#### Using the sidebar
The sidebar currently allows to define the following attributes

<img width="224" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/3fba4e05-77e2-45ae-97aa-f8a95c5763e1">

#### Display plots in 2 dimensions or 3 dimensions

2 dimensions

<img width="1415" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/8c4719b0-a8d5-4a99-8fcf-e34bfba07bc4">

3 dimensions

<img width="1417" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/b8b33df6-4e84-4b35-9230-38d52cb9a33b">

#### Changing annotation types for samples

Examples:

Age (attribute with continuous values):

<img width="1418" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/ebb7ac05-d92c-4527-a57f-663b960697dd">

Sex (categorical attribute):

<img width="1418" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/26a2b516-5c62-492a-aacd-53ccedf3b902">

#### Sample annotation color changes based on a list of discrete and continous colormaps

Continous colormap change (built-in colorscale name: agsunset)

<img width="1418" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/55a3f5b5-27e1-40f4-831a-50492ffa15d3">

Discrete colormap change (built-in colormap name: D3)

<img width="1416" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/2835ff64-39c5-4edc-ae42-4e5be5b31882">

#### Option of changing the opacity and the size of the datapoints on the displayed graph

Higher transparency

<img width="1418" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/29106aad-caf7-483d-93fe-6d48e0e0fc57">

Opaque datapoints

<img width="1420" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/e4951b09-b9b0-4c18-a447-07be681c00ac">

Larger datapoints

<img width="1421" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/f0c39388-dba8-41e7-8a16-4d00827bd4dc">

Smaller datapoint size

<img width="1415" alt="image" src="https://github.com/IvanRatushnyy/AML_RNAseq_PHATE/assets/108242614/40a21276-1f89-4d4d-9ae4-e10931e79d8f">

### References
[RNA sequencing data](https://www.nature.com/articles/s41467-022-34965-4)

- [PHATE](https://www.krishnaswamylab.org/projects/phate) library to generate PHATE coordinates of the data
- [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) library to generate PCA coordinates of the data
- [tSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html) library to generate tSNE coordinates of the data
- [UMAP](https://umap-learn.readthedocs.io/en/latest/) library to generate UMAP coordinates of the data

[Plotly](https://plotly.com/) and [Dash](https://dash.plotly.com/) for rendering the graphs and creating the layout of the application respectively

[Render](https://render.com/) for hosting the application

Other libraries such as pandas and numpy for processing and dealing with the data
