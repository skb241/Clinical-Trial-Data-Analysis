# Project 1: Oncology Clinical Trial Analysis

## Overview
This project analyzes the global landscape of oncology clinical trials using publicly available data from the ClinicalTrials.gov API. It demonstrates an end-to-end workflow including data extraction, cleaning, transformation, and visualization of trial characteristics.

## Dataset
- Source: ClinicalTrials.gov API  
- Number of trials: ~5,000 oncology-related studies  
- Query terms: "cancer", "oncology", "tumor/tumour"  
- Scope: Trials across multiple phases, statuses, and countries  

### Key Variables
- Trial phase  
- Recruitment status  
- Enrollment size  
- Study start date  
- Country  
- Lead sponsor  

---

## Data Processing
- Flattened nested JSON structures returned by the API into tabular format  
- Extracted country information from location fields  
- Converted enrollment values to numeric format for analysis  
- Derived study start year from date fields  
- Calculated study duration where applicable  
- Standardized categorical variables (phase, status)  
- Applied log10 transformation to enrollment for visualization  

---

## Visualizations

**Fig 1: Distribution of Trial Status**  
- Completed trials dominate (~1800)  
- Recruiting (~600) and Unknown (~600) follow  
- Terminated trials (~400) form a notable subset  
- Smaller categories include Active (not recruiting) (~200), Not yet recruiting (~200), Withdrawn (~100), and Enrolling by invitation  
- Indicates a dataset largely composed of completed and actively managed trials  

**Fig 2: Distribution of Trial Phases**  
- Phase 2 trials are most common (~1200+)  
- Unknown phase category is also substantial (~1100+)  
- Phase 1 trials follow (~900+)  
- Phase 3 (~400) and Phase 4 (~100+) are less frequent  
- Early Phase 1 represents a small subset (~100)  
- Reflects real-world variability and incomplete phase reporting  

**Fig 3: Top 10 Countries by Oncology Trial Activity**  
- United States leads (~1800 trials)  
- China follows (~600 trials)  
- France (~200) and Canada (~100) contribute moderate volumes  
- South Korea, Germany, and the United Kingdom fall below 100  
- Italy (~60), Denmark (~50), and Spain (~50) round out the top 10  
- Demonstrates strong geographic concentration in a few leading countries  

**Fig 4: Distribution of Trial Enrollment Sizes (Log Scale)**  
- Peak concentration occurs between log10 values of 1–2 (~10–100 participants), with ~500+ trials in this range  
- Trial counts decline steadily as enrollment size increases  
- Moderate-sized trials (100–1000 participants) are less frequent  
- Large-scale trials (>1000 participants) are relatively rare  
- The distribution reflects a typical clinical trial landscape, where early-phase and smaller cohort studies are more common than large, late-phase trials   

**Fig 5: Number of Oncology Trials Initiated Per Year**  
- Minimal activity prior to 2000  
- Gradual increase from early 2000s to ~2012  
- Accelerated growth from ~2012 to ~2015 (~145 trials)  
- Continued steady increase to ~2022 (~230 trials)  
- Recent plateau likely reflects ongoing or incomplete reporting  
- Overall trend shows sustained expansion in oncology research activity  

**Fig 6: Top 10 Trial Sponsors**  
- National Cancer Institute leads (~90 trials)  
- MD Anderson Cancer Center (~86) follows closely  
- Memorial Sloan Kettering (~50) ranks third  
- Academic institutions (Fudan University, Sun Yat-sen University) and industry sponsors (Pfizer, Roche, Novartis) are well represented  
- Sponsor counts range from ~30–90 trials  
- Indicates concentration among major research institutions and pharmaceutical companies  

---

## Key Insights
- Oncology trials are concentrated in **Phase 2 and Phase 1**, with a large proportion of unknown phase classifications  
- The **United States and China dominate global trial activity**  
- Most trials involve **small to moderate enrollment sizes (10–100 participants)**  
- Oncology research activity has grown steadily, particularly after 2010  
- Sponsorship is concentrated among a relatively small group of major institutions and companies  

---

## Tools Used
- Python (pandas, numpy, matplotlib)  
- requests (API data extraction)  

---

## Project Structure
data/
├── raw/ # Raw API JSON responses
├── processed/ # Cleaned and structured datasets

results/
├── figures/ # Final visualizations

analysis/
├── 01_oncology_trial_analysis.ipynb

---

## How to Run
1. Open the notebook in Jupyter or VSCode  
2. Run all cells sequentially  
3. Figures will be saved in `results/figures/` 
