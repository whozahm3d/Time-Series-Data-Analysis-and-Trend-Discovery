# Time-Series Data Mining for Trend Discovery in Pakistan’s Crop Prices

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Data Mining](https://img.shields.io/badge/Project-Type%3A%20Data%20Mining-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

Agricultural commodity prices in Pakistan fluctuate due to seasonal production cycles, supply chain factors, inflation, and market demand. Understanding these trends can help farmers, policymakers, and researchers make better decisions.

This project applies **time-series data mining techniques** to analyze historical crop price data collected from agricultural markets in Pakistan. The goal is to discover **seasonal patterns, long-term trends, and price volatility** in crop markets.

This project was developed as part of the **DS3005 – Data Mining Term Project (Spring 2026)**.

---

## Objectives

The main objectives of this project are:

- Analyze historical crop price data
- Identify **long-term price trends**
- Discover **seasonal price patterns**
- Detect **price fluctuations and anomalies**
- Visualize agricultural market behavior

---

## Dataset

The dataset contains historical crop price records from agricultural markets across Pakistan.

### Dataset Attributes

| Attribute | Description |
|-----------|-------------|
| Date | Date of price observation |
| Crop | Name of the crop |
| Market | Market location |
| Min Price | Minimum price recorded |
| Max Price | Maximum price recorded |
| Avg Price | Average market price |

### Example Crops

- Wheat  
- Rice  
- Maize  
- Potato  
- Onion  
- Tomato  

Dataset Source: **Kaggle – Pakistan Crop Prices Dataset**

---

## Methodology

The project follows a typical **data mining workflow**.

### 1. Data Preprocessing
- Handling missing values
- Converting date columns to time-series format
- Removing duplicates
- Detecting and handling outliers

### 2. Exploratory Data Analysis (EDA)
- Crop-wise price distributions
- Market-level comparisons
- Visualization of price fluctuations

### 3. Time-Series Analysis

Techniques used include:

- Moving averages
- Trend analysis
- Seasonal decomposition
- Volatility analysis

### 4. Trend Discovery

The analysis helps identify:

- Seasonal crop price cycles
- Long-term agricultural price trends
- Price spikes and unusual anomalies

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Jupyter Notebook

---

## Project Structure
- pakistan-crop-price-time-series-analysis
- │
- ├── data
- │ └── crop_prices.csv
- │
- ├── notebooks
- │ └── analysis.ipynb
- │
- ├── src
- │ ├── preprocessing.py
- │ ├── trend_analysis.py
- │ └── visualization.py
- │
- ├── results
- │ ├── plots
- │ └── reports
- │
- ├── requirements.txt
- ├── README.md
- └── LICENSE



### Folder Description

| Folder | Description |
|------|-------------|
| `data/` | Contains the dataset used for analysis |
| `notebooks/` | Jupyter notebooks for exploratory analysis |
| `src/` | Python scripts for preprocessing, analysis, and visualization |
| `results/` | Generated plots and output reports |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `LICENSE` | Project license |

---

## Key Insights

The analysis provides insights into:

- Crop price fluctuations over time
- Seasonal agricultural price patterns
- Price instability in certain commodities
- Long-term agricultural market trends

---

## Future Improvements

Possible future extensions include:

- Time-series forecasting using **ARIMA / SARIMA**
- Machine learning models for crop price prediction
- Regional market comparisons
- Integration with weather and climate datasets

---

## Author

**Ali Ahmad**  
BS Data Science

---

## License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for more details.
