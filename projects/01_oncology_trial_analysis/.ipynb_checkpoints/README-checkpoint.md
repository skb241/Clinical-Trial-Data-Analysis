# Project 1: Oncology Trials Analysis

## Overview
This project explores the landscape of oncology clinical trials using publicly available data from ClinicalTrials.gov. The analysis demonstrates end-to-end clinical research data workflows, from pulling trial data via the API to visualizing trial characteristics.

## Dataset
- Source: [ClinicalTrials.gov API](https://clinicaltrials.gov/api/)
- Number of trials retrieved: 5,000 oncology trials
- Key filters applied: trials with relevant oncology conditions, completed or active status, across multiple countries.
- Columns analyzed: trial phase, status, enrollment size, country, start year, lead sponsor.

## Data Processing
- Removed invalid or missing entries where necessary.
- Standardized trial phases and trial statuses (e.g., unknown phases labeled as "UNKNOWN").
- Handled enrollment sizes for log-scaled visualization.

## Visualizations
**Fig 1: Distribution of Trial Status**
- Majority of trials are "Completed", followed by "Recruiting", "Terminated", and "Unknown".

**Fig 2: Distribution of Trial Phases**
- Ordered from "EARLY PHASE 1" to "PHASE 4", including unknown phases.  
- Most trials are Phase 2, followed by Phase 1.

**Fig 3: Top 10 Countries by Oncology Trial Activity**
- The United States leads with ~1750 trials, followed by China and other countries.

**Fig 4: Distribution of Trial Enrollment Sizes (Log Scale)**
- Log10 scale applied to x-axis for easier visualization of wide enrollment ranges (e.g., 2 = 100 participants).
- The log scale was translated into participant number sizes.  
- Bell-shaped distribution indicates most trials have moderate enrollment sizes.

**Fig 5: Number of Oncology Trials Started Per Year**
- Shows exponential increase in trials after 1990.  
- Recent years are truncated to reflect ongoing data collection.

**Fig 6: Top 10 Sponsors in Oncology Trials**
- Lead sponsors are primarily large pharmaceutical and research organizations.  
- Names wrapped for readability, x-axis scaled for consistent increments.

## Technical Stack
- Python 3.9
- pandas, numpy, matplotlib
- requests (for API calls)

## Key Insights
- Majority of oncology trials are Phase 2 and completed in the US.
- Enrollment sizes follow a log-normal distribution.
- Lead sponsors are concentrated among a few major organizations.
- Trends indicate a rapid increase in oncology trials since the 1990s.

## Notes
- All figures saved in the `results/` folder.  
- Notebook fully reproducible; run top-to-bottom to generate all figures.