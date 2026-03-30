# 📋 Changelog

All notable changes to this project are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) conventions.

---

## [v1.0.0] — Deliverable 1 · March 29, 2026

### ✅ Added

#### 📦 Data Loading & Merging (`01_data_loading_and_merging`)
- Loaded and validated all **53 CSV files** from the Crop Prices Dataset of Pakistan
- Implemented schema validation to skip files missing required columns (`City`, `Date`, `Crop`, `Price`)
- Applied date parsing with explicit format strings and numeric coercion on the `Price` column
- Removed rows with invalid `Date` or `Price` values after coercion
- Merged all valid files into a single unified dataset of **~7.99 million records**
- Applied chronological sorting per `(City, Crop)` pair for correct time-series ordering
- Saved the final merged output as `merged_crop_prices.csv`

**Dataset Stats at Merge:**
| Attribute | Value |
|-----------|-------|
| Total Records | ~7.99 Million |
| Unique Cities | 138 |
| Unique Crops | 76 |
| Source Files | 53 CSV files |
| Date Range | 2008 – 2024 |

---

#### 🧹 Preprocessing & EDA (`02_preprocessing_exploratory_data_analysis`)
- Removed unnamed index columns and exact duplicate records
- Applied **IQR-based outlier removal** per `(City, Crop)` group (1.5× IQR rule)
- Extracted calendar features: `Year`, `Month`, `Day`, `DayOfWeek`, `Quarter`
- Normalized prices using **Min-Max scaling per crop** → `Normalized_Price` column
- Label-encoded `City` and `Crop` columns for downstream ML compatibility
- Filtered out `(City, Crop)` pairs with fewer than 100 observations
- Generated **9 EDA visualizations** saved to `outputs/EDA + Visualization/`:
  - `price_distribution.png`
  - `time_series_trend.png`
  - `yearly_trend.png`
  - `top_crops_analysis.png`
  - `crop_distribution.png`
  - `monthly_seasonality.png`
  - `city_comparison.png`
  - `volatility.png`
  - `correlation_heatmap.png`

---

#### 📈 Basic Time-Series Analysis (`03_basic_time_series_analysis`)
- Selected **Banana(DOZENS) in Vehari** as the representative series (most observations)
- Plotted raw price trend over the full date range (`plot_series.png`)
- Computed **7-day and 30-day moving averages** to isolate short and long-term trends (`moving_average.png`)
- Computed **30-day rolling mean and rolling standard deviation** to quantify price stability and volatility (`rolling_statistics.png`)

---

#### 🔬 Advanced Time-Series Analysis (`04_advanced_time_series_analysis`)
- Selected **top 5 crops** by observation count: Banana(DOZENS), Garlic(China), Cauliflower, Green Chilli, Cucumber(Kheera)
- Aggregated multi-city data into a single national daily mean series per crop
- Applied **classical additive seasonal decomposition** (period=30) per crop → `decompose.png`
- Ran **Augmented Dickey-Fuller (ADF) stationarity test** on all 5 series:
  - ✅ Stationary (p < 0.05): Cauliflower, Green Chilli, Cucumber(Kheera)
  - ⚠️ Non-Stationary: Banana(DOZENS) (p=0.059), Garlic(China) (p=0.230)
- Applied **first-order differencing** to non-stationary series → confirmed stationarity post-differencing
- Generated per-crop seasonal pattern charts and a cross-crop trend comparison (`compare_trends_top_crops.png`)

---

#### 🧠 Temporal Feature Engineering (`05_temporal_feature_engineering`)
- Built an **18-feature model-ready matrix** from the preprocessed dataset:

| Feature Group | Features |
|---------------|---------|
| Lag Features | `lag_1`, `lag_3`, `lag_7`, `lag_14` |
| Rolling Statistics | `rolling_mean_3`, `rolling_mean_7`, `rolling_mean_14`, `rolling_std_3`, `rolling_std_7` |
| Exponential Moving Average | `ema_7`, `ema_14` |
| Momentum | `price_diff`, `price_pct_change` |
| Volatility | `volatility_7` |
| Cyclical Encoding | `month_sin`, `month_cos` |
| Group Identifiers | `City_encoded`, `Crop_encoded` |

- Removed rows containing `NaN` or `Inf` values after feature creation
- Applied **StandardScaler** to the full feature matrix → ready for model training

---

#### 📁 Project Infrastructure
- Added `README.md` with badges, pipeline overview, key findings, and contributor section
- Added `CONTRIBUTING.md` with branch strategy, commit guidelines, and PR process
- Added `LICENSE` (MIT)
- Added `requirements.txt`
- Added `.gitignore` configured for Python / Jupyter / Google Colab

---

## [Unreleased] — Deliverable 2 · Coming Soon

### 🔜 Planned

- [ ] ACF and PACF analysis on top 5 crop series
- [ ] ARIMA model training with automated order selection
- [ ] Holt-Winters Exponential Smoothing implementation
- [ ] ML Models: Linear Regression and Random Forest baseline
- [ ] Temporal train-test split (chronological, no data leakage)
- [ ] Evaluation metrics: MAE, RMSE, MAPE per model per crop
- [ ] Preliminary model comparison table

---

## [Unreleased] — Final Deliverable · Coming Soon

### 🔜 Planned

- [ ] Hyperparameter tuning (ARIMA grid search, RF param sweep)
- [ ] Residual analysis and diagnostic plots
- [ ] Clustering analysis (if required)
- [ ] Final comparative evaluation across all models
- [ ] Long-term trend and seasonal insight extraction
- [ ] Complete analytical report and presentation slides

---

> **Versioning:** This project uses `vX.0.0` tags per deliverable submission.
> Tag `v1.0.0` corresponds to the Deliverable 1 submission on March 29, 2026.
