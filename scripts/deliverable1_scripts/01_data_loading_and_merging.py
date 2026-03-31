# Efficiently load, validate, clean, and merge multiple CSV files
# into a single dataset for time-series analysis.

# CONFIGURATION

DATA_DIR = Path("/content/pakistan_crop_prices_dataset")   # Location of CSV files in Colab
OUTPUT_FILE = Path("/content/merged_crop_prices.csv")

# FUNCTION: Load & Validate Single File

def load_and_validate(file_path):
    """
    Loads a CSV file and validates its schema.
    """

    try:
        df = pd.read_csv(file_path)

        # Expected schema
        required_columns = {"City", "Date", "Crop", "Price"}

        if not required_columns.issubset(df.columns):
            print(f"[WARNING] Skipping {file_path.name} (invalid schema)")
            return None

        return df

    except Exception as e:
        print(f"[ERROR] Failed to read {file_path.name}: {e}")
        return None


def clean_dataframe(df):
    """
    Cleans a single dataframe before merging.
    """

    # Convert Date → datetime
    # Explicitly setting a format to avoid UserWarning about inferring format
    # Common formats include '%Y-%m-%d', '%m/%d/%Y', etc. Choosing '%Y-%m-%d' as a common default.
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")

    # Convert Price → numeric
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["Date", "Price"])

    return df


# FUNCTION: Load All Files Efficiently

def load_all_files(data_dir):
    """
    Loads all CSV files one-by-one (memory efficient).
    """

    csv_files = list(data_dir.glob("*.csv"))

    print(f"\n[INFO] Found {len(csv_files)} CSV files.\n")

    all_dataframes = []

    for idx, file in enumerate(csv_files, 1):
        print(f"[{idx}/{len(csv_files)}] Processing: {file.name}")

        df = load_and_validate(file)

        if df is not None:
            df = clean_dataframe(df)
            all_dataframes.append(df)

    print(f"\n[INFO] Successfully loaded {len(all_dataframes)} datasets.")

    return all_dataframes


# FUNCTION: Merge Datasets

def merge_datasets(dataframes):
    """
    Merge all dataframes into one large dataset.
    """

    print("\n[INFO] Merging datasets...")

    merged_df = pd.concat(dataframes, ignore_index=True)

    print(f"[INFO] Total rows after merge: {len(merged_df)}")

    return merged_df

# FUNCTION: Final Processing

def finalize_dataset(df):
    """
    Final preparation for time-series analysis.
    """

    print("\n[INFO] Finalizing dataset...")

    # Sort for time-series correctness
    df = df.sort_values(by=["Crop", "City", "Date"])

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df

# MAIN PIPELINE

def main():

    print("======================================")
    print(" DATA LOADING & MERGING (COLAB MODE) ")
    print("========================================\n")

    # Step 1: Load all datasets
    datasets = load_all_files(DATA_DIR)

    if len(datasets) == 0:
        print("[ERROR] No valid datasets found. Exiting.")
        return

    # Step 2: Merge
    merged_df = merge_datasets(datasets)

    # Step 3: Final processing
    merged_df = finalize_dataset(merged_df)

    # Step 4: Save dataset
    merged_df.to_csv(OUTPUT_FILE, index=False)

    print(f"\n[INFO] Dataset saved at: {OUTPUT_FILE}")

    # Step 5: Summary (Important for report)
    print("\n========== DATA SUMMARY ==========")
    print(f"Total Records : {len(merged_df)}")
    print(f"Total Cities  : {merged_df['City'].nunique()}")
    print(f"Total Crops   : {merged_df['Crop'].nunique()}")
    print(f"Date Range    : {merged_df['Date'].min()} -> {merged_df['Date'].max()}")
    print("==================================")

if __name__ == "__main__":
    main()

