# Healthcare Analytics for Doctor Visit – TIRTC

**Student:** Arnaov Garg  
**AICTE ID:** STU66fc1fdc7fe6b1727799260  
**Project:** Healthcare Analytics for Doctor Visit TIRTC

## Project objective
This project analyzes the supplied doctor-visit dataset and presents an interactive dashboard for exploring visit patterns by gender, age group, illness count, health score, and coverage category.

## Dataset
- Records: **5,190**
- Variables: **13 original columns** (after removing the CSV index column, 12 analytical fields are used)
- Total recorded visits: **1,566**
- Mean visits per record: **0.30**

## Main analysis
1. Gender-wise doctor visits
2. Age-group visit patterns
3. Average visits by illness count
4. Average visits by health score
5. Coverage/insurance distribution
6. Interactive filtering and data table

## Key observations from the supplied dataset
- Female records have an average of **0.36** visits, compared with **0.24** for male records.
- The **61–80** age group has the largest total recorded visits among the derived age groups in this dataset.
- Average visits generally rise across higher illness-count categories, with the highest mean in illness category **5**.
- Higher health-score categories in this dataset often show higher average visit counts, although this is an observational pattern and not a causal medical conclusion.

## Technology
Python, Pandas, NumPy, Streamlit, Plotly, Matplotlib.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard will open in your browser.

## Project structure
```text
Healthcare_Analytics_Doctor_Visit_TIRTC/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── doctor_visits.csv
├── assets/
│   ├── gender_visits.png
│   ├── age_visits.png
│   ├── illness_avg.png
│   ├── health_avg.png
│   └── insurance.png
├── docs/
│   └── project_summary.txt
└── Healthcare_Analytics_Doctor_Visit_TIRTC.pptx
```

## Important note
This is an educational analytics project. The dashboard should not be used for diagnosis, treatment, or clinical decision-making.
