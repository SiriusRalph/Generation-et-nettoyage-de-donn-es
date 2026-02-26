import pandas as pd
import numpy as np
import os


def remove_duplicates(df):
    return df.drop_duplicates()


def handle_missing(df, method="fill"):
    if method == "fill":
        return df.fillna("Unknown")
    else:
        return df.dropna()


def fix_types(df):
    df["Transaction Amount"] = pd.to_numeric(df["Transaction Amount"], errors="coerce")
    df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")
    return df


def standardize_columns(df):
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def validate_values(df):
    df.loc[df['transaction_amount'] < 0, 'transaction_amount'] = 0
    return df


def clean_data(file_path):
    df = pd.read_excel(file_path)
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = fix_types(df)
    df = standardize_columns(df)
    df = validate_values(df)

    output_dir = "cleaned_data"
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.basename(file_path)
    cleaned_file = os.path.join(output_dir, "cleaned_" + base_name)
    df.to_excel(cleaned_file, index=False)
    return df, cleaned_file
