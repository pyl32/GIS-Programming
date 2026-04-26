# ⛽ U.S. Retail Gasoline Price Distribution — Extended ArcGIS Python Toolbox

![Python](https://img.shields.io/badge/Python-ArcPy%20Toolbox-blue?logo=python)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-Python%20Toolbox%20(.pyt)-blue?logo=esri)
![Scale](https://img.shields.io/badge/Scale-National%20(USA)-red)
![Course](https://img.shields.io/badge/Course-SSCI%20586%20GIS%20Programming-green)

## Overview

This project **extends the Python Toolbox built in Project 4** to a national scale — applying the same quantile-based spatial classification system to **retail gasoline prices across all U.S. states**.

It demonstrates how a well-designed geospatial tool can be adapted and reused across different datasets, geographies, and thematic questions with minimal code changes.

---

## 🎯 Objectives

- Adapt the Project 4 income toolbox to map a new variable: retail fuel gasoline prices by state
- Apply data cleaning to exclude non-contiguous or missing territories (Puerto Rico, DC, American Samoa, Guam)
- Generate a national choropleth map of gasoline price distribution using IQR-based quantile classification
- Demonstrate toolbox reusability across different scales (county → state) and domains (income → energy prices)

---

## 🗺️ Study Area

**United States of America** — all 50 states, visualized at the state polygon level. Data covers retail gasoline prices with state-level aggregation, enabling regional price pattern analysis across the contiguous U.S.

---

## 📂 Repository Structure

```
project5-gasoline-price-toolbox/
├── Project5_Report.pdf                        # Full write-up and methodology
├── notebooks/
│   └── Zandebergen_2020b_Ch9_Text_samples_v1.ipynb  # Reference Python for GIS notebook
├── data/                                            # Gasoline price Excel + state geodatabase
└── README.md
```

---

## 🗃️ Data Sources

| File | Type | Description |
|------|------|-------------|
| Retail Gasoline Price Table | Excel | State-level average retail fuel prices (Statista, 2022) |
| State Boundaries | ESRI GDB | U.S. state polygon boundaries (NAD 1983, Census) |

**Join field:** `NAME` (state name)
**Input columns:** `County` (state name), `Price` (retail price per unit)

---

## ⚙️ Methodology

### Data Cleaning

Before classification, non-state territories were excluded:

```python
exclude = ["Puerto Rico", "District of Columbia", "American Samoa", "Guam"]
df = df[~df["County"].isin(exclude)]
```

### Quantile Classification (same IQR logic as Project 4)

```python
Q1 = df["Price"].quantile(0.25)
Q2 = df["Price"].quantile(0.50)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

# Classify into 6 categories:
# OutliersOverQ3 / >75% / 50-75% / 25-50% / <25% / OutliersBelowQ1
```

### Geoprocessing Pipeline

```python
import arcpy

# Join state boundaries to classified price Excel
joined = arcpy.AddJoin_management(
    inFeatures="StateBoundaries",
    inField="NAME",
    joinTable="classified_gasoline.xlsx/Sheet1$",
    joinField="County"
)

# Export as new feature class
arcpy.CopyFeatures_management(joined, outputfc)

# Set manual interval symbology matching quantile ranges
```

---

## 📊 Results

The output choropleth map classifies all 50 U.S. states into 6 gasoline price tiers:

| Class | Description |
|-------|-------------|
| 🔴 Outliers Over Q3 | Highest-price states (typically West Coast) |
| 🟠 > 75% | High-price states |
| 🟡 50%–75% | Upper-mid price states |
| 🟢 25%–50% | Lower-mid price states |
| 🔵 < 25% | Low-price states (typically South/Midwest) |
| ⚫ Outliers Below Q1 | Lowest-price states |

Regional patterns are clearly visible — Western states tend to cluster in higher price tiers while Gulf Coast and Midwest states appear in lower tiers, consistent with proximity to refinery capacity.

---

## 💡 Key Findings & Limitations

- Directly demonstrates **toolbox reusability**: only variable names and join fields changed from Project 4
- Missing data for some territories required an explicit **data cleaning step** before classification
- The quantile method **handles outlier states** (Hawaii, California) without distorting the classification for other states
- Limitation: the gasoline price data is a **point-in-time snapshot** (2022) and does not reflect seasonal or annual fluctuations
- Future enhancements: add time-series data, overlay with refinery locations, or compute price-per-capita metrics

---

## 🔄 Toolbox Reuse Comparison

| Feature | Project 4 | Project 5 |
|---------|-----------|-----------|
| Geographic Unit | California County | U.S. State |
| Variable | Median Family Income | Retail Gasoline Price |
| Join Field | `COUNTY_NAM` | `NAME` |
| Data Source | CA Census Data | Statista (2022) |
| Output | CA County Choropleth | U.S. State Choropleth |
| Core Logic | ✅ Identical IQR classification | ✅ Identical IQR classification |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **ArcGIS Pro** | Toolbox hosting, map visualization |
| **Python 3 (.pyt)** | Toolbox scripting (extended from Project 4) |
| **arcpy** | `AddJoin_management`, `CopyFeatures_management` |
| **Pandas** | Data cleaning, `DataFrame.quantile()` |
| **U.S. Census Bureau** | State boundary geodatabase |
| **Statista** | Retail gasoline price data source |

---

## 📎 References

- United States Census Bureau (2018). *State Boundaries.* census.gov
- Statista (2022). *Retail prices of motor fuel in the United States by state.* statista.com
- Wikipedia contributors. *United States.* Wikipedia, The Free Encyclopedia.

---

## 📎 Report

See [`Project5_Report.pdf`](Project5_Report.pdf) for full methodology, map outputs, and discussion.
