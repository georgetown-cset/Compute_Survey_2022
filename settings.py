from pathlib import Path

from dotenv import load_dotenv

# The project root is the parent of this file
PROJECT_ROOT = Path(__file__).absolute().parent

# Top-level directories
ANALYSIS_DIR = PROJECT_ROOT / 'analysis'
DATA_DIR = PROJECT_ROOT / 'data'

# Data directories
FINAL_DATA_DIR = DATA_DIR / 'final'
INTERIM_DATA_DIR = DATA_DIR / 'interim'
REFERENCE_DATA_DIR = DATA_DIR / 'reference'
SOURCE_DATA_DIR = DATA_DIR / 'source'

# Analysis directories
FIGURES_DIR = ANALYSIS_DIR / 'figures'
TABLES_DIR = ANALYSIS_DIR / 'tables'

# Load environment variables from any .env file in the project root
load_dotenv(dotenv_path=PROJECT_ROOT, override=True)
