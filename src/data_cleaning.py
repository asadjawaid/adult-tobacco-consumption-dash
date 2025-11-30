import pandas as pd
import os

RAW_DATA_PATH = "data/raw/dataset/"
CLEANED_DATA_PATH = "data/cleaned/final_cleaned_data.csv"


def load_raw_data():
    """
    Loads multiple raw data CSV files into a dictionary of pandas DataFrames.
    Adds a 'demographic_type' column to each DataFrame.
    """
    files = {
        "age": "Age-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv",
        "employment": "Employment-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv",
        "income": "Income-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv",
        "mental_health": "Mental_Health-Related_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv",
        "race": "Race_and_Ethnic_Disparities_in_Cigarette_Smoking_Among_Adults_20251101.csv",
    }

    datasets = {}

    for demo, filename in files.items():
        path = os.path.join(RAW_DATA_PATH, filename)
        df = pd.read_csv(path)
        df["demographic_type"] = demo
        datasets[demo] = df

    return datasets


def clean_column_names(df):
    """
    Clean DataFrame column names:
    - lowercase
    - replace spaces with underscores
    - remove parentheses
    - remove double underscores
    """

    # Basic clean up
    df.columns = (
        df.columns.str.lower()
                  .str.replace(" ", "_")
                  .str.replace("(", "", regex=False)
                  .str.replace(")", "", regex=False)
                  .str.replace("%", "", regex=False)
                  .str.replace("__", "_")
    )
    # Rename prevalence columns no matter how they appear
    rename_map = {}

    for col in df.columns:
        cleaned = col.replace("__", "_")

        if "cigarette_use_prevalence" in cleaned and "focus" in cleaned:
            rename_map[col] = "prevalence_focus"

        if "cigarette_use_prevalence" in cleaned and "reference" in cleaned:
            rename_map[col] = "prevalence_reference"

    df = df.rename(columns=rename_map)

    return df


def clean_dataset(df):
    """
    Clean an individual demographic dataset.
    """
    df = clean_column_names(df)

    if "year" in df.columns:
        df["year"] = df["year"].astype(int)

    numeric_cols = [
        col for col in df.columns
        if "prevalence" in col or "disparity" in col
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop_duplicates()

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    return df


def merge_all(datasets):
    """
    Merge all demographic datasets into one unified dataset.
    """
    return pd.concat(datasets.values(), ignore_index=True)


def save_cleaned(df):
    """
    Save the cleaned dataset to the cleaned data directory.
    """
    os.makedirs("data/cleaned", exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)
    print(f"Saved cleaned dataset to: {CLEANED_DATA_PATH}")


# -----------------------------------------------------------------------------
# MAIN EXECUTION FUNCTION
# -----------------------------------------------------------------------------
# The main() function is responsible for executing the entire data cleaning
# pipeline when this script is run directly (e.g., `python data_cleaning.py`).
#
# It performs the following tasks:
#   1. Loads all raw demographic datasets (age, race, income, employment,
#      mental health) from the data/raw/dataset/ directory.
#   2. Cleans each dataset by standardizing column names, converting
#      datatypes, removing duplicates, and formatting categorical values.
#   3. Merges all cleaned datasets into a single unified dataframe.
#   4. Saves the final cleaned dataset to data/cleaned/final_cleaned_data.csv.
#
# This function allows the data cleaning phase to be run independently from the
# Dash application and ensures that other modules only need to load the cleaned
# data file instead of processing raw data every time.
#
# NOTE:
# Do NOT delete this block. It is essential for running the cleaning pipeline
# as a standalone script and follows the Single Responsibility Principle by
# separating preprocessing logic from the Dash app components.
# -----------------------------------------------------------------------------
def main():
    datasets = load_raw_data()

    for key in datasets:
        datasets[key] = clean_dataset(datasets[key])

    final_df = merge_all(datasets)
    save_cleaned(final_df)


if __name__ == "__main__":
    main()