# Project 2: Interventional Diabetes Clinical Trials RBM Analysis

## Overview
This project analyzes interventional diabetes clinical trials using data from ClinicalTrials.gov, with a focus on constructing and evaluating a heuristic Risk-Based Monitoring (RBM) framework. The analysis demonstrates how trial characteristics such as enrollment size, intervention type, and study phase influence operational risk.

## Dataset
- Source: ClinicalTrials.gov API  
- Number of trials retrieved: ~5,000 (random sample from ~34,000 diabetes trials)  
- Key filters applied: interventional diabetes studies across multiple phases and geographies  
- Columns analyzed: enrollment size, number of locations, study duration, phase, intervention type, and data completeness indicators

## Data Structure
The project follows a structured data workflow separating raw and processed data:

- `data/raw/`  
  - Contains the original dataset retrieved from the ClinicalTrials.gov API  
  - Preserved in its initial format for reproducibility and traceability  

- `data/processed/`  
  - Contains cleaned and transformed datasets used for analysis  
  - Includes standardized variables (e.g., phase, intervention type) and engineered features (e.g., RBM risk components)  

- `results/figures/`  
  - Final visualization outputs used in the main analysis  

- `results/exploratory/`  
  - Supplementary figures used for supporting and exploratory analysis  

This structure supports reproducibility and mirrors standard clinical research data workflows, where raw data is preserved and all transformations are performed on derived datasets.

## Data Processing
- Cleaned and standardized trial phase values from mixed formats (strings and list representations)  
- Removed or handled missing and inconsistent entries across key variables  
- Engineered RBM-related features using percentile-based thresholds

### RBM Feature Engineering - Risk Scoring Heuristic
The `total_risk_score` was constructed as a composite heuristic to approximate operational risk in a Risk-Based Monitoring (RBM) context. The score integrates multiple trial-level features:

- Binary risk flags (1 point each):
  - High enrollment (top 25%)
  - Multi-site trials (top 25% by number of locations)
  - Long study duration (top 25%)

- Mapped categorical risk components:
  - Phase risk:
    - Early Phase 1 / Phase 1 → 4  
    - Phase 2 / Phase 3 → 3  
    - Phase 4 → 1  
    - Missing/Unknown → 2  
  - Intervention risk:
    - Drug / Biological → 3  
    - Device / Procedure → 2  
    - Behavioral / Diagnostic / Other → 1  

- Data quality signal:
  - Missing location data contributes additional risk via `(1 - has_location_data)`

The final `total_risk_score` is the sum of these components, producing observed scores ranging from 2 to 10 within the dataset. This approach reflects a simplified RBM framework where operational complexity, scale, and data completeness contribute to monitoring burden.

## Visualizations

### Fig 1: Distribution of RBM Risk Scores
- RBM scores are concentrated between 3 and 6, with a peak at 4  
- A smaller right tail extends toward higher risk scores (8–10), representing more complex trials  

### Fig 2: RBM Risk Score Distribution by Intervention Type
- Biological and Drug interventions show the highest median risk and widest upper ranges  
- Procedure and Device interventions occupy a mid-risk range with moderate variability  
- Behavioral, Diagnostic Test, and Other interventions consistently show lower RBM risk  
- Higher-complexity interventions demonstrate both elevated risk and increased variability  

### Fig 3: RBM Risk Score Distribution by Clinical Trial Phase
- Early Phase 1 trials exhibit consistently high RBM risk with tight distributions  
- Phase 1 trials show concentrated risk profiles with limited variability  
- Phase 2 and Phase 3 trials display broader distributions, with Phase 3 showing elevated risk and variability  
- Phase 4 trials have the lowest RBM risk, reflecting reduced operational complexity  
- Trials with unknown phase show heterogeneous distributions, likely reflecting incomplete data  

### Fig 4: RBM Risk Score by Trial Enrollment Size
- Trials in Very Low to Medium enrollment categories show nearly identical risk distributions  
- A noticeable increase in risk emerges in the High enrollment group  
- Very High enrollment trials demonstrate both higher median risk and significantly greater variability  
- Results suggest a threshold effect where large-scale trials introduce disproportionate monitoring burden  

## Exploratory Analysis

### Exploratory Figure A: RBM Risk Composition by Enrollment Size
- Lower enrollment categories are dominated by Low and Medium risk trials  
- The proportion of High risk trials increases substantially in the Very High enrollment group  
- Low risk trials decrease as enrollment size increases  
- This supports the observation that trial scale shifts not only overall risk, but the composition of risk categories  

## Technical Stack
- Python 3.9  
- pandas  
- numpy  
- matplotlib  
- seaborn  

## Key Insights
- RBM risk is concentrated in the mid-range, with a smaller subset of high-risk trials  
- Intervention complexity is a strong driver of operational risk, with Drug and Biological trials consistently highest  
- Trial phase shows a non-linear relationship with risk, with elevated burden in early-stage and Phase 3 studies  
- Enrollment size acts as a threshold driver, where larger trials introduce disproportionately higher and more variable risk  
- Risk composition shifts with scale, with high-risk trials becoming more prevalent in large enrollment studies  

## Notes
- RBM risk scores are heuristic and derived from engineered features rather than validated clinical models  
- All figures are saved in the `results/figures` folder, with exploratory outputs stored separately in the `results/exploratory` folder 
- The notebook is fully reproducible and can be run top-to-bottom to regenerate all results  