<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=2E4057&height=200&section=header&text=Pakistan%20Crop%20Price%20Analysis&fontSize=36&fontColor=ffffff&fontAlignY=38&desc=Time-Series%20Data%20Mining%20%7C%20FAST-NUCES%20Spring%202026&descAlignY=58&descSize=16" width="100%"/>

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
├── 📁 outputs/
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

| Chart | Description |
|-------|-------------|
| `time_series_trend.png` | Mean price across all crops (2008–2024) |
| `monthly_seasonality.png` | Average price per month — reveals seasonal peaks |
| `correlation_heatmap.png` | Correlation between all numeric features |
| `moving_average.png` | 7-day and 30-day MA on representative series (Banana, Vehari) |
| `rolling_statistics.png` | Rolling mean and std dev — price volatility over time |
| `decompose.png` | Additive decomposition: trend + seasonal + residual |
| `compare_trends_top_crops.png` | Price trend overlay for top 5 crops |

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
| 1 | Data loading, validation & merging (53 CSVs) | Deliverable 1 | ✅ Complete |
| 2 | Preprocessing & EDA (9 visualizations) | Deliverable 1 | ✅ Complete |
| 3 | Basic time-series analysis (MA, rolling stats) | Deliverable 1 | ✅ Complete |
| 4 | Advanced TS: decomposition, ADF, differencing | Deliverable 1 | ✅ Complete |
| 5 | Temporal feature engineering (18 features) | Deliverable 1 | ✅ Complete |
| 6 | ACF/PACF analysis | Deliverable 2 | ⏳ Pending |
| 7 | ARIMA & Holt-Winters model training | Deliverable 2 | ⏳ Pending |
| 8 | Evaluation: MAE, RMSE, MAPE | Deliverable 2 | ⏳ Pending |
| 9 | Hyperparameter tuning & residual analysis | Final | ⏳ Pending |
| 10 | Final comparative report & presentation | Final | ⏳ Pending |

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
      <a href="https://github.com/tahanawaz">@tahanawaz</a>
    </td>
    <td align="center">
      <b>Ali Ahmad</b><br/>
      <sub>23L-2619</sub><br/>
      <a href="https://github.com/aliahmad">@aliahmad</a>
    </td>
    <td align="center">
      <b>Shahzeb Imran</b><br/>
      <sub>23L-2506</sub><br/>
      <a href="https://github.com/shahzebimran">@shahzebimran</a>
    </td>
  </tr>
</table>

> 💡 Update the `@username` links above with your actual GitHub usernames before publishing.

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

<img src="https://capsule-render.vercel.app/api?type=waving&color=2E4057&height=100&section=footer" width="100%"/>

*Made with ❤️ at FAST-NUCES · Spring 2026*

</div>
