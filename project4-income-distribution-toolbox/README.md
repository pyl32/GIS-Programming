# 💰 California Family Income Distribution — Custom ArcGIS Python Toolbox

![Python](https://img.shields.io/badge/Python-ArcPy%20Toolbox-blue?logo=python)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-Python%20Toolbox%20(.pyt)-blue?logo=esri)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Classification-yellow?logo=pandas)
![Course](https://img.shields.io/badge/Course-SSCI%20586%20GIS%20Programming-green)

## Overview

This project builds a **reusable custom Python Toolbox for ArcGIS Pro** that classifies numerical socioeconomic data using quantile statistics, joins it to a spatial geodatabase, and produces a choropleth map — all through a single parameterized tool.

Applied to **median family income by county across California**, the toolbox visualizes wealth distribution and inequality at the county level using an IQR-based classification scheme.

---

## 🎯 Objectives

- Create a custom `.pyt` Python Toolbox in ArcGIS Pro with configurable input parameters
- Apply quantile-based statistical classification (Q1, Q2, Q3, IQR, outlier detection) to tabular data
- Perform a table join between an Excel income dataset and a California County boundary geodatabase
- Export a new feature class and visualize income distribution as a choropleth map

---

## 🗺️ Study Area

**California, USA** — a state of dramatic economic diversity, from Silicon Valley tech wealth to rural agricultural counties. This project maps median family income across all 58 California counties.

---

## 📂 Repository Structure

```
project4-income-distribution-toolbox/
├── Project4_Report.pdf                  # Full write-up and methodology
├── scripts/
│   └── income_quantile_toolbox.pyt      # ArcGIS Pro Python Toolbox
├── data/
│   ├── incomebycounty_CA.xlsx           # Per capita and median income data
│   ├── familyincomebycounty_CA.xlsx     # Median family income by county
│   └── educational attainment2021.xlsx  # Supplementary education data
└── README.md
```

---

## 🗃️ Data Sources

| File | Type | Description |
|------|------|-------------|
| `familyincomebycounty_CA.xlsx` | Excel | Median family income per CA county |
| `CaliforniaCounty.shp` (in GDB) | Shapefile/GDB | CA county boundaries (NAD 1983, 1:24,000) |

**Input Excel columns used:** `County`, `Median family income`
**Join field:** `COUNTY_NAM`

---

## ⚙️ Toolbox Architecture

The toolbox (`income_quantile_toolbox.pyt`) exposes **4 parameters** in the ArcGIS Pro UI:

| Parameter | Type | Description |
|-----------|------|-------------|
| Input Feature | GPFeatureLayer | California County geodatabase layer |
| Input Table | Table | Excel file with income data |
| Input Field | Field | Column name for the numeric values to classify |
| Output Feature | GPFeatureLayer | Output choropleth feature class |

### Classification Logic (IQR Method)

```python
import pandas as pd

Q1 = df[field].quantile(0.25)
Q2 = df[field].quantile(0.50)   # Median
Q3 = df[field].quantile(0.75)
IQR = Q3 - Q1

# Six classification categories:
# "OutliersOverQ3"  → value ≥ Q3 + 1.5×IQR
# "> 75%"           → Q3 ≤ value < Q3 + 1.5×IQR
# "50%-75%"         → Q2 ≤ value < Q3
# "25%-50%"         → Q1 < value < Q2
# "< 25%"           → Q1 - 1.5×IQR < value ≤ Q1
# "OutliersBelowQ1" → value ≤ Q1 - 1.5×IQR
```

### Geoprocessing Pipeline

```python
import arcpy

# Step 1: Write classified data to new Excel
df['classify'] = classify_column
df.to_excel("output.xlsx")

# Step 2: Join Excel to geodatabase feature class
joined = arcpy.AddJoin_management(
    inFeatures, "COUNTY_NAM",
    joinTable,  "COUNTY_NAM"
)

# Step 3: Export joined result as permanent feature class
arcpy.CopyFeatures_management(joined, outputfc)
```

See full toolbox: [`scripts/income_quantile_toolbox.pyt`](scripts/income_quantile_toolbox.pyt)

---

## 📊 Results

The output choropleth map classifies all 58 California counties into 6 income brackets:

| Class | Description |
|-------|-------------|
| 🔴 Outliers Over Q3 | Exceptionally high-income counties (Silicon Valley, Marin) |
| 🟠 > 75% | High-income counties |
| 🟡 50%–75% | Upper-middle income counties |
| 🟢 25%–50% | Lower-middle income counties |
| 🔵 < 25% | Low-income counties |
| ⚫ Outliers Below Q1 | Exceptionally low-income counties |

---

## 💡 Key Findings & Reuse Potential

- **Quantile classification** is robust against extreme values, making it well-suited for skewed income data
- The outlier categories (above/below 1.5×IQR) explicitly flag counties with exceptional income levels
- This toolbox is **directly reusable** for any numeric attribute joined to a polygon layer:
  - Population density by county or census tract
  - Retail gasoline prices by state *(see Project 5)*
  - Educational attainment rates (supplementary data included)
  - Any other socioeconomic indicator in Excel format

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **ArcGIS Pro** | Toolbox hosting, map visualization |
| **Python 3 (.pyt)** | Toolbox scripting |
| **arcpy** | `AddJoin_management`, `CopyFeatures_management` |
| **Pandas** | `DataFrame.quantile()`, `DataFrame.to_excel()` |
| **ESRI File Geodatabase** | California County boundary storage |

---

## 📎 Report

See [`Project4_Report.pdf`](Project4_Report.pdf) for full methodology, map outputs, and discussion.
