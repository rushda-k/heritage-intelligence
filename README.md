# 🏛️ Heritage Intelligence

### Comparative Data Intelligence for Cultural Heritage Collections

**Heritage Intelligence** is an interactive data analytics project comparing cultural heritage collection data from the **Smithsonian National Museum of American History (NMAH)** and **The Metropolitan Museum of Art (The Met)**.

The project evaluates collection scale, metadata quality, digital accessibility, cultural metadata, geographic representation, and geographic concentration through a comparative analytical framework.

## 🚀 Live Demo

### [Open the Interactive Heritage Intelligence Dashboard](https://heritage-intelligence-7lcoy4vuqn2dqc5yceszte.streamlit.app/)

Explore the analysis through an interactive Streamlit dashboard with museum selection, comparative tables, visualizations, geographic analysis, key findings, and the Heritage Intelligence Score.

---

## 📊 Project Overview

The project investigates how two major cultural heritage collections differ in their:

* Collection scale
* Metadata completeness
* Artist metadata coverage
* Culture metadata coverage
* Country metadata coverage
* Digital accessibility
* Geographic representation
* Geographic concentration

The objective is to demonstrate how **data analytics can be applied to cultural heritage collections to identify patterns in metadata quality, accessibility, and representation.**

---

## 🏆 Key Results

| Metric                         | Smithsonian NMAH |         The Met |
| ------------------------------ | ---------------: | --------------: |
| Collection Size                |           15,000 |             584 |
| Metadata Quality               |           47.85% |          68.49% |
| Digital Accessibility          |           53.31% |          61.30% |
| Artist Metadata                |           51.77% |          85.45% |
| Culture Metadata               |            0.64% |          27.40% |
| Country Metadata               |           34.71% |          16.95% |
| Unique Geographies             |              175 |              18 |
| Top 5 Geographic Concentration |           81.19% |          76.77% |
| Heritage Intelligence Score    |  **53.16 / 100** | **40.13 / 100** |

### Key Insights

**Collection Scale**
The analyzed Smithsonian sample contains 15,000 objects compared with 584 objects in the analyzed Met sample.

**Metadata Quality**
The Met demonstrates stronger overall metadata completeness in the analyzed data.

**Digital Accessibility**
Digital accessibility is higher in the analyzed Met records.

**Artist Metadata**
Artist metadata coverage is substantially stronger for The Met.

**Culture Metadata**
Culture metadata coverage is substantially stronger for The Met.

**Country Metadata**
Country metadata coverage is higher in the Smithsonian sample.

**Geographic Representation**
The Smithsonian sample contains more standardized geographic categories in the current analysis.

**Geographic Concentration**
The five most frequent geographic categories account for 81.19% of Smithsonian records with geographic data and 76.77% of corresponding Met records.

---

## 📐 Analytical Framework

The Heritage Intelligence framework combines multiple collection-level indicators rather than relying on a single metric.

### Core Dimensions

| Dimension                | Purpose                                                                   |
| ------------------------ | ------------------------------------------------------------------------- |
| Collection Scale         | Measures the size of the analyzed collection sample                       |
| Metadata Quality         | Evaluates completeness of selected metadata fields                        |
| Artist Metadata          | Measures availability of artist-related information                       |
| Culture Metadata         | Measures availability of cultural classification information              |
| Country Metadata         | Measures geographic/country metadata availability                         |
| Digital Accessibility    | Measures availability of digital collection access/images                 |
| Geographic Diversity     | Examines the number of standardized geographic categories                 |
| Geographic Concentration | Examines the share represented by the most frequent geographic categories |

The resulting **Heritage Intelligence Score** is a project-specific comparative framework. It should not be interpreted as an official ranking of museum quality.

---

## 🗂️ Data Sources

The analysis uses collection data associated with:

* **Smithsonian Open Access / National Museum of American History**
* **The Metropolitan Museum of Art Collection API**

The project processes and standardizes collection metadata before performing cross-museum comparisons.

---

## 🛠️ Technology Stack

### Data Analysis

* Python
* Pandas
* NumPy
* Jupyter Notebook

### Visualization & Dashboard

* Streamlit
* Interactive data tables
* Comparative charts

### Development & Version Control

* Git
* GitHub

---

## 📁 Repository Structure

```text
HERITAGE-INTELLIGENCE/
│
├── app.py
├── dashboard.html
├── README.md
│
├── notebooks/
│   ├── 01_collection_exploration.ipynb
│   ├── 02_cross_museum_analysis.ipynb
│   ├── 03_heritage_dashboard.ipynb
│   └── README.md
│
└── data/
    └── processed/
        ├── final_scorecard.csv
        ├── geographic_concentration.csv
        └── top_country_comparison.csv
```

Large/raw datasets are intentionally excluded from the public repository.

---

## 🔬 Analysis Workflow

```text
Collection Data
       ↓
Data Cleaning & Standardization
       ↓
Collection Exploration
       ↓
Metadata Quality Analysis
       ↓
Cross-Museum Comparison
       ↓
Geographic Analysis
       ↓
Heritage Intelligence Scoring
       ↓
Interactive Streamlit Dashboard
```

---

## 📓 Notebooks

### `01_collection_exploration.ipynb`

Explores the underlying collection data and examines collection structure, metadata fields, and initial data quality.

### `02_cross_museum_analysis.ipynb`

Performs the comparative analysis between Smithsonian NMAH and The Met across metadata, digital, cultural, and geographic dimensions.

### `03_heritage_dashboard.ipynb`

Supports the final dashboard-oriented analysis and preparation of comparative outputs.

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/rushda-k/heritage-intelligence.git
cd heritage-intelligence
```

Install the required packages:

```bash
pip install streamlit pandas numpy
```

Run the dashboard:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 🌐 Interactive Dashboard

The deployed dashboard provides:

* Museum selection
* Executive overview
* Collection-scale comparison
* Metadata quality comparison
* Digital accessibility comparison
* Geographic diversity analysis
* Geographic-origin tables
* Heritage Intelligence Score
* Key analytical findings
* Methodology documentation

### Live Application

**[🚀 Launch Heritage Intelligence](https://heritage-intelligence-7lcoy4vuqn2dqc5yceszte.streamlit.app/)**

---

## ⚠️ Interpretation Note

This project is designed as a **data analytics and comparative intelligence exercise**.

The Heritage Intelligence Score reflects the project's selected indicators and weighting framework. It does **not** represent an official assessment, endorsement, or quality ranking issued by either museum.

Results should therefore be interpreted within the scope of the analyzed datasets and methodology.

---

## 👩‍💻 Project

**Heritage Intelligence — Cultural Heritage Data Analytics**

Built using Python, Pandas, NumPy, Jupyter, Streamlit, and GitHub.

