# 🐼 Spatial Analysis with GeoPandas — Antwerp & San Diego

![Python](https://img.shields.io/badge/Python-GeoPandas-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![GeoPandas](https://img.shields.io/badge/GeoPandas-0.x-green)
![Course](https://img.shields.io/badge/Course-SSCI%20586%20GIS%20Programming-green)

## Overview

This project explores **open-source GIS with Python** — using GeoPandas, Matplotlib, and JupyterLab to conduct spatial analysis and produce multi-layer maps entirely without proprietary software.

Two study areas are analyzed: **Antwerp, Belgium** (land use) and **San Diego, California** (zoning, streets, and recreation centers) — demonstrating buffer analysis, feature selection, proximity calculations, and publication-quality map rendering.

---

## 🎯 Objectives

- Set up a reproducible Python GIS environment with Anaconda and JupyterLab
- Load and explore shapefile data using GeoPandas `GeoDataFrame`
- Perform spatial operations: feature selection, reprojection, buffering, and proximity analysis
- Produce multi-layer maps combining points, lines, and polygon layers with `matplotlib`

---

## 🗺️ Study Areas

**Antwerp, Belgium** — Historic port city on the River Scheldt. Analysis focuses on land use polygons, filtering water bodies and highlighting green urban areas.

**San Diego, California** — Pacific coast city known for beaches and parks. Analysis covers zoning designations, street centerlines, and recreation center point locations across the city.

---

## 📂 Repository Structure

```
project3-geopandas-spatial-analysis/
├── Project3_Report.pdf               # Full write-up and map outputs
├── notebooks/
│   ├── project3-Antwerp.ipynb            # Antwerp analysis notebook
│   ├── project3-SanDiego.ipynb           # San Diego analysis notebook
│   └── Geopandas - Python for GIS.ipynb  # Reference/tutorial notebook
├── data/                                 # Shapefiles (CRAB_subset, landuse, layer_streets)
└── README.md
```

---

## 🗃️ Datasets

| Dataset | Layer Type | CRS | Description |
|---------|-----------|-----|-------------|
| `landuse` | Polygon | EPSG 2230 | Antwerp land use classifications (incl. Green Urban Areas) |
| `CRAB_subset` | Point | EPSG 2230 | Address points in Antwerp |
| `layer_streets` | LineString | EPSG 2230 | Street centerlines |
| San Diego Zoning | Polygon | EPSG 2230 | Current base zone designations (56,869 features, 47 fields) |
| San Diego Roads | LineString | EPSG 2230 | Road centerlines from all SD County jurisdictions (58 features) |
| Recreation Centers | Point | EPSG 2230 | Recreation facility locations with amenities (3,694 features) |

---

## ⚙️ Methodology

### Data Exploration
```python
import geopandas as gpd
from matplotlib import pyplot as plt

data = gpd.read_file("landuse.shp")
print(data.crs)       # Check projection
print(data.head(3))   # Preview attributes
print(data.bounds)    # Spatial extent
data.hist()           # Attribute distribution
```

### Feature Selection & Filtering
```python
# Exclude water bodies, focus on study extent
filtered = data[
    (data["ITEM"] != "Water bodies") &
    (data.geometry.x > 150000) & (data.geometry.x < 160000)
]
```

### Buffer Analysis
```python
# 300m buffer around Green Urban Areas
green_areas = data[data["ITEM"] == "Green urban areas"]
green_buffer = green_areas.geometry.buffer(300)
```

### Proximity Analysis
```python
# Distance from each address point to nearest green area
addresses["dist_to_green"] = addresses.geometry.apply(
    lambda pt: green_areas.geometry.distance(pt).min()
)
```

### Multi-Layer Map Rendering
```python
fig, ax = plt.subplots(figsize=(12, 10))
filtered.plot(ax=ax, column="ITEM", legend=True)
streets.plot(ax=ax, color="gray", linewidth=0.5)
green_buffer.plot(ax=ax, color="green", alpha=0.3)
plt.show()
```

---

## 📊 Map Outputs (5 Maps Produced)

| Map | Layers | Description |
|-----|--------|-------------|
| 1 | Land use polygons | Antwerp land use by ITEM category |
| 2 | Streets + Green buffer | Gray street lines + 300m green area buffers |
| 3 | Proximity heatmap | Distance-to-green-area for all address points |
| 4 | San Diego zoning | Zone name choropleth (excl. RS-17) with streets |
| 5 | Recreation centers | Point layer over blue-area buffers and zoning polygons |

---

## 💡 Key Findings & Limitations

- GeoPandas provides a **fully open-source alternative** to ArcGIS for spatial analysis workflows
- San Diego's zoning data (56K+ polygons) renders efficiently within a Jupyter environment
- The 300m green area buffer reveals which Antwerp neighborhoods have **limited access to urban green space**
- Proximity analysis can directly inform **equity-focused urban planning** decisions
- Data was already projected to EPSG 2230; no reprojection was required

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python 3** | Core programming language |
| **GeoPandas** | Spatial data I/O and analysis |
| **Matplotlib / pyplot** | Map rendering |
| **Pandas** | Tabular data manipulation |
| **EarthPy** | Reprojection utilities |
| **JupyterLab** | Interactive development environment |
| **Anaconda** | Environment management |

---

## 🚀 Getting Started

```bash
# Create environment
conda create -n gis-env python=3.9
conda activate gis-env
conda install -c conda-forge geopandas matplotlib jupyterlab earthpy

# Launch notebooks
jupyter lab
```

Open `notebooks/project3-SanDiego.ipynb` to run the San Diego analysis.

---

## 📎 Report

See [`Project3_Report.pdf`](Project3_Report.pdf) for full methodology, map outputs, and discussion.
