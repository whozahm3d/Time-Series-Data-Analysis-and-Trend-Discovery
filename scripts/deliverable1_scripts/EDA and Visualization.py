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

