# 💽 CSET-HAI 2022 Compute Survey Repository

This repository includes all associated materials for the compute survey run by CSET and HAI in June and July of 2022. Specifically, this repository hosts:

1. 🙋 SQL scripts used for identifying potential respondents in the population of interest;
2. ❓ The survey instrument; and
3. 📊 Analytical scripts (in Python and R) for cleaning, visualizing, and analyzing survey responses.

### Using This Repository

We are **not** releasing raw data associated with survey responses, due to IRB restrictions associated with this survey project. As a result, this repository primarily functions 1) to offer transparency regarding the analysis methods employed in this research and 2) to provide additional analytical results not included in our final paper.

### Organization

This repository is organized as follows:

```
.                                   <- Project root
├── data                            <- Additional details regarding the data structure and demographics of our respondents with respect to research subfields
|   ├── README.md                   <- Documentation explaining the meaning of each column in the final, cleaned data file
|   └── field_composition.csv       <- CSV file showing the number of industry, academic, and government respondents in each field and subfield
├── scripts                         <- Folder containing all associated code
|   ├── targeting                   <- SQL scripts used to identify potential respondents
|   ├── codebook.ipynb              <- Jupyter notebook containing primary Python code for all preprocessing, data visualization, and analysis
|   └── modeling.Rmd                <- R markdown file used to produce models used to interpret some additional results
├── results                         <- Folder containing visualizations
|   ├── figures                     <- Folder containing 16 total visualizations included in the final report
|   ├── modeling.html               <- Outputs including model summaries of modeling.Rmd
|   └── supplemental_figures        <- Folder containing 26 additional visualizations not included in the final paper
|       ├── with_snowball           <- Folder for all paper visualizations (except Appendix C) reproduced including snowball responses
|       └── no_partial_responses    <- Folder for all paper visualizations (except Appendix C) reproduced using only complete responses
├── INSTRUMENT.pdf                  <- PDF of the complete survey instrument
├── README.md                       <- Top-level project documentation (this file)
└── requirements.txt                <- Python requirements file
```
