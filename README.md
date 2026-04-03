# CI/CD Pipeline Analytics Dashboard 2025

**Tools:** Python • Jenkins API • Power BI • GitHub Actions

## Project Overview
Fetched CI/CD pipeline data from Jenkins APIs using Python 
and Pandas, stored in CSV format for analysis.

## What This Project Does
- Fetches build data from Jenkins REST API using Python
- Cleans and processes pipeline logs with Pandas
- Tracks key metrics: success rate, failure rate, build duration
- Visualizes data in a Power BI dashboard
- Automates daily data refresh using GitHub Actions

## Key Metrics Tracked
- Build success rate per job
- Build failure rate per job
- Average build duration
- Deployment frequency

## Project Files
- `fetch_data.py` — fetches build data from Jenkins API
- `clean_data.py` — cleans data and computes metrics
- `pipeline_data_clean.csv` — cleaned build records
- `pipeline_summary.csv` — summary metrics per job
- `requirements.txt` — Python dependencies

## Dashboard Preview

<img width="1279" height="724" alt="screenshot" src="https://github.com/user-attachments/assets/b5e4b6af-06a5-4db5-9a12-694338cab209" />

## How to Run
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with Jenkins credentials
4. Run `python fetch_data.py`
5. Run `python clean_data.py`
6. Open Power BI and refresh data source
