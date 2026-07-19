# Mutual Fund Analytics Capstone Project

## Overview

The Mutual Fund Analytics Capstone Project is an end-to-end data analytics project that demonstrates the complete data pipeline, from data collection and cleaning to advanced financial analysis and interactive dashboard development.

The project analyzes multiple mutual fund datasets to provide insights into fund performance, investor behavior, portfolio risk, and investment recommendations using Python, SQL, SQLite, and Power BI.

---

## Project Objectives

* Collect and clean mutual fund datasets
* Build a centralized SQLite database
* Perform exploratory data analysis (EDA)
* Calculate financial performance metrics
* Develop advanced risk analytics
* Build a mutual fund recommendation system
* Create an interactive Power BI dashboard

---

## Technology Stack

* Python 3.11
* Pandas
* NumPy
* Matplotlib
* SQLAlchemy
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
Mutual_Fund_Capstone_Project/
│
├── dashboard/
│   └── bluestock_mf.pbix
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Advanced_Analytics.ipynb
│   └── 03_Performance_Analytics.ipynb
│
├── reports/
│   ├── alpha_beta.csv
│   ├── benchmark_comparison.png
│   ├── fund_scorecard.csv
│   ├── rolling_sharpe_chart.png
│   ├── top5_funds.png
│   └── var_cvar_report.csv
│
├── scripts/
│   ├── data_ingestion.py
│   ├── load_to_sqlite.py
│   ├── verify_database.py
│   ├── recommender.py
│   └── live_nav_fetch.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── requirements.txt
└── README.md
```

---

## Features

### Data Processing

* Data ingestion
* Data cleaning
* Missing value handling
* Data validation
* SQLite database creation

### Exploratory Data Analysis

* NAV trends
* Category analysis
* Fund house comparison
* SIP analysis
* Portfolio analysis

### Performance Analytics

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard

### Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector Concentration (HHI)
* Mutual Fund Recommendation System

### Interactive Dashboard

* Executive Overview
* Performance Analytics
* Investor Analytics
* Portfolio & Risk Analytics

---

## Key Deliverables

* Cleaned datasets
* SQLite database
* Performance analytics notebook
* Advanced analytics notebook
* Power BI dashboard
* Financial reports
* GitHub repository

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Akshay736252/mutual-fund-capstone-project.git
```

Navigate to the project directory:

```bash
cd mutual-fund-capstone-project
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the scripts in the following order:

1. data_ingestion.py
2. clean_*.py scripts
3. load_to_sqlite.py
4. verify_database.py
5. Jupyter notebooks
6. Open the Power BI dashboard

---

## Dashboard Pages

* Executive Overview
* Performance Analytics
* Investor Analytics
* Portfolio & Risk Analytics

---

## Future Improvements

* Live NAV updates using APIs
* Portfolio optimization
* Monte Carlo simulation
* Streamlit web application
* Automated reporting

---

## Author

**Akshay Kanojia**

GitHub:
https://github.com/Akshay736252

---

## License

This project is created for educational and portfolio purposes.
