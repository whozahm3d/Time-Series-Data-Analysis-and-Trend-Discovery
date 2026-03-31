# 1. ADVANCED TIME-SERIES FEATURES

def create_advanced_ts_features(df):
    print("[INFO] Creating advanced time-series features...")

    df = df.sort_values(["City", "Crop", "Date"]) # Ensure correct sorting (CRITICAL)

    # LAG FEATURES (Temporal Dependency)
    df["lag_1"] = df.groupby(["City", "Crop"])["Price"].shift(1)
    df["lag_3"] = df.groupby(["City", "Crop"])["Price"].shift(3)
    df["lag_7"] = df.groupby(["City", "Crop"])["Price"].shift(7)
    df["lag_14"] = df.groupby(["City", "Crop"])["Price"].shift(14)

    # ROLLING WINDOW FEATURES (Trend + Stability)
    df["rolling_mean_3"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=3).mean()
    )
    df["rolling_mean_7"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=7).mean()
    )
    df["rolling_mean_14"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=14).mean()
    )

    df["rolling_std_3"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=3).std()
    )
    df["rolling_std_7"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=7).std()
    )

    # MOMENTUM / TREND FEATURES
    df["price_diff"] = df.groupby(["City", "Crop"])["Price"].diff()
    df["price_pct_change"] = df.groupby(["City", "Crop"])["Price"].pct_change()

    # EXPONENTIAL MOVING AVERAGE (ADVANCED TREND)
    df["ema_7"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.ewm(span=7, adjust=False).mean()
    )

    df["ema_14"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.ewm(span=14, adjust=False).mean()
    )

    # VOLATILITY FEATURES
    df["volatility_7"] = df.groupby(["City", "Crop"])["Price"].transform(
        lambda x: x.rolling(window=7).std()
    )

    # SEASONAL INTERACTION (IMPORTANT FOR CROPS)
    df["month_sin"] = np.sin(2 * np.pi * df["Month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["Month"] / 12)

    return df
     

# 2. HANDLE MISSING VALUES

def clean_after_feature_engineering(df):
    print("[INFO] Cleaning NaNs and Infs after feature creation...")
    # Replace infinite values with NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df_clean = df.dropna()

    print("Remaining rows:", df_clean.shape)
    return df_clean
     

# 3. FEATURE MATRIX (FOR DATA MINING)

def build_feature_matrix(df):
    print("[INFO] Building feature matrix...")

    feature_cols = [
        "Normalized_Price",  # Core signal

        "lag_1", "lag_3", "lag_7", "lag_14",  # Lag features

        "rolling_mean_3", "rolling_mean_7", "rolling_mean_14",  # Rolling stats
        "rolling_std_3", "rolling_std_7",

        "price_diff", "price_pct_change",  # Trend & momentum

        "ema_7", "ema_14",   # EMA

        "volatility_7",  # Volatility

        "month_sin", "month_cos",  # Seasonal encoding

        "City_encoded", "Crop_encoded"  # Categorical encodings (already created earlier)
    ]

    X = df[feature_cols]

    print("Feature matrix shape:", X.shape)
    return X
     

# 4. FEATURE SCALING (MANDATORY)

def scale_features(X):
    print("[INFO] Scaling features...")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled
     

# 5. PIPELINE WRAPPER

def run_advanced_feature_engineering(df):
    print("\n===== ADVANCED FEATURE ENGINEERING STARTED =====")

    df = create_advanced_ts_features(df)
    df = clean_after_feature_engineering(df)

    X = build_feature_matrix(df)
    X_scaled = scale_features(X)

    print("===== FEATURE ENGINEERING COMPLETED =====\n")

    return df, X, X_scaled
     

run_advanced_feature_engineering(df)

# Advanced feature engineering was performed to transform raw temporal observations into a high-dimensional
# representation capturing temporal dependencies, seasonal cycles, volatility, and trend dynamics.
# Lag features model temporal memory, rolling statistics capture local trends, while exponential
# moving averages provide smoothed trend estimation. Additionally, cyclical encoding of time variables
# ensures proper representation of seasonal effects inherent in agricultural data.
     
