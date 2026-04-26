# 🎭 Mapping LA Cultural Centers & Theaters with ArcPy

![Python](https://img.shields.io/badge/Python-ArcPy-blue?logo=python)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-10.x%2F3.x-blue?logo=esri)
![Data](https://img.shields.io/badge/Data-LA%20Dept.%20of%20Cultural%20Affairs-purple)
![Course](https://img.shields.io/badge/Course-SSCI%20586%20GIS%20Programming-green)

## Overview

This project demonstrates **end-to-end geospatial data automation using Python and ArcPy** — from raw tabular coordinates in a CSV file to a fully rendered point shapefile visualized in ArcGIS Pro.

The dataset contains **29 Department of Cultural Affairs (DCA) Cultural Centers and Theaters** across Los Angeles, with geographic coordinates collected from Google Earth and imported programmatically.

---

## 🎯 Objectives

- Collect geographic coordinates (X/Y/Z) for all DCA Cultural Centers and Theaters in LA
- Build a Python script using `arcpy.management.XYTableToPoint()` to convert CSV → Shapefile
- Validate the output by row count and visual inspection in ArcGIS Pro
- Produce a publication-quality map of cultural facility distribution across Los Angeles

---

## 🗺️ Study Area

**Los Angeles, California** — center of the nation's film and television industry, with a rich network of publicly accessible cultural centers and theaters serving diverse communities across the city.

---

## 📂 Repository Structure

```
project2-cultural-centers-arcpy/
├── Project2_Report.pdf                  # Full project write-up
├── scripts/
│   ├── py script.png                    # Script screenshot
│   └── workflow.py                      # ArcPy automation script
├── data/
│   └── DCA_Cultural_Centers_and_Theaters.csv  # Input coordinate table (29 locations)
├── maps/
│   └── finished map.png                 # Final map output
└── README.md
```

---

## 🗃️ Dataset

**DCA Cultural Centers & Theaters** (`data/DCA_Cultural_Centers_and_Theaters.csv`)

| Column | Type | Description |
|--------|------|-------------|
| `center name` | String | Name of the cultural facility |
| `X_Long` | Float | Longitude (WGS 1984) |
| `Y_Lati` | Float | Latitude (WGS 1984) |
| `Z_Elevation_ft` | Float | Elevation in feet |

- **29 rows** (one per facility)
- Projection applied on conversion: **EPSG 4326 (WGS 1984)**

---

## ⚙️ Methodology & Script

The core of this project is a single Python script using the ArcPy library:

```python
import arcpy

# Environment settings
arcpy.env.workspace = "path/to/project2"

# Variables
in_table = "DCA_Cultural_Centers_and_Theaters.csv"
out_feature_class = "DCA_Cultural_Centers_and_Theaters.shp"
x_coords = "X_Long"
y_coords = "Y_Lati"
z_coords = "Z_Elevation_ft"

# Convert XY table to point shapefile
arcpy.management.XYTableToPoint(
    in_table, out_feature_class,
    x_coords, y_coords, z_coords,
    arcpy.SpatialReference(4326)
)

# Validate row count
print(arcpy.GetCount_management(out_feature_class))  # Expected: 29
```

See the full script: [`scripts/workflow.py`](scripts/workflow.py)

**Steps:**
1. Set ArcPy workspace environment
2. Define local variables (table path, output name, coordinate field names)
3. Call `XYTableToPoint()` with WGS 1984 spatial reference
4. Validate output with `GetCount_management()` — confirms 29 points created
5. Verify visual placement in ArcGIS Pro

---

## 📊 Results

- ✅ **29 point features** created from the CSV — matching expected row count
- Points accurately placed across Los Angeles with **even geographic distribution**
- Map reveals cultural facilities serve multiple LA neighborhoods, from Downtown to the West Side
- Output shapefile is fully attributed with facility names for pop-up labeling

---

## 💡 Key Findings & Limitations

- Cultural centers appear **geographically distributed** across LA, suggesting broad community access
- The shapefile only contains name + coordinates — **no address, hours, or contact info**
- A richer dataset (with operational attributes) could support accessibility analysis, such as proximity to transit or underserved census tracts
- This workflow is **reusable** for any point-based dataset (e.g., mapping real estate properties, business locations, service facilities)

---

## 🛠️ Tools & Technologies

- **Python 3** with `arcpy` (ArcGIS Pro)
- **ArcGIS Pro** — visualization and validation
- **Google Earth** — coordinate collection
- **Key Function:** `arcpy.management.XYTableToPoint()`

---

## 📎 Report

See [`docs/Project2_Report.pdf`](docs/Project2_Report.pdf) for full methodology, screenshots, and discussion.
