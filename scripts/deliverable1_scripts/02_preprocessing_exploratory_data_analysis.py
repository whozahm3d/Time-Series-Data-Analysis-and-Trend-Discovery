# Perform exploratory data analysis (EDA) on merged crop price dataset.
# Includes statistical summaries, time-based feature extraction, and visualization for trend discovery.
# Comprehensive preprocessing pipeline for time-series crop price data.
# - Missing value handling
# - Time-series regularization
# - Feature engineering
# - Normalization
# - Data filtering

# DIRECTORY SETUP

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


BASE_DIR = "outputs"
create_dir(BASE_DIR)

DATA_FILE = "/content/merged_crop_prices.csv"
print("Data path checked and load into a particular varialble successfully!")

df = pd.read_csv(DATA_FILE)
df.head()

unnamed_cols = [col for col in df.columns if 'Unnamed' in col]
print(f"Columns to be removed: {unnamed_cols}")

df = df.drop(columns=unnamed_cols)

print("DataFrame after removing 'Unnamed' columns:")
df.head()

## Basic data overview and it's Inspection
def dataset_shape(df):
    print("Dataset Shape:", df.shape)

dataset_shape(df)

def dataset_columns(df):
    print("Columns:\n", df.columns)
     
dataset_columns(df)

def dataset_datatypes(df):
    print("Data Types:\n", df.dtypes)
     
dataset_datatypes(df)

def dataset_head(df):
    print("First 5 Rows:\n", df.head())
     
dataset_head(df)

def dataset_description(df):
    print("Statistical Summary:\n", df.describe())
  
dataset_description(df)

def missing_values(df):
    print("Missing Values:\n", df.isnull().sum())
     
missing_values(df)

def unique_cities(df):
    print("\nUnique Cities:", df["City"].nunique())
     
unique_cities(df)

def unique_crops(df):
    print("Unique Crops:", df["Crop"].nunique())
     
unique_crops(df)

## Cleaning the entire dataset

def remove_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    print("Duplicates removed:", before - after)
    print("\n[INFO] Removing duplicate records...")
    df = df.drop_duplicates(subset=["City", "Crop", "Date"])
    return df
     

# OUTLIER HANDLING (MODIFIED)

def remove_outliers(df):
    print("[INFO] Removing outliers using IQR...")

    def filter_group(group):
        Q1 = group["Price"].quantile(0.25)
        Q3 = group["Price"].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        return group[(group["Price"] >= lower) & (group["Price"] <= upper)]

    df = df.groupby(["City", "Crop"]).apply(filter_group).reset_index(drop=True)

    return df
     
df = remove_outliers(df)

def fill_missing_dates(df):
    """
    For each (City, Crop), ensure continuous date sequence.
    """

    print("[INFO] Filling missing dates (time-series regularization)...")

    # Ensure Date column is datetime type before processing
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    # Drop rows where Date could not be parsed, to prevent issues with min/max or grouping
    df = df.dropna(subset=["Date"])

    processed_groups = []

    grouped = df.groupby(["City", "Crop"])

    for (city, crop), group in grouped:

        group = group.sort_values("Date")

        group = group.groupby("Date")["Price"].mean().reset_index() # Handle duplicate dates by taking the mean of 'Price'
        group["City"] = city
        group["Crop"] = crop

        full_range = pd.date_range(start=group["Date"].min(),
                                   end=group["Date"].max(),
                                   freq='D')

        group = group.set_index("Date").reindex(full_range) # Reindex to ensure continuous dates, filling missing dates with NaN for Price

        # Re-assign City and Crop as they might become NaN during reindex for new dates
        group["City"] = city
        group["Crop"] = crop

        group["Price"] = group["Price"].interpolate(method='linear', limit_direction='both') # Interpolate missing prices, including those at the start/end
        group["Price"] = group["Price"].fillna(method='ffill').fillna(method='bfill') # Fill any remaining NaNs using forward-fill then backward-fill

        group = group.reset_index().rename(columns={"index": "Date"})

        processed_groups.append(group)

    df = pd.concat(processed_groups, ignore_index=True)

    return df


## Featuring and normalization

# FEATURE ENGINEERING (TIME FEATURES)
def create_time_features(df):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["DayOfWeek"] = df["Date"].dt.dayofweek

    return df
     
create_time_features(df)

# NORMALIZATION (ADAPTED)
def normalize_prices(df):
    print("[INFO] Normalizing prices (Min-Max scaling per crop)...")
    df["Normalized_Price"] = df.groupby("Crop")["Price"].transform(
        lambda x: (x - x.min()) / (x.max() - x.min())
    )
    return df
df = normalize_prices(df)

# FILTER LOW-DATA SERIES
def filter_short_series(df, min_length=100):
    print("[INFO] Filtering short time-series...")

    valid_series = df.groupby(["City", "Crop"]).filter(lambda x: len(x) >= min_length)
    return valid_series
  
def encode_categorical(df):
    print("[INFO] Encoding categorical variables...")

    le = LabelEncoder()

    df["City_encoded"] = le.fit_transform(df["City"])
    df["Crop_encoded"] = le.fit_transform(df["Crop"])

    return df
df = encode_categorical(df)

df.head()

## Preprocessing Pipeline
# MAIN PIPELINE

def run_pipeline(df):
    print("======================================")
    print(" PREPROCESSING PIPELINE ")
    print("======================================\n")

    print("\n========== DATASET INSPECTION ==========")

    dataset_shape(df)
    dataset_columns(df)
    dataset_datatypes(df)
    dataset_head(df)
    dataset_description(df)
    missing_values(df)

    print("\n========== PREPROCESSING ==========")

    df = remove_duplicates(df)
    df = fill_missing_dates(df)
    filter_short_series(df)

    print("\nPREPROCESSING COMPLETED!")

    print("\nFinal Dataset Info:")
    print(df.info())

    return df

run_pipeline(df)


CLEANED_OUTPUT_FILE = Path("/content/cleaned_merged_crop_prices.csv")

df.to_csv(CLEANED_OUTPUT_FILE, index=False)
print(f"[INFO] Cleaned dataset saved at: {CLEANED_OUTPUT_FILE}")

CLEANED_OUTPUT_FILE = "/content/cleaned_merged_crop_prices.csv"
files.download(CLEANED_OUTPUT_FILE)

OUTPUT_FILE = "/content/merged_crop_prices.csv"
files.download(OUTPUT_FILE)

df = pd.read_csv("/content/cleaned_merged_crop_prices.csv")
df['Date'] = pd.to_datetime(df['Date'])

df.head()


## EDA + Visualizations
# SAVE + SHOW FUNCTION

def save_and_show(name, folder):
    create_dir(folder)
    path = os.path.join(folder, f"{name}.png")
    plt.savefig(path, bbox_inches="tight")
    plt.show()
    print(f"[SAVED] {path}")

# FINAL EDA (ADAPTED FROM YOUR STRUCTURE)
# 1. Price Distribution
def plot_price_distribution(df):
    plt.figure()
    plt.hist(df["Price"], bins=50)
    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    save_and_show("price_distribution", "outputs/distribution")
     
plot_price_distribution(df)

# 2. Time-Series Trend
def plot_time_series(df):
    ts = df.groupby("Date")["Price"].mean()

    plt.figure()
    plt.plot(ts.index, ts.values)
    plt.title("Overall Price Trend Over Time")
    save_and_show("time_series_trend", "outputs/trends")

plot_time_series(df)

# 3. YEARLY TREND

def yearly_trend(df):
    print("\n[INFO] Analyzing yearly trends...")

    yearly_avg = df.groupby("Year")["Price"].mean()

    plt.figure()
    plt.plot(yearly_avg.index, yearly_avg.values)
    plt.title("Yearly Average Price Trend")
    plt.xlabel("Year")
    plt.ylabel("Average Price")
    save_and_show("yearly_trend", "outputs/trends")
    
yearly_trend(df)

# 4. TOP CROPS ANALYSIS

def top_crops_analysis(df):
    print("\n[INFO] Analyzing top crops...")

    top_crops = df["Crop"].value_counts().head(5).index

    plt.figure()

    for crop in top_crops:
        subset = df[df["Crop"] == crop]
        grouped = subset.groupby("Date")["Price"].mean()

        plt.plot(grouped.index, grouped.values, label=crop)

    plt.title("Top 5 Crops Price Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Average Price")
    plt.legend()
    save_and_show("top_crops_analysis", "outputs/analysis")
     
top_crops_analysis(df)

# 5. Crop Distribution
def crop_distribution(df):
    counts = df["Crop"].value_counts().head(10)

    plt.figure()
    plt.bar(counts.index, counts.values)
    plt.xticks(rotation=45)
    plt.title("Top Crops Distribution")

    save_and_show("crop_distribution", "outputs/crops")
     
crop_distribution(df)

# 6. Monthly Seasonality or # Seasonal Analysis
def monthly_seasonality(df):
    print("\n[INFO] Analyzing monthly seasonality...")
    monthly_avg = df.groupby("Month")["Price"].mean()

    plt.figure()
    plt.plot(monthly_avg.index, monthly_avg.values)
    plt.title("Average Monthly Price (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Average Price")

    save_and_show("monthly_seasonality", "outputs/seasonality")
     
monthly_seasonality(df)

# 7. City-wise Comparison
def city_comparison(df):
    print("\n[INFO] Comparing cities...")
    city_avg = df.groupby("City")["Price"].mean().sort_values(ascending=False).head(10)

    plt.figure()
    plt.bar(city_avg.index, city_avg.values)
    plt.xticks(rotation=45)
    plt.title("Top Cities by Avg Price")

    save_and_show("city_comparison", "outputs/city")
     
city_comparison(df)

# 8. Volatility (Important Insight)
def volatility_plot(df):
    print("\n[INFO] Calculating crop volatility...")

    vol = df.groupby("Crop")["Price"].std().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 6)) # Increase figure size
    plt.bar(vol.index, vol.values)
    plt.title("Top 10 Most Volatile Crops")
    plt.xlabel("Crop")
    plt.ylabel("Standard Deviation (Volatility)")
    plt.xticks(rotation=45) # Rotate labels to 90 degrees
    plt.tight_layout() # Adjust layout to prevent labels from overlapping

    save_and_show("volatility", "outputs/volatility")
    
volatility_plot(df)

# 9. correlation Heatmap
def plot_correlation_heatmap(df, cmap='viridis'):
    """
    Generate and save correlation heatmap
    """

    create_dir("outputs/heatmap")

    # Select only numeric columns
    numerical_df = df.select_dtypes(include=[np.number])

    corr = numerical_df.corr()

    plt.figure(figsize=(12, 8))

    sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap)

    plt.title("Correlation Heatmap")
    save_and_show("correlation_heatmap", "outputs/heatmap")
     
plot_correlation_heatmap(df, cmap='mako')


# 1. MISSING DATE HANDLING
# Time-series data must be continuous for meaningful analysis.
# We generate a full daily date range for each (City, Crop) pair and fill missing values using linear interpolation.

# 2. OUTLIER REMOVAL
# Extreme price spikes can distort trend analysis.
# We use IQR-based filtering per group to remove anomalies.

# 3. FEATURE ENGINEERING
# Time-based features (Month, DayOfWeek) help capture seasonality.

# 4. NORMALIZATION
# Prices differ greatly across crops (e.g., Apple vs Onion).
# We normalize per crop to make patterns comparable.

# 5. FILTERING SHORT SERIES
# Very short time-series are unreliable for analysis,
# so we remove groups with insufficient data.

# 6. This preprocessing ensures:
# - clean time-series structure
# - comparable data across crops
# - reliable trend and clustering results
     
