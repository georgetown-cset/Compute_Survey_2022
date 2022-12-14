# 💽 CSET-HAI 2022 Compute Survey Repository

This repository includes all associated materials for the compute survey run by CSET and HAI in June and July of 2022. Specifically, this repository hosts:

1. 🙋 SQL scripts used for identifying potential respondents in the population of interest;
2. ❓ The survey instrument;
3. 📊 Analytical scripts (in Python and R) for cleaning, visualizing, and analyzing survey responses; and
4. 📈 Additional scripts and visualizations produced but not included in the paper, which are provided here to give interested readers a more complete view of the data.

### Using This Repository

We are **not** releasing raw data associated with survey responses, due to anonymity concerns. As a result, this repository primarily functions 1) to offer transparency regarding the analysis methods employed in this research and 2) to provide additional analytical results not included in our final paper. This repository does contain a dataset of synthetically-generated fake response data, which was produced by independently sampling each response from our survey. Scripts can be executed to produce visualizations based on this synthetic data to verify the proper functioning of all code, but the results will be meaningless.

### Organization

This repository is organized as follows:

```
.                                   <- Project root
├── data                            <- Synthetic data and associated CSVs for interpreting results
|   ├── README.md                   <- Documentation explaining the meaning of each column in synthetci_data.csv
|   ├── synthetic_data.csv          <- Synthetically generated data mimicking the layout of our final, cleaned dataset
|   ├── field_composition.csv       <- CSV file showing the number of industry, academic, and government respondents in each field and subfield
|   └── answer_key.csv              <- CSV file for use in interpreting some responses
├── scripts                         <- Folder containing all associated code
|   ├── targeting                   <- SQL scripts used to identify potential respondents
|   ├── data_cleaner.py             <- Python script to reformat raw data into a cleaned .csv
|   ├── paper_figures.ipynb         <- Jupyter notebook containing code for visualizations (and hypothesis testing) included in the final report
|   ├── supplemental_figures.ipynb  <- Jupyter notebook containing code for supplemental visualizations
|   ├── modeling.Rmd                <- R markdown file used to produce models used to interpret some additional results
|   └── modeling.html               <- Outputs including model summaries of modeling.Rmd
├── results                         <- Folder containing visualizations
|   ├── figures                     <- Folder containing TKTK total visualizations included in the final report
|   └── supplemental_figures        <- Folder containing TKTK additional visualizations not included in the final paper
├── INSTRUMENT.pdf                  <- PDF of the complete survey instrument
├── README.md                       <- Top-level project documentation (this file)
└── requirements.txt                <- Python requirements file
```
