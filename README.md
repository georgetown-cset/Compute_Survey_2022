## 🧶 Template for data processing and analysis

This is a [template repository](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates) for working in Python to gather, process, and analyze data.
To use it in a project, open its repo page on Github.com and click the green "Use this template" button.
After creating your new repo, replace this top section of `README.md` with project documentation.

As always, discussion, suggestions, and changes are welcome. Just create an issue or PR.

The text below and everything else in the repo are template content.

### Getting started

- Clone the project repo
- Create a new Python 3.7 virtual environment and install requirements:

```bash
# using conda:
conda create -n {project-name} python=3.7 --file requirements.txt
conda activate {project-name}

# or using virtualenv:
python3.7 -m venv ~/.virtualenvs/{project-name}
source ~/.virtualenvs/{project-name}/bin/activate
pip install -r requirements.txt
```

- Optionally, create an `.env` file in the project root that defines environment variables; they will be accessible from Python via `os.environ[]` after importing `./settings.py`, e.g. with `import settings`  
- Populate data directories with any data excluded from the project repo:

```bash
# Requires activated environment
python data/main.py
```

- Reproduce any analytic outputs excluded from the project repo:

```bash
# Requires activated environment
python analysis/main.py
```

### Organization

```
.                       <- Project root
├── analysis            <- Scripts/notebooks for analysis of final data
│   ├── figures         <- Figures created during analysis 
│   ├── tables          <- Tables created during analysis (e.g., of summary statistics or estimates)
│   └── main.py         <- Entry point for analysis code
├── data                <- Scripts to download or process data
│   ├── final           <- Final datasets
│   │   └── README.md   <- Documentaton for source data; organization, etc.
│   ├── interim         <- Intermediate transformed data
│   │   └── README.md   <- Documentaton for interim data; organization, etc.
│   ├── reference       <- Data dictionaries, user guides, lookup tables, and other references
│   │   └── README.md   <- Documentaton for source data; organization, etc.
│   ├── source          <- Original, immutable data dump
│   │   └── README.md   <- Documentaton for source data; organization, etc.
│   └── main.py         <- Entry point for data collection and/or processing code
├── .env                <- Optional environment variables file (NOTE: excluded from Git; create by hand)
├── main.py             <- Entry point for project code
├── README.md           <- Top-level project documentation
├── requirements.txt    <- Python requirements file
└── settings.py         <- Project settings; will load environment variables from `.env`
```

### Collaboration

Questions and suggestions from the broader team are encouraged! Just create an issue.

