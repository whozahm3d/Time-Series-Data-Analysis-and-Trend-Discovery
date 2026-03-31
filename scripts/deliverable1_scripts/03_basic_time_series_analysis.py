# To Perform basic time-series analysis on a single representative series.
# It includes:
# - Time-series visualization
# - Moving averages
# - Rolling statistics
# - Basic trend understanding


# SELECT REPRESENTATIVE SERIES

def select_series(df):
    """
    Select most frequent (City, Crop) combination
    """

    print("[INFO] Selecting representative time-series...")

    group_sizes = df.groupby(["City", "Crop"]).size()
    city, crop = group_sizes.idxmax()

    subset = df[(df["City"] == city) & (df["Crop"] == crop)]
    subset = subset.sort_values("Date")

    print(f"Selected → City: {city}, Crop: {crop}")

    return subset, city, crop

select_series(df)

# PLOT ORIGINAL SERIES

def plot_series(df, city, crop):

    plt.figure()
    plt.plot(df["Date"], df["Price"])

    plt.title(f"Price Trend ({crop} - {city})")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()
    save_and_show("plot_series", "outputs/basic_time_series")

series, city, crop = select_series(df)
plot_series(series, city, crop)

# MOVING AVERAGE

def moving_average(df):

    print("[INFO] Calculating moving averages...")

    df["MA_7"] = df["Price"].rolling(window=7).mean()
    df["MA_30"] = df["Price"].rolling(window=30).mean()

    plt.figure()
    plt.plot(df["Date"], df["Price"], label="Original")
    plt.plot(df["Date"], df["MA_7"], label="7-Day MA")
    plt.plot(df["Date"], df["MA_30"], label="30-Day MA")

    plt.title("Moving Average Trends")
    plt.legend()
    save_and_show("moving_average", "outputs/basic_time_series")

    return df

moving_average(series)

# ROLLING STATISTICS

def rolling_statistics(df):

    print("[INFO] Calculating rolling statistics...")

    df["Rolling_Mean"] = df["Price"].rolling(window=30).mean()
    df["Rolling_STD"] = df["Price"].rolling(window=30).std()

    plt.figure()
    plt.plot(df["Date"], df["Rolling_Mean"], label="Rolling Mean")
    plt.plot(df["Date"], df["Rolling_STD"], label="Rolling Std")

    plt.title("Rolling Statistics")
    plt.legend()
    save_and_show("rolling_statistics", "outputs/basic_time_series")

    return df

rolling_statistics(series)

# MAIN PIPELINE

def basic_time_series_pipeline(df):

    print("\n======================================")
    print(" BASIC TIME-SERIES ANALYSIS ")
    print("======================================")

    series, city, crop = select_series(df)

    plot_series(series, city, crop)

    series = moving_average(series)

    rolling_statistics(series)

    print("\n[INFO] Basic time-series analysis completed.")

    return series

basic_time_series_pipeline(df)

df.head()

# EXPLANATION BLOCK
# 1. REPRESENTATIVE SERIES
# We select one (City, Crop) pair with maximum observations to ensure sufficient data for analysis.

# 2. ORIGINAL TIME-SERIES Shows raw price fluctuations over time.
# 3. MOVING AVERAGE - 7-day MA → short-term trend, - 30-day MA → long-term trend
# 4. ROLLING STATISTICS - Rolling Mean → trend stability, - Rolling Std → volatility
# 5. This step helps understand:
# price behavior over time, noise vs trend, volatility patterns
# This builds the foundation for advanced analysis.
