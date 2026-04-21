# Clinical Trial Data Analytics Portfolio

## Overview
This repository showcases a series of projects focused on analyzing real-world clinical trial data, progressing from exploratory analysis to applied risk-based monitoring (RBM) concepts.

The objective is to demonstrate practical, job-relevant skills in:
- Clinical trial data interpretation  
- Data cleaning and transformation  
- Visualization and insight generation  
- Risk-based analytical thinking aligned with clinical operations  

These projects use publicly available data from ClinicalTrials.gov and are designed to reflect real-world analytical workflows in clinical research, data management, and monitoring.

---

## Projects

### 01 — Oncology Clinical Trial Analysis
Exploratory analysis of ~5,000 oncology trials from ClinicalTrials.gov to understand global trial characteristics.

Key focus:
- Trial distributions (status, phase, geography)
- Enrollment patterns and scale variability
- Temporal trends in trial activity
- Sponsor landscape and activity

Skills demonstrated:
- API data extraction  
- Data cleaning and structuring of nested datasets  
- Exploratory data analysis (EDA)  
- Data visualization and reporting  

---

### 02 — Clinical Trial RBM Analysis (Diabetes)
Application of a simplified Risk-Based Monitoring (RBM) framework to interventional diabetes trials.

Key focus:
- Development of a composite risk score using operational and clinical features  
- Identification of high-risk trial characteristics based on:
  - Enrollment size  
  - Trial duration  
  - Phase  
  - Intervention type  
  - Data completeness signals  
- Stratification of trials to simulate monitoring prioritization  

Skills demonstrated:
- Feature engineering  
- Risk modeling logic aligned with RBM principles  
- Comparative and distribution-based analysis  
- Clinical interpretation of trial-level risk  

---

## Tech Stack
- Python (pandas, numpy, matplotlib, seaborn)
- Jupyter Notebook / VSCode
- ClinicalTrials.gov API

---

## Repository Structure
projects/
├── 01_oncology_trial_analysis/
├── 02_clinical_trial_rbm_analysis/

data/
results/

---

## Author

**Suhail Barakzai**  
BSc Biology – University of Waterloo  

---

## Notes

- All analyses are reproducible and based on publicly available data  
- Data is sourced from ClinicalTrials.gov and processed for analytical use  
- Figures are generated programmatically  
- Projects are structured to reflect real-world clinical data workflows and RBM-style thinking  