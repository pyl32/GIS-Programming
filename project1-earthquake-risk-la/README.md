# 🏫 Earthquake Risk Analysis for Schools in Los Angeles County

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-ModelBuilder-blue?logo=esri)
![USGS Data](https://img.shields.io/badge/Data-USGS%20Earthquake%20Faults-orange)
![Course](https://img.shields.io/badge/Course-SSCI%20586%20GIS%20Programming-green)

## Overview

Los Angeles County sits atop one of the most seismically active regions in the United States. This project identifies and prioritizes K–12 schools most at risk from earthquake faults — providing actionable data for seismic retrofit planning and emergency preparedness.

Schools within **1 mile of active fault lines** are identified and ranked by fault slip rate, giving planners a clear, data-driven prioritization framework.

---

## 🎯 Objectives

- Identify all public and private schools within 1 mile of earthquake faults in LA County
- Classify schools by fault slip-rate risk level (highest → lowest priority)
- Visualize spatial distribution of at-risk schools using a color-coded risk map
- Provide a reproducible ModelBuilder workflow for future re-analysis

---

## 🗺️ Study Area

**Los Angeles County, California** — home to millions of residents and thousands of schools, bisected by the San Andreas Fault system and numerous secondary fault lines mapped by the USGS.

---

## 📂 Repository Structure

```
project1-earthquake-risk-la/
├── Project1_Report.pdf         # Full project write-up and methodology
├── Project1_workflow.png       # ModelBuilder workflow diagram
├── data/                       # Source data (shapefiles, fault lines), using open source data from https://geohub.lacity.org/
└── README.md
```

---

## 🗃️ Data Sources

| Layer | Source | Description |
|-------|--------|-------------|
| Earthquake Faults | USGS | Active fault lines with slip rate codes |
| Public Schools | CA Dept. of Education | Point locations of public schools in LA County |
| Private Schools | CA Dept. of Education | Point locations of private schools in LA County |
| LA County Boundary | Census / ESRI | County boundary for clipping |

**Coordinate System:** WGS 1984 Web Mercator (Mercator Auxiliary Sphere)

---

## ⚙️ Methodology

The entire workflow was built in **ArcGIS Pro ModelBuilder**:

1. **Merge** public and private school layers into a single schools dataset
2. **Clip** schools and fault layers to Los Angeles County boundary
3. **Buffer** fault lines by 1 mile to define the earthquake risk zone
4. **Clip** merged school layer to the 1-mile buffer polygon
5. **Intersect** clipped schools with the fault buffer to assign slip-rate codes
6. **Symbolize** schools by slip rate code (1 = highest risk, 4 = lowest risk, 0 = unknown)

> **Slip Rate Codes (USGS):** Code 1 = highest activity → highest retrofit priority. Code 4 = lowest activity. Code 0 = unknown slip rate.

---

## 📊 Results

| Risk Level | Slip Code | Color | Description |
|------------|-----------|-------|-------------|
| Highest Priority | 1 | 🔴 Red | Adjacent to most active faults |
| High Priority | 2 | 🟠 Orange | Near moderately active faults |
| Medium Priority | 3 | 🟡 Yellow | Near low-activity faults |
| Lower Priority | 4 | 🟢 Green | Near least active faults |
| Unknown | 0 | ⚪ Gray | Fault slip rate not characterized |

Schools colored red should be the **first priority** for seismic inspections and retrofit funding.

---

## 💡 Key Findings & Limitations

- A significant number of LA County schools fall within the 1-mile earthquake risk buffer
- Merging public and private schools means the output cannot distinguish school type — a limitation for targeted policy
- An alternative approach using **Select by Location** (rather than Intersect) could produce comparable results with fewer geoprocessing steps
- Future iterations could incorporate building age, construction type, and population density for a composite risk score

---

## 🛠️ Tools & Technologies

- **ArcGIS Pro** — ModelBuilder, geoprocessing tools
- **USGS Fault Data** — Quaternary Fault and Fold Database
- **Geoprocessing Tools Used:** Merge, Clip, Buffer, Intersect, Change Symbology

---

## 📎 Report

See [`Project1_Report.pdf`](Project1_Report.pdf) for the full methodology, maps, and discussion.
