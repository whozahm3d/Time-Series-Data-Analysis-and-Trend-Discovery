<div align="center">

# 🌾 Time-Series Data Analysis and Trend Discovery in Pakistan's Crop Prices

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-B8860B?style=for-the-badge)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-In%20Progress-2E7D32?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan)

> A data mining project applying time-series analysis, seasonal decomposition, stationarity testing, and temporal feature engineering to discover patterns and forecast agricultural crop prices across Pakistan (2008–2024).

**Course:** Data Mining &nbsp;|&nbsp; **Institution:** FAST-NUCES &nbsp;|&nbsp; **Semester:** Spring 2026

</div>

---

## 📚 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset Summary](#-dataset-summary)
- [Repository Structure](#️-repository-structure)
- [Pipeline Overview](#️-pipeline-overview)
- [Key Findings](#-key-findings)
- [Sample Outputs](#️-sample-outputs)
- [Tech Stack](#️-tech-stack)
- [How to Run](#-how-to-run)
- [Project Milestones](#-project-milestones)
- [Reports & Documents](#-reports--documents)
- [Contributors](#-contributors)
- [Acknowledgements](#-acknowledgements)
- [License](#-license)

---

## 📌 Project Overview

Agricultural price volatility is a persistent challenge for farmers, policymakers, and market participants in Pakistan. Prices of essential crops fluctuate due to a complex interplay of seasonal cycles, supply-demand dynamics, and climatic factors.

This project addresses this challenge by applying systematic **time-series data mining techniques** to the [Crop Prices Dataset of Pakistan (Kaggle)](https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan) — a dataset containing historical price records across multiple markets with attributes including **crop type**, **city**, **date**, and **price**.

### 🔬 Research Question
> *Can we systematically discover and model seasonal patterns, long-term trends, and abnormal fluctuations in Pakistan's crop prices using time-series data mining techniques?*

---

## 📊 Dataset Summary

| Attribute | Value |
|-----------|-------|
| 📎 Source | [Kaggle — Crop Prices Dataset of Pakistan](https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan) |
| 🗃️ Total Records | ~7.99 Million |
| 📁 Source Files | 53 CSV files |
| 🏙️ Unique Cities | 138 |
| 🌿 Unique Crops | 76 |
| 📅 Date Range | 2008 – 2024 |
| 💰 Avg Price (PKR) | 5,475 |
| 📈 Max Price (PKR) | 97,850 |

---

## 🗂️ Repository Structure

```
📦 pakistan-crop-price-analysis
├── 📓 DM_Project_Deliverable_1.ipynb       # Main notebook — all 5 pipeline stages
│
├── 📁 Images/
│   ├── 📁 EDA + Visualization/             # 9 EDA charts
│   │   ├── time_series_trend.png
│   │   ├── monthly_seasonality.png
│   │   ├── correlation_heatmap.png
│   │   ├── crop_distribution.png
│   │   ├── city_comparison.png
│   │   ├── top_crops_analysis.png
│   │   ├── volatility.png
│   │   ├── price_distribution.png
│   │   └── yearly_trend.png
│   │
│   ├── 📁 basic_time_series/               # Basic TS analysis charts
│   │   ├── plot_series.png
│   │   ├── moving_average.png
│   │   └── rolling_statistics.png
│   │
│   ├── 📁 advanced_time_series/            # Advanced TS analysis charts
│   │   ├── moving_average_advanced.png
│   │   ├── decompose.png
│   │   ├── differencing.png
│   │   ├── seasonal_pattern.png
│   │   └── compare_trends.png
│   │
│   └── 📁 top_5_cross_crops/              # Per-crop analysis (5 crops × 4 charts each)
│       ├── BananaDOZENS_decompose.png
│       ├── BananaDOZENS_differencing.png
│       ├── ... (20 crop-specific charts)
│       └── compare_trends_top_crops.png
│
├── 📄 Data_Mining_Project_Proposal.docx    # Original project proposal
├── 📄 DM_MidSemester_Progress_Report.docx # Mid-semester progress report
├── 📄 LICENSE
└── 📄 README.md
```

---

## ⚙️ Pipeline Overview

The project is structured as **5 sequential, modular pipeline stages**, all implemented inside the main notebook.

| Stage | Module | Description | Output |
|-------|--------|-------------|--------|
| **01** | Data Loading & Merging | Load & validate 53 CSVs, clean, merge chronologically | `merged_crop_prices.csv` |
| **02** | Preprocessing & EDA | IQR outlier removal, normalization, calendar features, 9 visualizations | `outputs/EDA + Visualization/` |
| **03** | Basic Time-Series Analysis | Representative series, 7/30-day MA, rolling statistics | `outputs/basic_time_series/` |
| **04** | Advanced Time-Series Analysis | Seasonal decomposition, ADF test, differencing, cross-crop comparison | `outputs/advanced_time_series/` |
| **05** | Temporal Feature Engineering | Lag features, rolling stats, EMA, cyclical encoding → scaled matrix | Model-ready matrix (18 features) |

```
  Raw CSVs (53 files)
        │
        ▼
┌───────────────────────┐
│  01  Data Loading &   │──► merged_crop_prices.csv (~7.99M rows)
│       Merging         │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│  02  Preprocessing    │──► 9 EDA Visualizations
│       & EDA           │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│  03  Basic            │──► Moving Averages · Rolling Statistics
│       Time-Series     │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│  04  Advanced         │──► Decomposition · ADF Test · Differencing
│       Time-Series     │
└──────────┬────────────┘
           │
           ▼
┌───────────────────────┐
│  05  Feature          │──► 18-Feature Scaled Matrix
│       Engineering     │
└──────────┬────────────┘
           │
           ▼
  ARIMA / Holt-Winters Modeling   ← Deliverable 2
```

---

## 🔍 Key Findings

- 📅 **Strong monthly seasonality** — several crops spike consistently in summer months, likely driven by supply-side climatic constraints.
- 📉 **Highest volatility crops** — Green Chilli and Cucumber show the largest rolling standard deviations across all cities.
- 🧪 **Stationarity results (ADF Test)**:

  | Crop | Result | Action Taken |
  |------|--------|-------------|
  | Cauliflower | ✅ Stationary | None required |
  | Green Chilli | ✅ Stationary | None required |
  | Cucumber (Kheera) | ✅ Stationary | None required |
  | Banana (DOZENS) | ⚠️ Non-Stationary | First-order differencing applied |
  | Garlic (China) | ⚠️ Non-Stationary | First-order differencing applied |

- 📈 **Steepest long-term price growth** — Garlic(China) shows the most consistent upward trend; Cauliflower prices remain comparatively stable over the observed period.

---

## 🖼️ Sample Outputs

All charts are saved automatically to the `outputs/` folder when the notebook is executed.

---

### 📂 EDA & Visualization

<table>
  <tr>
    <td align="center" width="33%">
      <img src="Images/EDA + Visualization/time_series_trend.png" width="100%"/><br/>
      <b>Fig 1. Price Trend Over Time</b><br/>
      <sub>Shows the overall mean crop price trend from 2008–2024. A steady upward drift is visible across the full period, with notable acceleration post-2018.</sub>
    </td>
    <td align="center" width="33%">
      <img src="Images/EDA + Visualization/monthly_seasonality.png" width="100%"/><br/>
      <b>Fig 2. Monthly Seasonality Pattern</b><br/>
      <sub>Average price grouped by month across all crops and cities. Clear seasonal spikes are visible in summer months, reflecting supply constraints during peak heat.</sub>
    </td>
    <td align="center" width="33%">
      <img src="Images/EDA + Visualization/correlation_heatmap.png" width="100%"/><br/>
      <b>Fig 3. Feature Correlation Heatmap</b><br/>
      <sub>Heatmap of Pearson correlations between all numeric features. Strong positive correlation between Price, Normalized_Price, and lag-based features confirms temporal dependency.</sub>
    </td>
  </tr>
</table>

---

### 📂 Basic Time-Series Analysis

<table>
  <tr>
    <td align="center" width="50%">
      <img src="Images/basic_time_series/moving_average.png" width="100%"/><br/>
      <b>Fig 4. Moving Averages (7-Day & 30-Day)</b><br/>
      <sub>Applied on Banana(DOZENS) in Vehari — the most data-rich series. The 7-day MA captures short-term fluctuations while the 30-day MA reveals the underlying long-term trend clearly.</sub>
    </td>
    <td align="center" width="50%">
      <img src="Images/basic_time_series/rolling_statistics.png" width="100%"/><br/>
      <b>Fig 5. Rolling Mean & Std Dev (Volatility)</b><br/>
      <sub>30-day rolling mean and standard deviation plotted together. Periods of wide std deviation indicate high price instability — useful for identifying volatile market intervals.</sub>
    </td>
  </tr>
</table>

---

### 📂 Advanced Time-Series Analysis

<table>
  <tr>
    <td align="center" width="55%">
      <img src="Images/advanced_time_series/decompose.png" width="100%"/><br/>
      <b>Fig 6. Seasonal Decomposition (Trend / Seasonal / Residual)</b><br/>
      <sub>Classical additive decomposition separating the time-series into three interpretable components: a long-term upward trend, a repeating seasonal cycle, and the irregular residual noise.</sub>
    </td>
    <td align="center" width="45%">
      <img src="Images/top 5_cross_crops/compare_trends_top_crops.png" width="100%"/><br/>
      <b>Fig 7. Price Trends Across Top 5 Crops</b><br/>
      <sub>Overlay of national mean price trends for the top 5 most observed crops. Garlic(China) exhibits the steepest upward trajectory while Cauliflower remains the most price-stable crop.</sub>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat) **Python 3.10+** | Core language |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat) **pandas** | Data loading, merging, time-series manipulation |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat) **NumPy** | Numerical computation |
| ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat) **Matplotlib & Seaborn** | Visualization |
| **statsmodels** | Seasonal decomposition, ADF stationarity test |
| ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=flat) **scikit-learn** | Preprocessing, StandardScaler |
| ![Colab](https://img.shields.io/badge/-Google%20Colab-F9AB00?logo=googlecolab&logoColor=white&style=flat) **Google Colab** | Execution environment |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/pakistan-crop-price-analysis.git
cd pakistan-crop-price-analysis
```

### 2. Download the Dataset
Download from Kaggle and place all CSV files inside a folder named `pakistan_crop_prices_dataset/`:

📎 https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan

### 3. Open in Google Colab
Upload `DM_Project_Deliverable_1.ipynb` to [Google Colab](https://colab.research.google.com/) and upload the dataset folder when prompted.

### 4. Run All Cells in Order
The notebook is fully sequential. All output charts are saved automatically to the `outputs/` directory.

---

## 📅 Project Milestones

| # | Task | Deliverable | Status |
|---|------|------------|--------|
| 1 | Dataset loading, validation & merging (53 CSV files) | Deliverable 1 | ✅ Complete |
| 2 | Missing value handling & outlier removal (IQR) | Deliverable 1 | ✅ Complete |
| 3 | Calendar feature extraction & price normalization | Deliverable 1 | ✅ Complete |
| 4 | Exploratory data analysis (9 visualizations) | Deliverable 1 | ✅ Complete |
| 5 | Basic time-series: moving averages & rolling statistics | Deliverable 1 | ✅ Complete |
| 6 | Advanced TS: decomposition, ADF test, differencing | Deliverable 1 | ✅ Complete |
| 7 | Cross-crop trend comparison (top 5 crops) | Deliverable 1 | ✅ Complete |
| 8 | Temporal feature engineering (18 features, scaled matrix) | Deliverable 1 | ✅ Complete |
| 9 | ACF/PACF analysis & ARIMA model training | Final | ⏳ Pending |
| 10 | Holt-Winters Exponential Smoothing implementation | Final | ⏳ Pending |
| 11 | ML Models: Linear Regression & Random Forest | Final | ⏳ Pending |
| 12 | Evaluation: MAE, RMSE, MAPE on temporal train-test split | Final | ⏳ Pending |
| 13 | Hyperparameter tuning & residual analysis | Final | ⏳ Pending |
| 14 | Clustering analysis (if required) | Final | ⏳ Pending |
| 15 | Final comparative evaluation & trend insight extraction | Final | ⏳ Pending |
| 16 | Complete analytical report & visualizations | Final | ⏳ Pending |

---

## 📄 Reports & Documents

- 📄 [Project Proposal](./Data_Mining_Project_Proposal.docx)
- 📄 [Mid-Semester Progress Report](./DM_MidSemester_Progress_Report.docx)

---

## 👥 Contributors

<table>
  <tr>
    <td align="center">
      <b>Taha Nawaz</b><br/>
      <sub>23L-2644</sub><br/>
    </td>
    <td align="center">
      <b>Ali Ahmad</b><br/>
      <sub>23L-2619</sub><br/>
    </td>
    <td align="center">
      <b>Shahzeb Imran</b><br/>
      <sub>23L-2506</sub><br/>
    </td>
  </tr>
</table>

---

## 🙏 Acknowledgements

- **Dataset** — [Humaira Rana](https://www.kaggle.com/datasets/humairarana/crop-prices-dataset-of-pakistan) for making the Crop Prices Dataset of Pakistan publicly available on Kaggle.
- **Course Instructor** — For guidance and structure throughout the Data Mining project at FAST-NUCES.
- **Open-Source Libraries** — The Python ecosystem — pandas, statsmodels, scikit-learn, matplotlib, and seaborn — that made this analysis possible.

---

## 📃 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

Developed for academic purposes at FAST-NUCES as part of the Data Mining course (Spring 2026).

---

<div align="center">

*Made with ❤️ at FAST-NUCES · Spring 2026*

</div>
